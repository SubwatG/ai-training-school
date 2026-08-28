/* ==========================================================================
   AI Training School — site/assets/js/app.js
   High-Performance Vanilla JS (Master-Detail Split-Pane & Full View Modes)
   ========================================================================== */

"use strict";

/* ------------------------------------------------------------------------
   1. TOAST NOTIFICATION (Singleton)
   ------------------------------------------------------------------------ */

function ensureToast() {
  let toast = document.getElementById("toast");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "toast";
    toast.setAttribute("role", "status");
    toast.innerHTML = '<span class="dot"></span><span class="toast-msg"></span>';
    document.body.appendChild(toast);
  }
  return toast;
}

let _toastTimer = null;

function showToast(message) {
  const toast = ensureToast();
  const msg = toast.querySelector(".toast-msg");
  if (msg) msg.textContent = message;
  toast.classList.remove("show");
  void toast.offsetWidth;
  toast.classList.add("show");

  clearTimeout(_toastTimer);
  _toastTimer = setTimeout(() => toast.classList.remove("show"), 2200);
}

async function copyText(text, okMessage) {
  const fallbackMessage = okMessage || "คัดลอกเรียบร้อยแล้ว!";
  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
    } else {
      const ta = document.createElement("textarea");
      ta.value = text;
      ta.style.position = "fixed";
      ta.style.opacity = "0";
      document.body.appendChild(ta);
      ta.select();
      document.execCommand("copy");
      document.body.removeChild(ta);
    }
    showToast(fallbackMessage);
    return true;
  } catch (err) {
    console.error("Copy failed:", err);
    showToast("คัดลอกไม่สำเร็จ — ลองกดลากคลุมข้อความเอง");
    return false;
  }
}

/* ------------------------------------------------------------------------
   2. MASTHEAD — active nav link highlighting
   ------------------------------------------------------------------------ */

function initActiveNav() {
  const page = document.body ? document.body.dataset.page : null;
  if (!page) return;
  const links = document.querySelectorAll(".nav-link");
  links.forEach((link) => {
    if (link.dataset.page === page) link.classList.add("active");
  });
}

/* ------------------------------------------------------------------------
   3. HIGH-PERFORMANCE PROMPTS LIBRARY (Master-Detail & Split-Pane)
   ------------------------------------------------------------------------ */

