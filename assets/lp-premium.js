(() => {
  const doc = document.documentElement;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const progress = document.createElement('div');
  progress.className = 'lp-progress';
  progress.setAttribute('aria-hidden', 'true');
  document.body.appendChild(progress);

  const startProgress = () => {
    progress.classList.remove('is-done');
    void progress.offsetWidth;
    progress.classList.add('is-active');
  };
  const endProgress = () => {
    if (!progress.classList.contains('is-active')) return;
    progress.classList.remove('is-active');
    progress.classList.add('is-done');
  };

  document.addEventListener('click', (event) => {
    if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const link = event.target.closest('a[href]');
    if (!link || link.target === '_blank' || link.hasAttribute('download')) return;
    const url = new URL(link.href, location.href);
    if (url.origin !== location.origin) return;
    if (url.pathname === location.pathname && url.search === location.search) return;
    if (link.getAttribute('href').startsWith('#') || link.matches('[aria-controls], [data-no-progress]')) return;
    startProgress();
  });

  document.addEventListener('submit', (event) => {
    const form = event.target;
    if (event.defaultPrevented || form.matches('[is], [data-no-progress]') || form.closest('product-form, cart-drawer, cart-notification-drawer')) return;
    startProgress();
  });

  window.addEventListener('pageshow', endProgress);
  window.addEventListener('pagehide', () => setTimeout(endProgress, 10000));

  document.addEventListener('cart:change', () => {
    document.querySelectorAll('.count-bubble').forEach((bubble) => {
      bubble.classList.remove('lp-bump');
      void bubble.offsetWidth;
      bubble.classList.add('lp-bump');
    });
  });

  document.addEventListener('variant:add', (event) => {
    const button = event.target.querySelector?.('button[type="submit"]') || document.querySelector('.product-info__buy-buttons button[type="submit"]');
    if (!button) return;
    button.classList.remove('lp-atc-success');
    void button.offsetWidth;
    button.classList.add('lp-atc-success');
  });

  ['facet:update', 'cart:refresh'].forEach((name) => {
    document.addEventListener(name, () => {
      startProgress();
      setTimeout(endProgress, 700);
    });
  });

  let ticking = false;
  const onScroll = () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      doc.classList.toggle('lp-scrolled', window.scrollY > 8);
      ticking = false;
    });
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  const prepImage = (img) => {
    if (img.dataset.lpImg || img.complete || img.fetchPriority === "high") return;
    img.dataset.lpImg = '1';
    img.classList.add('lp-img-loading');
    const done = () => {
      img.classList.remove('lp-img-loading');
      if (!reduceMotion) img.classList.add('lp-img-loaded');
    };
    img.addEventListener('load', done, { once: true });
    img.addEventListener('error', done, { once: true });
  };
  const imageSelector = '.product-card__figure img, .lp-media img, .collection-card img, .blog-post-card img';
  document.querySelectorAll(imageSelector).forEach(prepImage);

  const revealObserver = 'IntersectionObserver' in window && !reduceMotion
    ? new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-in');
          revealObserver.unobserve(entry.target);
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 })
    : null;

  const formatter = new Intl.NumberFormat(doc.lang || 'en-GB');
  const countObserver = 'IntersectionObserver' in window
    ? new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          countObserver.unobserve(el);
          const target = parseFloat(el.dataset.lpCount);
          const decimals = (el.dataset.lpCount.split('.')[1] || '').length;
          if (reduceMotion || Number.isNaN(target)) return;
          const start = performance.now();
          const duration = 1600;
          const tick = (now) => {
            const t = Math.min(1, (now - start) / duration);
            const eased = 1 - Math.pow(1 - t, 4);
            el.textContent = decimals ? (target * eased).toFixed(decimals) : formatter.format(Math.round(target * eased));
            if (t < 1) requestAnimationFrame(tick);
          };
          requestAnimationFrame(tick);
        });
      }, { threshold: 0.6 })
    : null;

  const hydrate = (root = document) => {
    root.querySelectorAll('[data-lp-reveal]').forEach((el) => {
      if (revealObserver) revealObserver.observe(el);
      else el.classList.add('is-in');
    });
    root.querySelectorAll('[data-lp-count]').forEach((el) => countObserver && countObserver.observe(el));
    root.querySelectorAll(imageSelector).forEach(prepImage);
  };
  hydrate();

  document.addEventListener('shopify:section:load', (event) => hydrate(event.target));

  const pending = new Set();
  let scheduled = false;
  const flush = () => {
    scheduled = false;
    pending.forEach((node) => node.isConnected && hydrate(node));
    pending.clear();
  };
  const main = document.getElementById('main') || document.querySelector('main');
  if (main) {
    new MutationObserver((mutations) => {
      for (const m of mutations) {
        for (const node of m.addedNodes) {
          if (node.nodeType === 1 && (node.matches('img, [data-lp-reveal], [data-lp-count]') || node.querySelector('img, [data-lp-reveal], [data-lp-count]'))) pending.add(node);
        }
      }
      if (pending.size && !scheduled) {
        scheduled = true;
        (window.requestIdleCallback || requestAnimationFrame)(flush);
      }
    }).observe(main, { childList: true, subtree: true });
  }

  const startLazyVideos = () => document.querySelectorAll('video[data-lp-lazy]').forEach((video) => {
    if (reduceMotion) return;
    const io = new IntersectionObserver(([entry]) => {
      if (!entry.isIntersecting) return;
      video.querySelectorAll('source[data-src]').forEach((s) => { s.src = s.dataset.src; });
      video.addEventListener('playing', () => video.classList.add('is-playing'), { once: true });
      video.load();
      video.play().catch(() => {});
      io.disconnect();
    }, { rootMargin: '200px' });
    io.observe(video);
  });


  const syncPrice = () => document.querySelectorAll('.lp-pdp-price').forEach((box) => {
    const now = box.querySelector('.lp-pdp-price__now');
    const was = box.querySelector('.lp-pdp-price__was');
    const tag = box.querySelector('.lp-pdp-price__tag');
    if (!now || !was) return;
    // A variant change swaps in a server-rendered button with the one-time price; let Skio write its plan price again.
    if (box.classList.contains('lp-pdp-price--atc') && !box.dataset.lpSkio) {
      box.dataset.lpSkio = '1';
      const picker = document.querySelector('.shopify-section--main-product skio-plan-picker');
      if (picker && typeof picker.updateExternalPrice === 'function' && picker.selectedVariant) picker.updateExternalPrice();
    }
    const toNum = (t) => parseFloat((t || '').replace(/[^0-9.,]/g, '').replace(/,(?=\d{3}\b)/g, '').replace(',', '.')) || 0;
    const a = toNum(now.textContent), b = toNum(was.dataset.base || was.textContent);
    const discounted = a > 0 && b > a + 0.001;
    was.hidden = !discounted;
    if (tag) { tag.hidden = !discounted; if (discounted) tag.textContent = 'Save ' + Math.round((1 - a / b) * 100) + '%'; }
    const sticky = document.querySelector('[data-lp-sticky-price]');
    if (sticky && a > 0 && sticky.textContent.trim() !== now.textContent.trim()) sticky.textContent = now.textContent.trim();
    const unit = document.querySelector('[data-lp-sticky-unit]');
    if (unit && a > 0) {
      const count = Number(unit.dataset.count) || 0;
      const symbol = (now.textContent.trim().match(/^[^0-9]*/) || [''])[0];
      const text = count ? ` ${symbol}${(a / count).toFixed(2)} / ${unit.dataset.unit}` : '';
      if (unit.textContent !== text) unit.textContent = text;
    }
  });
  const priceRoot = document.querySelector('.shopify-section--main-product');
  if (priceRoot) {
    let raf = 0;
    new MutationObserver(() => { cancelAnimationFrame(raf); raf = requestAnimationFrame(syncPrice); }).observe(priceRoot, { childList: true, subtree: true, characterData: true });
    syncPrice();
  }
  const watchUgc = () => document.querySelectorAll('tolstoy-stories').forEach((stories) => {
    const item = stories.closest('.product-info__block-item');
    const head = item && item.previousElementSibling && item.previousElementSibling.querySelector('.lp-pdp-subhead');
    const ready = () => stories.childElementCount > 0 || (stories.shadowRoot && stories.shadowRoot.childElementCount > 0);
    const reveal = () => { stories.classList.add('lp-ready'); if (head) head.classList.add('is-ready'); };
    if (ready()) return reveal();
    const mo = new MutationObserver(() => { if (ready()) { reveal(); mo.disconnect(); } });
    mo.observe(stories, { childList: true, subtree: true });
  });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', watchUgc, { once: true });
  else watchUgc();

  const tidyDashes = () => document.querySelectorAll('.metafield-rich_text_field, .metafield-multi_line_text_field').forEach((root) => {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) {
      if (node.nodeValue.includes('\u2014')) node.nodeValue = node.nodeValue.replace(/\s*\u2014\s*/g, ', ');
    }
  });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', tidyDashes, { once: true });
  else tidyDashes();



  const initMobileMenu = () => {
    const menu = document.querySelector('[data-lp-menu]');
    const toggle = document.querySelector('[data-lp-menu-toggle]');
    if (!menu || !toggle) return;
    const root = menu.querySelector('[data-lp-menu-panel="root"]');
    const desktop = window.matchMedia('(min-width: 1000px)');
    const duration = reduceMotion ? 0 : 420;
    let active = null;
    let lastFocus = null;
    let viaKeyboard = false;
    document.addEventListener('keydown', () => { viaKeyboard = true; }, true);
    document.addEventListener('pointerdown', () => { viaKeyboard = false; }, true);
    const moveFocus = (el) => { if (el && viaKeyboard) el.focus({ preventScroll: true }); };

    const headerBottom = () => {
      const header = toggle.closest('.shopify-section--header, header, store-header') || toggle;
      return Math.max(0, Math.round(header.getBoundingClientRect().bottom));
    };
    const focusables = () => {
      const panel = active || root;
      return [toggle, ...panel.querySelectorAll('a[href], button:not([disabled])')].filter((el) => el.offsetParent !== null || el === toggle);
    };

    const showRoot = () => {
      menu.classList.remove('is-sub');
      root.inert = false;
      const previous = active;
      active = null;
      if (previous) {
        previous.classList.remove('is-active');
        setTimeout(() => { if (active !== previous) { previous.hidden = true; previous.inert = true; } }, duration);
        moveFocus(root.querySelector(`[data-lp-menu-open="${previous.dataset.lpMenuPanel}"]`));
      }
    };
    const showPanel = (key) => {
      const panel = menu.querySelector(`[data-lp-menu-panel="${key}"]`);
      if (!panel) return;
      panel.hidden = false;
      panel.inert = false;
      panel.scrollTop = 0;
      requestAnimationFrame(() => requestAnimationFrame(() => {
        panel.classList.add('is-active');
        menu.classList.add('is-sub');
        root.inert = true;
        active = panel;
        moveFocus(panel.querySelector('[data-lp-menu-back]'));
      }));
    };

    const open = () => {
      lastFocus = document.activeElement;
      menu.style.setProperty('--lp-menu-top', `${headerBottom()}px`);
      menu.hidden = false;
      toggle.setAttribute('aria-expanded', 'true');
      document.documentElement.classList.add('lp-menu-open');
      requestAnimationFrame(() => requestAnimationFrame(() => menu.classList.add('is-open')));
      document.addEventListener('keydown', onKey);
    };
    const close = (restoreFocus = true) => {
      if (menu.hidden) return;
      menu.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
      document.documentElement.classList.remove('lp-menu-open');
      document.removeEventListener('keydown', onKey);
      setTimeout(() => {
        if (toggle.getAttribute('aria-expanded') === 'true') return;
        menu.hidden = true;
        menu.classList.remove('is-sub');
        menu.querySelectorAll('.lp-menu__panel--sub').forEach((p) => { p.hidden = true; p.classList.remove('is-active'); });
        root.inert = false;
        active = null;
      }, reduceMotion ? 0 : 360);
      if (restoreFocus && lastFocus && lastFocus.focus) lastFocus.focus({ preventScroll: true });
    };
    const onKey = (event) => {
      if (event.key === 'Escape') {
        if (active) showRoot(); else close();
        return;
      }
      if (event.key !== 'Tab') return;
      const items = focusables();
      if (!items.length) return;
      const first = items[0];
      const last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
      else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
      else if (!menu.contains(document.activeElement) && document.activeElement !== toggle) { event.preventDefault(); first.focus(); }
    };

    const refItem = menu.querySelector('.lp-menu__ref');
    const refButton = () => document.querySelector('.referral-banner__name--clickable');
    const syncRef = () => {
      if (!refItem) return;
      const title = document.querySelector('.referral-banner__title');
      const btn = refButton();
      if (!btn) { refItem.hidden = true; return; }
      const referred = title && getComputedStyle(title).display !== 'none';
      refItem.hidden = false;
      refItem.querySelector('button').textContent = referred ? `Shopping with ${btn.textContent.trim()} · Change` : 'Were you referred by someone?';
    };
    toggle.addEventListener('click', (event) => {
      event.preventDefault();
      if (toggle.getAttribute('aria-expanded') === 'true') close(); else { syncRef(); open(); }
    });
    menu.addEventListener('click', (event) => {
      const opener = event.target.closest('[data-lp-menu-open]');
      if (opener) { showPanel(opener.dataset.lpMenuOpen); return; }
      if (event.target.closest('[data-lp-menu-back]')) { showRoot(); return; }
      if (event.target.closest('[data-lp-menu-ref]')) { close(false); const btn = refButton(); if (btn) setTimeout(() => btn.click(), 50); return; }
      const link = event.target.closest('a[href]');
      if (link) {
        if (link.getAttribute('aria-controls') === 'search-drawer') { close(false); return; }
        close(false);
      }
    });
    const onDesktop = () => { if (desktop.matches) close(false); };
    if (desktop.addEventListener) desktop.addEventListener('change', onDesktop);
    window.addEventListener('pageshow', () => close(false));
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initMobileMenu, { once: true });
  else initMobileMenu();


  const initProductTabs = () => document.querySelectorAll('[data-lp-tabs]').forEach((root) => {
    const tabs = [...root.querySelectorAll('[data-lp-tab]')];
    const cards = [...root.querySelectorAll('[data-collections]')];
    const grid = root.querySelector('[data-lp-tab-panel]');
    const select = (tab) => {
      const key = tab.dataset.lpTab;
      tabs.forEach((t) => t.setAttribute('aria-selected', String(t === tab)));
      // The first tab shows the main collection only; the other tabs show every card that belongs to their collection.
      cards.forEach((card) => { card.hidden = key === 'all' ? card.hasAttribute('data-lp-extra') : !card.dataset.collections.split(' ').includes(key); });
      if (grid) grid.scrollTo({ left: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
      window.requestAnimationFrame(() => syncRail());
    };
    const prev = root.querySelector('[data-lp-rail="-1"]');
    const next = root.querySelector('[data-lp-rail="1"]');
    const syncRail = () => {
      if (!grid || !prev || !next) return;
      const max = grid.scrollWidth - grid.clientWidth - 2;
      prev.disabled = grid.scrollLeft <= 2;
      next.disabled = grid.scrollLeft >= max;
    };
    [prev, next].forEach((btn) => btn && btn.addEventListener('click', () => {
      grid.scrollBy({ left: Number(btn.dataset.lpRail) * grid.clientWidth * 0.9, behavior: reduceMotion ? 'auto' : 'smooth' });
    }));
    if (grid) { grid.addEventListener('scroll', syncRail, { passive: true }); window.addEventListener('resize', syncRail); syncRail(); }
    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => { select(tab); requestAnimationFrame(syncRail); });
      tab.addEventListener('keydown', (event) => {
        if (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') return;
        const next = tabs[(index + (event.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length];
        next.focus(); select(next);
      });
    });
    root.addEventListener('click', async (event) => {
      const button = event.target.closest('[data-lp-add]');
      if (!button || button.classList.contains('is-loading')) return;
      button.classList.add('is-loading');
      button.setAttribute('aria-busy', 'true');
      try {
        const routeRoot = window.Shopify?.routes?.root || '/';
        const sections = [];
        document.documentElement.dispatchEvent(new CustomEvent('cart:prepare-bundled-sections', { bubbles: true, detail: { sections } }));
        const response = await fetch(`${routeRoot}cart/add.js`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json', 'X-Requested-With': 'XMLHttpRequest' },
          body: JSON.stringify({ items: [{ id: Number(button.dataset.lpAdd), quantity: 1 }], sections: sections.join(','), sections_url: window.location.pathname })
        });
        const added = await response.json();
        if (!response.ok) throw new Error(added.description || 'Could not add to cart');
        if (window.themeVariables?.settings?.cartType === 'page') { window.location.href = `${routeRoot}cart`; return; }
        const cart = await (await fetch(`${routeRoot}cart.js`)).json();
        cart.sections = added.sections || {};
        button.dispatchEvent(new CustomEvent('variant:add', { bubbles: true, detail: { items: added.items || [added], cart } }));
        document.documentElement.dispatchEvent(new CustomEvent('cart:change', { bubbles: true, detail: { baseEvent: 'variant:add', cart } }));
      } catch (error) {
        window.location.href = button.closest('[data-collections]').querySelector('a[href]').href;
      } finally {
        button.classList.remove('is-loading');
        button.removeAttribute('aria-busy');
      }
    });
  });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initProductTabs, { once: true });
  else initProductTabs();

  /* Referral at checkout (snippets/lp-referral-nudge.liquid). Replaces the old slide-in and floating tab.
     Pressing Checkout opens the dialog when the Teqnavi referral app is on the page and the shopper has not ticked
     "Don't show this again":
       - no referrer yet  -> "Were You Referred by Someone?" (Add My Referrer / No, Continue to Checkout)
       - referrer set     -> "Your Order Is Referred By <name>" (Continue to Checkout / Change)
     Add My Referrer / Change open the app's own enroller search. When the shopper picks someone, the dialog comes back
     in the confirmed state with the name ticked; if they close the search, it comes back as it was.
     The cart drawer shows a "Referred by <name> · Change" line whenever a referrer is set. */
  const initReferralCheckout = () => {
    const dialog = document.querySelector('[data-lp-refq]');
    if (!dialog) return;
    const NEVER = 'lp-ref-optout';
    const never = () => { try { return localStorage.getItem(NEVER) === '1'; } catch (e) { return false; } };
    const setNever = () => { try { localStorage.setItem(NEVER, '1'); } catch (e) { /* storage unavailable */ } };
    const appButton = () => document.querySelector('.referral-banner__name--clickable');
    const referrer = () => {
      const title = document.querySelector('.referral-banner__title');
      const button = appButton();
      if (!button || !title || getComputedStyle(title).display === 'none') return '';
      return button.textContent.trim();
    };
    const appModalOpen = () => [...document.querySelectorAll('.referral-banner__modal')].some((m) => {
      const cs = getComputedStyle(m);
      return cs.display !== 'none' && cs.visibility !== 'hidden' && m.getBoundingClientRect().height > 0;
    });
    const checkbox = dialog.querySelector('[data-lp-refq-never]');
    const nameEl = dialog.querySelector('[data-lp-refq-name]');
    const video = dialog.querySelector('video');
    let pending = null; // { form, submitter }
    let bypass = false;
    let watching = 0;

    const playArt = () => {
      if (!video || reduceMotion) return;
      const source = video.querySelector('source[data-src]');
      if (source) { source.src = source.dataset.src; source.removeAttribute('data-src'); video.load(); }
      try { video.currentTime = 0; } catch (e) {}
      const attempt = video.play();
      if (attempt && attempt.catch) attempt.catch(() => {});
    };
    const show = (state) => {
      const name = referrer();
      const done = state === 'done' && !!name;
      dialog.classList.toggle('is-done', done);
      if (nameEl.textContent !== name) nameEl.textContent = name;
      dialog.setAttribute('aria-labelledby', done ? '' : 'lp-refq-title');
      if (!dialog.open) { dialog.showModal(); playArt(); }
    };
    const remember = () => { if (checkbox.checked) setNever(); };
    const continueCheckout = () => {
      const form = pending && pending.form;
      const submitter = pending && pending.submitter;
      pending = null;
      // After the app's reload there is no paused submit: the cart (and its Referral attribute) is already saved, so go straight to checkout
      if (!form || !form.isConnected) { window.location.href = (window.Shopify?.routes?.root || '/') + 'checkout'; return; }
      bypass = true;
      if (form && form.requestSubmit) {
        form.requestSubmit(submitter && submitter.isConnected && submitter.form === form ? submitter : form.querySelector('[name="checkout"]') || undefined);
      } else {
        const input = Object.assign(document.createElement('input'), { type: 'hidden', name: 'checkout', value: '1' });
        form.appendChild(input); form.submit();
      }
      setTimeout(() => { bypass = false; }, 0);
    };

    /* Store the referrer's display name on the cart, so the checkout "Referred by" block can show it
       (Teqnavi only stores the webalias, as the "Referral" attribute) */
    let nameWrite = Promise.resolve();
    const writeName = (name) => {
      let last = '';
      try { last = sessionStorage.getItem('lp-ref-name') || ''; } catch (e) {}
      if (!name || name === last) return nameWrite;
      try { sessionStorage.setItem('lp-ref-name', name); } catch (e) {}
      nameWrite = fetch((window.Shopify?.routes?.root || '/') + 'cart/update.js', {
        method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ attributes: { 'Referrer Name': name } })
      }).catch(() => { try { sessionStorage.removeItem('lp-ref-name'); } catch (e) {} });
      return nameWrite;
    };

    /* Referred-by line in the cart drawer */
    const syncRow = () => {
      const row = document.querySelector('#cart-drawer [data-lp-ref-row]');
      if (!row) return;
      const name = referrer();
      if (name) writeName(name);
      // Write only on change: these nodes sit inside observed subtrees, so an unconditional write would loop
      if (row.hidden !== !name) row.hidden = !name;
      const strong = row.querySelector('[data-lp-ref-row-name]');
      if (strong && strong.textContent !== name) strong.textContent = name;
    };

    /* Open the app's enroller search, then come back to the dialog */
    // The app reloads the page (?ref=<webalias>) after a pick, so remember what to reopen
    const RESUME = 'lp-refq-resume';
    let unloading = false;
    window.addEventListener('pagehide', () => { unloading = true; });
    window.addEventListener('beforeunload', () => { unloading = true; });
    const setResume = (v) => { try { v ? sessionStorage.setItem(RESUME, JSON.stringify(v)) : sessionStorage.removeItem(RESUME); } catch (e) {} };
    const getResume = () => { try { return JSON.parse(sessionStorage.getItem(RESUME) || 'null'); } catch (e) { return null; } };
    const openApp = (backToDialog) => {
      const button = appButton();
      if (!button) return;
      const before = referrer();
      setResume({ t: Date.now(), dialog: !!backToDialog, before });
      const returnState = dialog.classList.contains('is-done') ? 'done' : 'ask';
      if (dialog.open) dialog.close();
      clearInterval(watching);
      let seenOpen = false;
      const started = Date.now();
      setTimeout(() => button.click(), 120);
      watching = setInterval(() => {
        const now = referrer();
        const open = appModalOpen();
        if (open) seenOpen = true;
        const picked = now && now !== before;
        const closed = seenOpen && !open;
        if (picked || closed || Date.now() - started > 300000) {
          clearInterval(watching);
          // The app closes its search and then reloads the page after a pick: wait a beat before treating it as "closed"
          setTimeout(() => {
            if (unloading) return;
            setResume(null);
            syncRow();
            if (backToDialog) show(referrer() ? 'done' : returnState);
          }, picked ? 200 : 1500);
        }
      }, 250);
    };

    document.addEventListener('submit', (event) => {
      if (bypass) return;
      const submitter = event.submitter;
      if (!submitter || submitter.name !== 'checkout') return;
      if (never() || !appButton()) return;
      event.preventDefault();
      pending = { form: event.target, submitter };
      checkbox.checked = false;
      show(referrer() ? 'done' : 'ask');
    }, true);

    dialog.addEventListener('click', (event) => {
      if (event.target.closest('[data-lp-refq-skip]')) { remember(); dialog.close(); continueCheckout(); return; }
      if (event.target.closest('[data-lp-refq-continue]')) {
        remember(); dialog.close();
        const name = referrer();
        Promise.race([writeName(name), new Promise((r) => setTimeout(r, 1500))]).then(continueCheckout);
        return;
      }
      if (event.target.closest('[data-lp-refq-add]') || event.target.closest('[data-lp-refq-change]')) { remember(); openApp(true); return; }
      if (event.target.closest('[data-lp-refq-close]') || event.target === dialog) { remember(); pending = null; dialog.close(); }
    });
    dialog.addEventListener('cancel', () => { remember(); pending = null; });
    document.addEventListener('click', (event) => {
      if (event.target.closest('[data-lp-ref-row-change]')) { event.preventDefault(); openApp(false); }
    });

    const drawer = document.getElementById('cart-drawer');
    let rowQueued = false;
    const queueRow = () => { if (rowQueued) return; rowQueued = true; requestAnimationFrame(() => { rowQueued = false; syncRow(); }); };
    if (drawer) new MutationObserver(queueRow).observe(drawer, { childList: true, subtree: true });
    let tries = 0;
    const waitForApp = () => {
      if (appButton()) {
        syncRow();
        const resume = getResume();
        if (resume && Date.now() - resume.t < 10 * 60 * 1000) {
          setResume(null);
          // Give the app a moment to apply the new referrer after the reload
          let n = 0;
          const settle = () => {
            if (referrer() && referrer() !== resume.before) {
              const cart = document.getElementById('cart-drawer');
              if (cart && cart.show) cart.show();
              syncRow();
              if (resume.dialog) setTimeout(() => show('done'), 450);
            } else if (++n < 20) setTimeout(settle, 250);
          };
          settle();
        }
        const banner = document.querySelector('.referral-banner');
        if (banner) new MutationObserver(queueRow).observe(banner, { subtree: true, childList: true, characterData: true, attributes: true, attributeFilter: ['style'] });
        return;
      }
      if (++tries < 40) setTimeout(waitForApp, 250);
    };
    waitForApp();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initReferralCheckout, { once: true });
  else initReferralCheckout();


  /* Sticky Add to Cart: shown whenever the page's own Add to Cart is off screen (below it on first load on mobile, or
     scrolled past it), hidden while that button, the footer, a drawer or the menu is on screen. A hidden bar is inert.
     A variant change replaces the whole bar (product-rerender), so nothing outside may hold a reference to it: the
     element itself publishes its state (html.lp-sticky-on and --lp-sticky-h, used to lift the chat bubble), and a
     replacement that arrives while the bar is showing appears at once instead of fading out and in again. */
  const syncStickyState = () => {
    const root = document.documentElement;
    const bar = document.querySelector('lp-sticky-atc.is-visible');
    if (bar) root.style.setProperty('--lp-sticky-h', `${Math.round(bar.offsetHeight + (parseFloat(getComputedStyle(bar).bottom) || 0)) + 10}px`);
    root.classList.toggle('lp-sticky-on', !!bar);
  };
  if (!customElements.get('lp-sticky-atc')) {
    customElements.define('lp-sticky-atc', class extends HTMLElement {
      connectedCallback() {
        this.form = document.getElementById(this.getAttribute('form'));
        this.footer = document.querySelector('.shopify-section--footer, .footer') || document.querySelector('body > footer, #shopify-section-footer');
        if (!this.form) return;
        if (document.documentElement.classList.contains('lp-sticky-on')) {
          this.style.transition = 'none';
          this.classList.add('is-visible');
          this.removeAttribute('inert');
          requestAnimationFrame(() => requestAnimationFrame(() => { this.style.transition = ''; }));
        }
        this.seen = new Map();
        const note = (entries) => { entries.forEach((e) => this.seen.set(e.target, e.isIntersecting)); this.update(); };
        // The page's button counts as on screen once 48px of it is in view, not at the first pixel.
        this.io = new IntersectionObserver(note, { rootMargin: '0px 0px -48px 0px' });
        this.io.observe(this.form);
        this.footerIo = new IntersectionObserver(note);
        if (this.footer) this.footerIo.observe(this.footer);
      }
      disconnectedCallback() {
        this.io && this.io.disconnect();
        this.footerIo && this.footerIo.disconnect();
        // Replaced by a re-render: the new bar takes over. Removed for good (sold out): clear the state.
        requestAnimationFrame(() => { if (!document.querySelector('lp-sticky-atc')) syncStickyState(); });
      }
      update() {
        if (!this.seen.has(this.form)) return;
        const show = this.seen.get(this.form) === false && !this.seen.get(this.footer);
        this.classList.toggle('is-visible', show);
        this.toggleAttribute('inert', !show);
        syncStickyState();
      }
    });
  }
  window.addEventListener('resize', syncStickyState, { passive: true });

  const whenIdle = (fn) => (window.requestIdleCallback ? requestIdleCallback(fn, { timeout: 2500 }) : setTimeout(fn, 1200));
  if (document.readyState === 'complete') whenIdle(startLazyVideos);
  else window.addEventListener('load', () => whenIdle(startLazyVideos), { once: true });


  const setStep = (root, i, focus) => {
    const tabs = [...root.querySelectorAll('[data-lp-step]')];
    if (!tabs[i]) return;
    tabs.forEach((t, k) => {
      const on = k === i;
      t.setAttribute('aria-selected', on);
      t.tabIndex = on ? 0 : -1;
      t.classList.toggle('is-done', k < i);
    });
    root.querySelectorAll('[data-lp-step-panel]').forEach((p) => p.classList.toggle('is-active', Number(p.dataset.lpStepPanel) === i));
    const list = root.querySelector('[role="tablist"]');
    if (list) list.style.setProperty('--lp-tl-p', tabs.length > 1 ? i / (tabs.length - 1) : 0);
    const media = root.closest('.lp-tl')?.querySelector('[data-lp-step-media]');
    if (media) {
      media.classList.add('is-synced');
      media.querySelectorAll('[data-lp-step-tile]').forEach((t) => t.classList.toggle('is-active', Number(t.dataset.lpStepTile) === i));
    }
    if (focus) tabs[i].focus();
  };
  document.addEventListener('click', (e) => {
    const tab = e.target.closest('[data-lp-step]');
    if (tab) return setStep(tab.closest('[data-lp-steps]'), Number(tab.dataset.lpStep));
    const next = e.target.closest('[data-lp-step-next]');
    if (next) {
      const root = next.closest('[data-lp-steps]');
      const cur = Number(next.closest('[data-lp-step-panel]').dataset.lpStepPanel);
      setStep(root, cur + 1, true);
    }
  });
  document.addEventListener('keydown', (e) => {
    const tab = e.target.closest && e.target.closest('[data-lp-step]');
    if (!tab) return;
    const root = tab.closest('[data-lp-steps]');
    const n = root.querySelectorAll('[data-lp-step]').length;
    const i = Number(tab.dataset.lpStep);
    const map = { ArrowRight: (i + 1) % n, ArrowLeft: (i - 1 + n) % n, Home: 0, End: n - 1 };
    if (!(e.key in map)) return;
    e.preventDefault();
    setStep(root, map[e.key], true);
  });

  const syncOrbit = (section) => {
    const open = section.querySelector('details[data-lp-acc][open]');
    const active = open ? open.dataset.lpAcc : null;
    section.querySelectorAll('[data-lp-node]').forEach((n) => n.setAttribute('aria-expanded', n.dataset.lpNode === active));
  };
  document.addEventListener('click', (e) => {
    const node = e.target.closest('[data-lp-node]');
    if (!node) return;
    const item = document.getElementById(node.getAttribute('aria-controls'));
    if (!item) return;
    item.open = true;
    const section = node.closest('.lp-fx');
    section.querySelectorAll('details[name="' + item.getAttribute('name') + '"]').forEach((d) => { if (d !== item) d.open = false; });
    syncOrbit(section);
    if (!window.matchMedia('(min-width: 1000px)').matches) {
      const r = item.getBoundingClientRect();
      if (r.top < 0 || r.top > window.innerHeight - 120) item.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'center' });
    }
  });
  document.addEventListener('toggle', (e) => {
    if (e.target.matches && e.target.matches('.lp-fx details')) syncOrbit(e.target.closest('.lp-fx'));
  }, true);

  const edgeTone = (frame, img) => {
    try {
      const c = document.createElement('canvas');
      const w = (c.width = 32), h = (c.height = 32);
      const ctx = c.getContext('2d', { willReadFrequently: true });
      ctx.drawImage(img, 0, 0, w, h);
      const d = ctx.getImageData(0, 0, w, h).data;
      const px = [];
      for (let k = 0; k < w; k++) [[k, 0], [k, h - 1], [0, k], [w - 1, k]].forEach(([x, y]) => { const o = (y * w + x) * 4; px.push([d[o], d[o + 1], d[o + 2]]); });
      const avg = [0, 1, 2].map((ch) => px.reduce((a, p) => a + p[ch], 0) / px.length);
      const spread = Math.max(...px.map((p) => Math.max(...p.map((v, ch) => Math.abs(v - avg[ch])))));
      if (spread > 28) return;
      const [r, g, b] = avg.map(Math.round);
      const lin = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
      const L = 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b);
      frame.style.setProperty('--lp-how-bg', `rgb(${r} ${g} ${b})`);
      frame.dataset.tone = (L + 0.05) / 0.063 >= 1.05 / (L + 0.05) ? 'light' : 'dark';
    } catch (err) {}
  };
  const initEdgeBg = () => document.querySelectorAll('[data-lp-edge-bg]').forEach((frame) => {
    const img = frame.querySelector('.lp-how__img');
    if (!img || frame.dataset.tone) return;
    if (img.complete && img.naturalWidth) edgeTone(frame, img);
    else img.addEventListener('load', () => edgeTone(frame, img), { once: true });
  });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initEdgeBg, { once: true });
  else initEdgeBg();
  document.addEventListener('shopify:section:load', initEdgeBg);
})();

