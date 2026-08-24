/* ==========================================================================
   AI Training School — site/assets/js/app.js
   High-Performance, Optimized & Modular Vanilla JS
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
   3. HIGH-PERFORMANCE PROMPTS LIBRARY (Virtual Pagination + Event Delegation)
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
    pageSize: 30, // Show initial 30 for instant 60fps render
    currentPage: 1
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
        '<div class="my-3 p-3.5 rounded text-sm space-y-1.5" style="background:var(--paper-2); border:1px solid var(--line);">' +
        '<div><strong style="color:var(--accent)">บทบาท:</strong> ' + escapeHtml(rcc.role || "-") + '</div>' +
        '<div><strong style="color:var(--accent)">บริบท:</strong> ' + escapeHtml(rcc.context || "-") + '</div>' +
        '<div><strong style="color:var(--accent)">เงื่อนไข:</strong> ' + escapeHtml(rcc.condition || "-") + '</div>' +
        '</div>';
    }

    let tipsBlock = "";
    if (p.tips) {
      tipsBlock = '<div class="text-sm mb-3 italic" style="color:var(--ink-soft)">💡 <strong>คำแนะนำตรวจทาน:</strong> ' + escapeHtml(p.tips) + '</div>';
    }

    // Lazy Render Slot Customizer Accordion
    let customizerBlock = "";
    if (slots.length > 0) {
      const inputsHtml = slots.map((s) => {
        return (
          '<div class="flex flex-col sm:flex-row sm:items-center gap-1 sm:gap-2 text-sm">' +
          '<label class="sm:w-1/3 text-xs font-bold text-ink-soft truncate" title="' + escapeHtml(s) + '">[' + escapeHtml(s) + ']:</label>' +
          '<input type="text" class="slot-input flex-1 px-2.5 py-1.5 rounded border text-sm font-sans" data-slot="' + escapeHtml(s) + '" placeholder="พิมพ์ข้อมูลของคุณ..." style="border-color:var(--line); background:#ffffff;">' +
          '</div>'
        );
      }).join("");

      customizerBlock = (
        '<details class="slot-customizer my-3 p-3 rounded border text-sm" style="background:var(--paper); border-color:var(--line);">' +
        '<summary class="font-display font-bold text-xs cursor-pointer flex items-center justify-between text-accent hover:opacity-80 select-none">' +
        '<span>⚙️ ปรับแต่งตัวแปรก่อนคัดลอก (' + slots.length + ' ช่อง)</span>' +
        '<span class="text-xs font-normal" style="color:var(--ink-soft)">คลิกเพื่อกรอกค่า</span>' +
        '</summary>' +
        '<div class="mt-3 pt-2 border-t space-y-2" style="border-color:var(--line);">' +
        inputsHtml +
        '<div class="pt-2 flex justify-end gap-2">' +
        '<button type="button" class="btn-reset-slots text-xs px-2.5 py-1 rounded border hover:bg-gray-100" style="border-color:var(--line); color:var(--ink-soft)">ล้างค่า</button>' +
        '<button type="button" class="btn-copy-customized btn-accent text-xs font-bold px-3 py-1 rounded flex items-center gap-1 shadow-sm">✨ คัดลอกแบบปรับแต่งแล้ว</button>' +
        '</div>' +
        '</div>' +
        '</details>'
      );
    }

    return (
      '<article class="prompt-card flex flex-col justify-between p-5 rounded-lg border bg-white shadow-sm" data-id="' + escapeHtml(p.id) + '" style="border-color:var(--line); content-visibility:auto; contain-intrinsic-size:350px;">' +
      '<div>' +
      '<div class="flex items-start justify-between gap-3 mb-2">' +
      '<div class="min-w-0">' +
      (top10Badge ? '<div class="mb-1.5">' + top10Badge + '</div>' : '') +
      '<h3 class="font-display font-bold text-lg sm:text-xl leading-snug mb-2">' + escapeHtml(p.title) + "</h3>" +
      '<div class="flex flex-wrap gap-1.5 mb-1">' + tools + task + subj + '</div>' +
      "</div>" +
      '<button type="button" class="copy-btn btn-accent shrink-0 !py-2 !px-3.5 text-sm font-semibold rounded-md flex items-center gap-1" aria-label="คัดลอก prompt">' +
      '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">' +
      '<rect x="9" y="9" width="11" height="11" rx="2" stroke="currentColor" stroke-width="1.8"/><path d="M5 15H4.5A1.5 1.5 0 0 1 3 13.5v-9A1.5 1.5 0 0 1 4.5 3h9A1.5 1.5 0 0 1 15 4.5V5" stroke="currentColor" stroke-width="1.8"/>' +
      '</svg>' +
      'คัดลอก' +
      '</button>' +
      '</div>' +
      rccBlock +
      customizerBlock +
      '<pre class="prompt-body mb-3 p-3 rounded font-mono text-sm leading-relaxed" style="background:#f8f9fa; border:1px solid #e9ecef; white-space:pre-wrap; word-break:break-word;">' + escapeHtml(promptText) + '</pre>' +
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
        '<div class="panel-2 px-5 py-10 text-center col-span-full rounded-lg" style="background:var(--paper-2); border:1px solid var(--line);">' +
        '<p class="font-display font-semibold text-xl mb-1">ไม่พบ Prompt ที่ตรงกับเงื่อนไข</p>' +
        '<p class="text-base" style="color:var(--ink-soft)">ลองพิมพ์คำค้นอื่น เช่น "แผน", "ข้อสอบ", "SDQ", "ว.PA" หรือกดปุ่ม "แสดงทั้งหมด"</p>' +
        "</div>";
      if (els.count) els.count.textContent = "0 / " + rawData.length + " รายการ";
      return;
    }

    const limit = state.pageSize * state.currentPage;
    const pagedItems = visible.slice(0, limit);

    let html = pagedItems.map(buildCardHTML).join("");

    if (visible.length > limit) {
      html +=
        '<div class="col-span-full text-center py-6">' +
        '<button type="button" id="btn-load-more" class="btn-ink px-6 py-2.5 rounded-lg text-sm font-display font-bold shadow hover:opacity-90">' +
        'โหลดเพิ่มเติม (' + (visible.length - limit) + ' รายการที่เหลือ) ⬇️' +
        '</button>' +
        '</div>';
    }

    container.innerHTML = html;

    if (els.count) els.count.textContent = visible.length + " / " + rawData.length + " รายการ";

    const btnLoadMore = qs("#btn-load-more");
    if (btnLoadMore) {
      btnLoadMore.addEventListener("click", () => {
        state.currentPage++;
        renderCards();
      });
    }
  }

  function setupEventDelegation() {
    const container = els.grid;
    if (!container) return;

    // Single Global Event Listener for Input, Click, Reset
    container.addEventListener("click", (e) => {
      // 1. Raw Copy Button
      const copyBtn = e.target.closest(".copy-btn");
      if (copyBtn) {
        const card = copyBtn.closest(".prompt-card");
        const prompt = promptMap.get(card?.dataset?.id);
        if (prompt) copyText(prompt.prompt_template, "คัดลอก Prompt ต้นฉบับสำเร็จ!");
        return;
      }

      // 2. Customized Copy Button
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

      // 3. Reset Button
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

    // Reactive Slot Input Listener
    container.addEventListener("input", (e) => {
      if (e.target.classList.contains("slot-input")) {
        const card = e.target.closest(".prompt-card");
        const prompt = promptMap.get(card?.dataset?.id);
        if (!prompt) return;

        const pre = card.querySelector(".prompt-body");
        const inputs = card.querySelectorAll(".slot-input");
        let text = prompt.prompt_template;
        inputs.forEach((inp) => {
          const val = inp.value.trim();
          const slot = inp.dataset.slot;
          if (val) text = text.split("[" + slot + "]").join(val);
        });
        if (pre) pre.textContent = text;
      }
    });
  }

  function update() {
    state.currentPage = 1;
    renderCards();
  }

  function onSearchInput(e) {
    clearTimeout(debounceTimer);
    const val = e.target.value;
    // Fast 120ms debounce to keep typing at 60 FPS
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

  async function init() {
    els.grid = qs("#prompt-grid");
    els.count = qs("#prompt-count");
    if (!els.grid) return false;

    setupEventDelegation();

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
        '<div class="panel-2 px-5 py-10 text-center col-span-full rounded-lg" style="background:var(--paper-2); border:1px solid var(--line);">' +
        '<p class="font-display font-semibold text-xl mb-1">โหลดข้อมูล prompt ไม่สำเร็จ</p>' +
        '<p class="text-base" style="color:var(--ink-soft)">หากเปิดผ่านไฟล์ตรง (file://) โปรดเปิดผ่านเว็บเซิร์ฟเวอร์ เช่น รันคำสั่ง <code>python3 -m http.server 8085</code> ในโฟลเดอร์ <code>site/</code> แล้วเข้าผ่าน <code>http://localhost:8085/prompts.html</code></p>' +
        "</div>";
    }
    return true;
  }

  return { init, update };
})();

document.addEventListener("DOMContentLoaded", () => {
  initActiveNav();
  PromptsLibrary.init();
});