const PromptsLibrary = (() => {
  let rawData = [];
  let promptMap = new Map(); // O(1) lookup cache
  let slotCache = new Map();  // Memoized slot tokens

  let state = {
    q: "",
    task: "all",
    subject: "all",
    tool: "all",
    onlyTop10: false,
    viewMode: "list", // 'list' or 'grid'
    pageSize: 35,
    currentPage: 1,
    activePromptId: null
  };

  const els = {};
  let debounceTimer = null;

  function qs(sel) { return document.querySelector(sel); }
  function qsa(sel) { return Array.from(document.querySelectorAll(sel)); }

  function norm(str) {
    return String(str || "").toLowerCase().normalize("NFKC");
  }

  function extractSlots(text) {
    if (!text) return [];
    if (slotCache.has(text)) return slotCache.get(text);

    const matches = text.match(/\[(.*?)\]/g) || [];
    const unique = [];
    matches.forEach((m) => {
      const raw = m.slice(1, -1).trim();
      if (raw && !unique.includes(raw)) {
        unique.push(raw);
      }
    });
    slotCache.set(text, unique);
    return unique;
  }

  function matchesFilter(p) {
    if (state.onlyTop10 && !p.curated_top10) return false;

    if (state.subject !== "all") {
      const subj = (p.category && p.category.subject) || "";
      if (subj !== state.subject) return false;
    }

    if (state.task !== "all") {
      const task = (p.category && p.category.task_type) || "";
      if (task !== state.task) return false;
    }

    if (state.tool !== "all") {
      const tools = p.tools || [];
      if (!tools.includes(state.tool)) return false;
    }

    if (state.q) {
      if (!p._searchHaystack) {
        p._searchHaystack = norm([
          p.title,
          p.prompt_template,
          p.tips,
          (p.tags || []).join(" "),
          (p.role_context_condition ? Object.values(p.role_context_condition).join(" ") : "")
        ].join(" "));
      }
      if (!p._searchHaystack.includes(norm(state.q))) return false;
    }
    return true;
  }

  function escapeHtml(str) {
    return String(str == null ? "" : str).replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
    }[c]));
  }

  // 1. Build Compact List Row (Master List)
  function buildListRowHTML(p) {
    const subj = (p.category && p.category.subject) || "ทั่วไป";
    const task = (p.category && p.category.task_type) || "";
    const isTop10 = p.curated_top10;
    const promptText = p.prompt_template || "";
    const slots = extractSlots(promptText);

    const isSelected = state.activePromptId === p.id ? "selected" : "";

    return `
      <div class="prompt-row-item flex flex-col sm:flex-row sm:items-center justify-between gap-3 ${isSelected}" data-id="${escapeHtml(p.id)}">
        <div class="min-w-0 flex-1">
          <div class="flex items-center gap-2 mb-1 flex-wrap">
            ${isTop10 ? '<span class="px-2 py-0.5 rounded text-[11px] font-bold text-white uppercase" style="background:var(--accent)">⭐ Top 10</span>' : ''}
            <span class="px-2 py-0.5 rounded-full text-xs font-semibold bg-slate-100 text-slate-700">${escapeHtml(subj)}</span>
            ${task ? `<span class="px-2 py-0.5 rounded-full text-xs font-medium bg-indigo-50 text-indigo-700">${escapeHtml(task)}</span>` : ''}
            ${slots.length > 0 ? `<span class="text-[11px] text-amber-600 font-semibold bg-amber-50 px-1.5 py-0.5 rounded border border-amber-200">⚙️ ${slots.length} ตัวแปร</span>` : ''}
          </div>
          <h3 class="font-display font-bold text-base sm:text-lg text-slate-800 leading-snug group-hover:text-[#E8877A] transition">
            ${escapeHtml(p.title)}
          </h3>
          <p class="text-xs text-slate-500 line-clamp-1 mt-0.5 font-mono">
            ${escapeHtml(promptText)}
          </p>
        </div>
        <div class="flex items-center gap-2 self-end sm:self-center shrink-0">
          <button type="button" class="btn-open-detail text-xs font-bold px-3 py-1.5 rounded-xl border border-slate-200 bg-white hover:bg-slate-50 text-slate-700 flex items-center gap-1">
            <span>ดูเต็ม/ปรับค่า</span>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="m9 18 6-6-6-6"/></svg>
          </button>
          <button type="button" class="copy-btn btn-accent text-xs font-bold !py-1.5 !px-3.5 rounded-xl flex items-center gap-1 shadow-sm">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            <span>คัดลอก</span>
          </button>
        </div>
      </div>
    `;
  }

  // 2. Build Full Card (Expanded Grid Mode)
  function buildCardHTML(p) {
    const tags = (p.tags || [])
      .map((t) => '<span class="tag">' + escapeHtml(t) + "</span>")
      .join("");

    const tools = (p.tools || [])
      .map((t) => '<span class="tag tool font-semibold" style="color:var(--accent)">' + escapeHtml(t) + "</span>")
      .join("");

    const subj = (p.category && p.category.subject) ? '<span class="tag">' + escapeHtml(p.category.subject) + "</span>" : "";
    const task = (p.category && p.category.task_type) ? '<span class="tag font-medium">' + escapeHtml(p.category.task_type) + "</span>" : "";

    const top10Badge = p.curated_top10 ? '<span class="px-2 py-0.5 rounded text-xs font-bold text-white font-display uppercase tracking-wider" style="background:var(--accent)">⭐ Top 10 กู้ชีพครู</span>' : "";

    const promptText = p.prompt_template || "";
    const slots = extractSlots(promptText);

    let rccBlock = "";
    if (p.role_context_condition) {
      const rcc = p.role_context_condition;
      rccBlock =
        '<div class="my-3 p-4 rounded-xl text-sm space-y-1.5" style="background:var(--paper-2); border:1px solid var(--line);">' +
        '<div><strong class="font-bold text-accent" style="color:var(--accent)">บทบาท:</strong> ' + escapeHtml(rcc.role || "-") + '</div>' +
        '<div><strong class="font-bold text-accent" style="color:var(--accent)">บริบท:</strong> ' + escapeHtml(rcc.context || "-") + '</div>' +
        '<div><strong class="font-bold text-accent" style="color:var(--accent)">เงื่อนไข:</strong> ' + escapeHtml(rcc.condition || "-") + '</div>' +
        '</div>';
    }

    let tipsBlock = "";
    if (p.tips) {
      tipsBlock = '<div class="text-xs mb-3 italic text-slate-500">💡 <strong>คำแนะนำตรวจทาน:</strong> ' + escapeHtml(p.tips) + '</div>';
    }

    // Slots Accordion
    let customizerBlock = "";
    if (slots.length > 0) {
      const inputsHtml = slots.map((s) => {
        return (
          '<div class="flex flex-col sm:flex-row sm:items-center gap-1 sm:gap-2 text-sm">' +
          '<label class="sm:w-1/3 text-xs font-bold text-ink-soft truncate" title="' + escapeHtml(s) + '">[' + escapeHtml(s) + ']:</label>' +
          '<input type="text" class="slot-input flex-1 px-3 py-1.5 rounded border text-sm font-sans" data-slot="' + escapeHtml(s) + '" placeholder="พิมพ์ข้อมูลของคุณ..." style="border-color:var(--line); background:#ffffff;">' +
          '</div>'
        );
      }).join("");

      customizerBlock = (
        '<details class="slot-customizer my-3 p-3.5 rounded-xl border text-sm" style="background:var(--paper); border-color:var(--line);">' +
        '<summary class="font-display font-bold text-xs cursor-pointer flex items-center justify-between text-accent hover:opacity-80 select-none">' +
        '<span>⚙️ ปรับแต่งตัวแปรก่อนคัดลอก (' + slots.length + ' ช่อง)</span>' +
        '<span class="text-xs font-normal text-slate-400">คลิกเพื่อกรอกค่า</span>' +
        '</summary>' +
        '<div class="mt-3 pt-3 border-t space-y-2" style="border-color:var(--line);">' +
        inputsHtml +
        '<div class="pt-2 flex justify-end gap-2">' +
        '<button type="button" class="btn-reset-slots text-xs px-3 py-1.5 rounded-lg border hover:bg-gray-100" style="border-color:var(--line); color:var(--ink-soft)">ล้างค่า</button>' +
        '<button type="button" class="btn-copy-customized btn-accent text-xs font-bold px-3.5 py-1.5 rounded-lg flex items-center gap-1 shadow-sm">✨ คัดลอกแบบปรับแต่งแล้ว</button>' +
        '</div>' +
        '</div>' +
        '</details>'
      );
    }

    return (
      '<article class="prompt-card flex flex-col justify-between p-5 rounded-2xl border bg-white shadow-sm hover:shadow-md transition" data-id="' + escapeHtml(p.id) + '" style="border-color:var(--line);">' +
      '<div>' +
      '<div class="flex items-start justify-between gap-3 mb-2">' +
      '<div class="min-w-0">' +
      (top10Badge ? '<div class="mb-1.5">' + top10Badge + '</div>' : '') +
      '<h3 class="font-display font-bold text-lg leading-snug mb-1.5">' + escapeHtml(p.title) + "</h3>" +
      '<div class="flex flex-wrap gap-1.5 mb-1.5">' + tools + task + subj + '</div>' +
      "</div>" +
      '<button type="button" class="copy-btn btn-accent shrink-0 !py-1.5 !px-3 text-xs font-bold rounded-xl flex items-center gap-1" aria-label="คัดลอก prompt">' +
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>' +
      'คัดลอก' +
      '</button>' +
      '</div>' +
      rccBlock +
      customizerBlock +
      '<pre class="prompt-body mb-3 p-3.5 rounded-xl font-mono text-sm leading-relaxed" style="background:#f8f9fa; border:1px solid #e9ecef; white-space:pre-wrap; word-break:break-word;">' + escapeHtml(promptText) + '</pre>' +
      tipsBlock +
      '</div>' +
      '<div class="flex flex-wrap gap-1.5 mt-2 pt-2 border-t" style="border-color:var(--line);">' + tags + '</div>' +
      '</article>'
    );
  }

  function renderCards() {
    const container = els.grid;
    if (!container) return;

    const visible = rawData.filter(matchesFilter);

    if (visible.length === 0) {
      container.innerHTML =
        '<div class="p-8 text-center col-span-full rounded-2xl bg-white border border-slate-200 shadow-sm">' +
        '<p class="font-display font-bold text-lg mb-1 text-slate-700">ไม่พบ Prompt ที่ตรงกับเงื่อนไข</p>' +
        '<p class="text-xs text-slate-500">ลองพิมพ์คำค้นอื่น เช่น "แผน", "ข้อสอบ", "SDQ", "ว.PA" หรือกดปุ่ม "แสดงทั้งหมด"</p>' +
        "</div>";
      if (els.count) els.count.textContent = "0 / " + rawData.length + " รายการ";
      return;
    }

    const limit = state.pageSize * state.currentPage;
    const pagedItems = visible.slice(0, limit);

    let html = "";
    if (state.viewMode === "list") {
      container.className = "space-y-2.5";
      html = pagedItems.map(buildListRowHTML).join("");
    } else {
      container.className = "grid sm:grid-cols-1 md:grid-cols-2 gap-4";
      html = pagedItems.map(buildCardHTML).join("");
    }

    if (visible.length > limit) {
      html +=
        '<div class="text-center py-6 col-span-full">' +
        '<button type="button" id="btn-load-more" class="btn-ghost text-xs font-bold px-6 py-2.5 rounded-xl shadow-sm hover:bg-slate-100">' +
        'โหลดเพิ่มเติม (' + (visible.length - limit) + ' รายการที่เหลือ) ⬇️' +
        '</button>' +
        '</div>';
    }

    container.innerHTML = html;

    if (els.count) els.count.textContent = `${visible.length} / ${rawData.length} รายการ`;

    const btnLoadMore = qs("#btn-load-more");
    if (btnLoadMore) {
      btnLoadMore.addEventListener("click", () => {
        state.currentPage++;
        renderCards();
      });
    }
  }

  // 4. Detail Drawer Handlers
  function openDetailDrawer(promptId) {
    const p = promptMap.get(promptId);
    if (!p) return;

    state.activePromptId = promptId;

    const drawerBackdrop = qs("#prompt-drawer-backdrop");
    const drawerTitle = qs("#drawer-title");
    const drawerBadges = qs("#drawer-badges");
    const drawerRcc = qs("#drawer-rcc");
    const drawerSlotsContainer = qs("#drawer-slots-container");
    const drawerSlotsInputs = qs("#drawer-slots-inputs");
    const drawerPromptText = qs("#drawer-prompt-text");
    const drawerTips = qs("#drawer-tips");

    // Title & Badges
    drawerTitle.textContent = p.title;
    const isTop10 = p.curated_top10;
    const subj = (p.category && p.category.subject) || "ทั่วไป";
    const task = (p.category && p.category.task_type) || "";
    const tools = (p.tools || []).join(", ");

    drawerBadges.innerHTML = `
      ${isTop10 ? '<span class="px-2 py-0.5 rounded text-xs font-bold text-white uppercase" style="background:var(--accent)">⭐ Top 10</span>' : ''}
      <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-slate-200 text-slate-800">${escapeHtml(subj)}</span>
      ${task ? `<span class="px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-100 text-indigo-800">${escapeHtml(task)}</span>` : ''}
      <span class="px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800">🤖 ${escapeHtml(tools)}</span>
    `;

    // RCC
    if (p.role_context_condition) {
      const rcc = p.role_context_condition;
      drawerRcc.innerHTML = `
        <div><strong class="text-[#E8877A]">บทบาท (Role):</strong> ${escapeHtml(rcc.role || "-")}</div>
        <div><strong class="text-[#E8877A]">บริบท (Context):</strong> ${escapeHtml(rcc.context || "-")}</div>
        <div><strong class="text-[#E8877A]">เงื่อนไข (Condition):</strong> ${escapeHtml(rcc.condition || "-")}</div>
      `;
      drawerRcc.classList.remove("hidden");
    } else {
      drawerRcc.classList.add("hidden");
    }

    // Slots & Variable Inputs
    const slots = extractSlots(p.prompt_template);
    if (slots.length > 0) {
      drawerSlotsInputs.innerHTML = slots.map((s) => `
        <div class="flex flex-col sm:flex-row sm:items-center gap-1.5 text-sm">
          <label class="sm:w-1/3 text-xs font-bold text-slate-600 truncate" title="${escapeHtml(s)}">[${escapeHtml(s)}]:</label>
          <input type="text" class="drawer-slot-input flex-1 px-3 py-1.5 rounded-lg border border-slate-200 text-sm focus:ring-1 focus:ring-[#E8877A] outline-none" data-slot="${escapeHtml(s)}" placeholder="พิมพ์ค่าตัวแปรของคุณ...">
        </div>
      `).join("");
      drawerSlotsContainer.classList.remove("hidden");
    } else {
      drawerSlotsContainer.classList.add("hidden");
    }

    // Full Prompt
    drawerPromptText.textContent = p.prompt_template;

    // Tips
    if (p.tips) {
      drawerTips.innerHTML = `💡 <strong>คำแนะนำตรวจทาน:</strong> ${escapeHtml(p.tips)}`;
      drawerTips.classList.remove("hidden");
    } else {
      drawerTips.classList.add("hidden");
    }

    // Show Drawer
    drawerBackdrop.classList.add("active");
    drawerBackdrop.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function closeDetailDrawer() {
    const drawerBackdrop = qs("#prompt-drawer-backdrop");
    if (drawerBackdrop) {
      drawerBackdrop.classList.remove("active");
      drawerBackdrop.setAttribute("aria-hidden", "true");
    }
    document.body.style.overflow = "";
  }

  function setupEventDelegation() {
    const container = els.grid;
    if (!container) return;

    // List & Card Clicks
    container.addEventListener("click", (e) => {
      // 1. Raw Copy Button
      const copyBtn = e.target.closest(".copy-btn");
      if (copyBtn) {
        e.stopPropagation();
        const item = copyBtn.closest("[data-id]");
        const prompt = promptMap.get(item?.dataset?.id);
        if (prompt) copyText(prompt.prompt_template, "คัดลอก Prompt ต้นฉบับสำเร็จ!");
        return;
      }

      // 2. Open Detail Drawer Button or Row Click
      const rowItem = e.target.closest(".prompt-row-item");
      if (rowItem) {
        openDetailDrawer(rowItem.dataset.id);
        return;
      }

      // 3. Card Slot Customized Copy Button
      const customCopyBtn = e.target.closest(".btn-copy-customized");
      if (customCopyBtn) {
        const card = customCopyBtn.closest(".prompt-card");
        const prompt = promptMap.get(card?.dataset?.id);
        if (prompt) {
          const pre = card.querySelector(".prompt-body");
          const inputs = card.querySelectorAll(".slot-input");
          let text = prompt.prompt_template;
          inputs.forEach((inp) => {
            const val = inp.value.trim();
            const slot = inp.dataset.slot;
            if (val) text = text.split("[" + slot + "]").join(val);
          });
          if (pre) pre.textContent = text;
          copyText(text, "✨ คัดลอก Prompt แบบปรับแต่งแล้วสำเร็จ!");
        }
        return;
      }

      // 4. Reset Button
      const resetBtn = e.target.closest(".btn-reset-slots");
      if (resetBtn) {
        const card = resetBtn.closest(".prompt-card");
        const prompt = promptMap.get(card?.dataset?.id);
        if (prompt) {
          const inputs = card.querySelectorAll(".slot-input");
          const pre = card.querySelector(".prompt-body");
          inputs.forEach((inp) => { inp.value = ""; });
          if (pre) pre.textContent = prompt.prompt_template;
          showToast("ล้างค่าตัวแปรเรียบร้อย");
        }
        return;
      }
    });

    // Drawer Event Listeners
    const btnCloseDrawer = qs("#btn-close-drawer");
    const drawerBackdrop = qs("#prompt-drawer-backdrop");
    if (btnCloseDrawer) btnCloseDrawer.addEventListener("click", closeDetailDrawer);
    if (drawerBackdrop) {
      drawerBackdrop.addEventListener("click", (e) => {
        if (e.target === drawerBackdrop) closeDetailDrawer();
      });
    }

    // Drawer Keyboard Esc
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && drawerBackdrop?.classList?.contains("active")) {
        closeDetailDrawer();
      }
    });

    // Drawer Slot Live Update
    const drawerSlotsInputs = qs("#drawer-slots-inputs");
    if (drawerSlotsInputs) {
      drawerSlotsInputs.addEventListener("input", () => {
        const p = promptMap.get(state.activePromptId);
        if (!p) return;
        const pre = qs("#drawer-prompt-text");
        const inputs = qsa(".drawer-slot-input");
        let text = p.prompt_template;
        inputs.forEach((inp) => {
          const val = inp.value.trim();
          const slot = inp.dataset.slot;
          if (val) text = text.split("[" + slot + "]").join(val);
        });
        if (pre) pre.textContent = text;
      });
    }

    // Drawer Reset Slots
    const btnDrawerReset = qs("#btn-drawer-reset-slots");
    if (btnDrawerReset) {
      btnDrawerReset.addEventListener("click", () => {
        const p = promptMap.get(state.activePromptId);
        if (!p) return;
        const pre = qs("#drawer-prompt-text");
        qsa(".drawer-slot-input").forEach((inp) => { inp.value = ""; });
        if (pre) pre.textContent = p.prompt_template;
        showToast("ล้างค่าตัวแปรเรียบร้อย");
      });
    }

    // Drawer Copy Raw
    const btnDrawerCopyRaw = qs("#btn-drawer-copy-raw");
    if (btnDrawerCopyRaw) {
      btnDrawerCopyRaw.addEventListener("click", () => {
        const p = promptMap.get(state.activePromptId);
        if (p) copyText(p.prompt_template, "คัดลอก Prompt ต้นฉบับสำเร็จ!");
      });
    }

    // Drawer Copy Customized
    const btnDrawerCopyCustomized = qs("#btn-drawer-copy-customized");
    if (btnDrawerCopyCustomized) {
      btnDrawerCopyCustomized.addEventListener("click", () => {
        const pre = qs("#drawer-prompt-text");
        if (pre) copyText(pre.textContent, "✨ คัดลอก Prompt แบบปรับแต่งแล้วสำเร็จ!");
      });
    }
  }

  function update() {
    state.currentPage = 1;
    renderCards();
  }

  function onSearchInput(e) {
    clearTimeout(debounceTimer);
    const val = e.target.value;
    debounceTimer = setTimeout(() => {
      state.q = val;
      update();
    }, 120);
  }

  function bindFilterGroup(attr, container) {
    const buttons = qsa("[data-" + attr + "]", container);
    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        state[attr] = btn.dataset[attr];
        buttons.forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        update();
      });
    });
  }

  function setupTop10Buttons() {
    const btnTop10 = qs("#btn-show-top10");
    const btnAll = qs("#btn-show-all");
    if (!btnTop10 || !btnAll) return;

    btnTop10.addEventListener("click", () => {
      state.onlyTop10 = true;
      btnTop10.classList.add("active");
      btnAll.classList.remove("active");
      update();
    });

    btnAll.addEventListener("click", () => {
      state.onlyTop10 = false;
      btnAll.classList.add("active");
      btnTop10.classList.remove("active");
      update();
    });
  }

  function setupViewModeSwitcher() {
    const btnList = qs("#btn-view-list");
    const btnGrid = qs("#btn-view-grid");
    if (!btnList || !btnGrid) return;

    btnList.addEventListener("click", () => {
      state.viewMode = "list";
      btnList.classList.add("active");
      btnGrid.classList.remove("active");
      renderCards();
    });

    btnGrid.addEventListener("click", () => {
      state.viewMode = "grid";
      btnGrid.classList.add("active");
      btnList.classList.remove("active");
      renderCards();
    });
  }

  function setupStarterKitsToggle() {
    const btnToggle = qs("#btn-toggle-starter-kits");
    const btnClose = qs("#btn-close-starter-kits");
    const panel = qs("#starter-kits-panel");
    if (!btnToggle || !panel) return;

    btnToggle.addEventListener("click", () => {
      panel.classList.toggle("hidden");
      if (!panel.classList.contains("hidden")) {
        panel.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });

    if (btnClose) {
      btnClose.addEventListener("click", () => {
        panel.classList.add("hidden");
      });
    }
  }

  async function init() {
    els.grid = qs("#prompt-grid");
    els.count = qs("#prompt-count");
    if (!els.grid) return false;

    setupEventDelegation();
    setupViewModeSwitcher();
    setupStarterKitsToggle();

    const searchInput = qs("#prompt-search");
    if (searchInput) {
      searchInput.addEventListener("input", onSearchInput);
      searchInput.addEventListener("search", (e) => { state.q = e.target.value; update(); });
    }

    const taskGrp = qs("[data-filter='task']");
    const subjGrp = qs("[data-filter='subject']");
    const toolGrp = qs("[data-filter='tool']");
    if (taskGrp) bindFilterGroup("task", taskGrp);
    if (subjGrp) bindFilterGroup("subject", subjGrp);
    if (toolGrp) bindFilterGroup("tool", toolGrp);

    setupTop10Buttons();

    try {
      const res = await fetch("prompts-data.json", { cache: "no-store" });
      if (!res.ok) throw new Error("HTTP " + res.status);
      const json = await res.json();
      rawData = Array.isArray(json) ? json : (json.prompts || []);
      
      promptMap.clear();
      rawData.forEach((p) => promptMap.set(p.id, p));

      renderCards();
    } catch (err) {
      console.error("Failed to load prompts-data.json:", err);
      els.grid.innerHTML =
        '<div class="p-8 text-center col-span-full rounded-2xl bg-white border border-slate-200">' +
        '<p class="font-display font-semibold text-lg mb-1 text-red-600">โหลดข้อมูล prompt ไม่สำเร็จ</p>' +
        '<p class="text-xs text-slate-500">โปรดเปิดผ่านเว็บเซิร์ฟเวอร์ เช่น <code>python3 -m http.server 8085</code></p>' +
        "</div>";
    }
    return true;
  }

  return { init, update };
})();