/* Cart drawer quantity stepper: +/- update the theme's quantity input and fire 'change', so Impact's line-item-quantity does the cart update. Delegated, because the drawer re-renders its lines. */
(() => {
  document.addEventListener('click', (event) => {
    const button = event.target.closest('.lp-qty__btn');
    if (!button || button.disabled) return;
    const input = button.parentElement.querySelector('.lp-qty__input');
    if (!input) return;
    const step = parseInt(input.step, 10) || 1;
    const min = parseInt(input.min, 10) || 1;
    const max = input.max ? parseInt(input.max, 10) : Infinity;
    const current = parseInt(input.value, 10) || min;
    const next = Math.min(max, Math.max(min, current + (button.classList.contains('lp-qty__btn--plus') ? step : -step)));
    if (next === current) return;
    input.value = next;
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
  });
  document.addEventListener('keydown', (event) => {
    if ((event.key === 'Enter' || event.key === ' ') && event.target.matches('.share-cart-link')) {
      event.preventDefault();
      event.target.click();
    }
  });
})();

/* Free-delivery component in the cart drawer.
   - Re-checks the state with Shopify.currency.rate (same rule as the theme's free-shipping bar), so it is right in every currency.
   - When the drawer re-renders, the bar animates from the previous fill to the new one.
   - Crossing the threshold: the bar fills to 100%, then the card crossfades to "Free Delivery Unlocked" and the HyperFrames truck clip plays.
   - Opening a cart that is already free: the clip plays once per visit; otherwise its final frame (the poster) is the static icon.
   - Reduced motion: no fill animation, no clip. */
(() => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const KEY = 'lp-fd-played';
  let last = null; // { progress, free }
  let pendingPlay = false;
  const sessionPlayed = () => { try { return sessionStorage.getItem(KEY) === '1'; } catch (e) { return false; } };
  const markPlayed = () => { try { sessionStorage.setItem(KEY, '1'); } catch (e) {} };
  const money = (cents) => {
    try { return new Intl.NumberFormat(Shopify.locale, { style: 'currency', currency: Shopify.currency.active }).format(cents / 100); }
    catch (e) { return (cents / 100).toFixed(2); }
  };
  const drawerOpen = () => document.getElementById('cart-drawer')?.hasAttribute('open');
  const play = (el) => {
    const video = el.querySelector('.lp-ship__video');
    if (!video || reduce) return;
    markPlayed();
    try { video.currentTime = 0; } catch (e) {}
    video.play().catch(() => {});
  };

  const sync = (el) => {
    const rate = (window.Shopify && Shopify.currency && Number(Shopify.currency.rate)) || 1;
    const threshold = Math.round(parseFloat(el.dataset.threshold) * rate);
    const total = parseFloat(el.dataset.total) || 0;
    const progress = threshold > 0 ? Math.min(1, Math.max(0, total / threshold)) : 1;
    const free = total >= threshold;
    const remaining = el.querySelector('[data-lp-ship-remaining]');
    const remainingText = money(Math.max(0, threshold - total));
    // While the bar fills on the way to free, keep the last amount so it never reads "0.00 away"
    if (remaining) remaining.textContent = (last && !last.free && free && last.remainingText) ? last.remainingText : remainingText;
    const row = document.querySelector('#cart-drawer [data-lp-ship-row]');
    const fill = el.querySelector('.lp-ship__fill');

    const crossing = last && !last.free && free;
    const moved = last && Math.abs(last.progress - progress) > 0.001;

    if (crossing && !reduce) {
      // Hold the old look, fill the bar, then reveal the unlocked state
      el.classList.remove('is-free');
      el.style.setProperty('--lp-ship-progress', progress);
      const anim = fill.animate([{ transform: `scaleX(${last.progress})` }, { transform: 'scaleX(1)' }], { duration: 650, easing: 'cubic-bezier(.22,1,.36,1)' });
      anim.onfinish = () => {
        el.classList.add('is-free');
        if (row && row.hidden) { row.hidden = false; row.classList.add('is-entering'); }
        drawerOpen() ? play(el) : (pendingPlay = true);
      };
    } else {
      el.classList.toggle('is-free', free);
      el.style.setProperty('--lp-ship-progress', progress);
      if (moved && !reduce) fill.animate([{ transform: `scaleX(${last.progress})` }, { transform: `scaleX(${progress})` }], { duration: 600, easing: 'cubic-bezier(.22,1,.36,1)' });
      if (row) {
        if (row.hidden === free && free && last && !last.free) row.classList.add('is-entering');
        row.hidden = !free;
      }
      if (free && !last && !sessionPlayed()) drawerOpen() ? play(el) : (pendingPlay = true);
    }
    last = { progress, free, remainingText: free ? (last && last.remainingText) : remainingText };
  };

  const scan = () => {
    const el = document.querySelector('#cart-drawer [data-lp-ship]');
    if (!el) { const row = document.querySelector('#cart-drawer [data-lp-ship-row]'); if (row) row.hidden = true; last = last && { progress: 0, free: false }; return; }
    if (el.dataset.lpShipSynced) return;
    el.dataset.lpShipSynced = '1';
    sync(el);
  };

  const start = () => {
    const drawer = document.getElementById('cart-drawer');
    if (!drawer) return;
    new MutationObserver((records) => {
      if (records.some((r) => r.type === 'childList')) scan();
      if (records.some((r) => r.type === 'attributes') && drawer.hasAttribute('open') && pendingPlay) {
        pendingPlay = false;
        const el = drawer.querySelector('[data-lp-ship]');
        if (el && el.classList.contains('is-free')) setTimeout(() => play(el), 300);
      }
    }).observe(drawer, { childList: true, subtree: true, attributes: true, attributeFilter: ['open'] });
    scan();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