/* ------------------------------------------------------------------------
   4. PRESET SCENARIO STARTER KITS LOADER
   ------------------------------------------------------------------------ */

const StarterKitsModule = (() => {
  async function init() {
    const container = document.getElementById("starter-kits-container");
    if (!container) return;

    try {
      const res = await fetch("assets/data/scenario-kits.json", { cache: "no-store" });
      if (!res.ok) return;
      const kits = await res.json();

      container.innerHTML = kits.map((k) => {
        return `
          <div class="card p-4 flex flex-col justify-between rounded-xl bg-white border border-stone-200 shadow-sm hover:shadow-md transition">
            <div>
              <div class="flex items-center justify-between gap-2 mb-1.5">
                <span class="px-2 py-0.5 rounded text-[11px] font-bold uppercase tracking-wider" style="background:rgba(95,169,158,0.15); color:#2E7D73;">${k.subject}</span>
                <span class="text-[11px] text-stone-500 font-semibold">${k.grade}</span>
              </div>
              <h3 class="font-display font-bold text-base mb-1 leading-snug" style="color:var(--ink);">${k.topic}</h3>
              <p class="text-xs text-stone-600 mb-3 line-clamp-2">${k.scenario_title}</p>
            </div>
            <div class="space-y-1.5 pt-2.5 border-t border-stone-100">
              <button type="button" class="btn-copy-starter w-full py-2 px-3 rounded-lg text-xs font-bold flex items-center justify-center gap-1.5 text-white transition hover:opacity-95 shadow-sm" style="background:#5FA99E;" data-text="${encodeURIComponent(k.prompt_gemini)}">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
                คัดลอก Prompt ครู (Gemini)
              </button>
              <button type="button" class="btn-copy-starter w-full py-1.5 px-3 rounded-lg text-xs font-semibold flex items-center justify-center gap-1.5 text-stone-700 bg-stone-100 hover:bg-stone-200 transition" data-text="${encodeURIComponent(k.notebooklm_study_guide_text)}">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                คัดลอกข้อความบทเรียน (NotebookLM)
              </button>
            </div>
          </div>
        `;
      }).join("");

      container.addEventListener("click", (e) => {
        const btn = e.target.closest(".btn-copy-starter");
        if (btn && btn.dataset.text) {
          const raw = decodeURIComponent(btn.dataset.text);
          copyText(raw, "คัดลอกชุดข้อมูลสำหรับใช้งานแล้ว!");
        }
      });
    } catch (err) {
      console.warn("Could not load scenario-kits.json", err);
    }
  }

  return { init };
})();

// ======= Visual Infographics Read-only Viewer & Modal =======
window.switchDiagram = function(index) {
  for (let i = 0; i < 3; i++) {
    const panel = document.getElementById('diagram-panel-' + i);
    const tab = document.getElementById('diagram-tab-' + i);
    if (panel && tab) {
      if (i === index) {
        panel.classList.remove('hidden');
        panel.classList.add('block');
        tab.className = 'diagram-tab-btn px-3 py-1.5 rounded-lg text-xs font-display font-bold transition-all bg-white text-[#26394A] shadow-xs';
      } else {
        panel.classList.add('hidden');
        panel.classList.remove('block');
        tab.className = 'diagram-tab-btn px-3 py-1.5 rounded-lg text-xs font-display font-bold transition-all text-slate-600 hover:text-[#26394A]';
      }
    }
  }
};

window.openDiagramModal = function(imgSrc, title) {
  const modal = document.getElementById('diagramModal');
  const modalImg = document.getElementById('diagramModalImg');
  const modalTitle = document.getElementById('diagramModalTitle');
  const modalDl = document.getElementById('diagramModalDownload');
  if (modal && modalImg && modalTitle) {
    modalImg.src = imgSrc;
    modalTitle.textContent = title;
    if (modalDl) modalDl.href = imgSrc;
    modal.classList.remove('hidden');
    setTimeout(() => {
      modal.classList.remove('opacity-0');
    }, 10);
  }
};

window.closeDiagramModal = function() {
  const modal = document.getElementById('diagramModal');
  if (modal) {
    modal.classList.add('opacity-0');
    setTimeout(() => {
      modal.classList.add('hidden');
    }, 200);
  }
};

document.addEventListener("DOMContentLoaded", () => {
  initActiveNav();
  PromptsLibrary.init();
  StarterKitsModule.init();

  const modal = document.getElementById('diagramModal');
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeDiagramModal();
      }
    });
  }
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeDiagramModal();
    }
  });
});

