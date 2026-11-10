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
    const toNum = (t) => parseFloat((t || '').replace(/[^0-9.,]/g, '').replace(/,(?=\d{3}\b)/g, '').replace(',', '.')) || 0;
    const a = toNum(now.textContent), b = toNum(was.dataset.base || was.textContent);
    const discounted = a > 0 && b > a + 0.001;
    was.hidden = !discounted;
    if (tag) { tag.hidden = !discounted; if (discounted) tag.textContent = 'Save ' + Math.round((1 - a / b) * 100) + '%'; }
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


  const initReferralNudge = () => {
    const panel = document.querySelector('[data-lp-ref]');
    const tab = document.querySelector('[data-lp-ref-tab]');
    if (!panel || !tab) return;
    const KEY = 'lp-ref-dismissed';
    const TTL = 14 * 24 * 60 * 60 * 1000;
    const store = {
      get() { try { return Number(localStorage.getItem(KEY)) || 0; } catch (e) { return 0; } },
      set() { try { localStorage.setItem(KEY, String(Date.now())); } catch (e) { /* storage unavailable */ } }
    };
    const video = panel.querySelector('video');
    const tabLabel = tab.querySelector('[data-lp-ref-tab-label]');
    const appButton = () => document.querySelector('.referral-banner__name--clickable');
    const referrerName = () => {
      const title = document.querySelector('.referral-banner__title');
      const button = appButton();
      if (!button || !title || getComputedStyle(title).display === 'none') return '';
      return button.textContent.trim();
    };
    let open = false;
    let timer = 0;

    const showTab = () => {
      const name = referrerName();
      tabLabel.textContent = name ? `With ${name}` : 'Referred?';
      tab.setAttribute('aria-label', name ? `You are shopping with ${name}. Change referrer` : 'Were you referred by someone?');
      tab.hidden = false;
      requestAnimationFrame(() => tab.classList.add('is-shown'));
    };
    const hideTab = () => { tab.classList.remove('is-shown'); };

    const playArt = () => {
      if (!video || reduceMotion) return;
      const source = video.querySelector('source[data-src]');
      if (source) { source.src = source.dataset.src; source.removeAttribute('data-src'); video.load(); }
      video.currentTime = 0;
      const attempt = video.play();
      if (attempt && attempt.catch) attempt.catch(() => {});
    };

    const openPanel = () => {
      if (open || !appButton()) return;
      open = true;
      clearTimeout(timer);
      hideTab();
      panel.hidden = false;
      requestAnimationFrame(() => requestAnimationFrame(() => { panel.classList.add('is-open'); playArt(); }));
    };
    const closePanel = (remember) => {
      if (!open) return;
      open = false;
      panel.classList.remove('is-open');
      if (remember) store.set();
      setTimeout(() => { if (!open) panel.hidden = true; }, 600);
      showTab();
    };

    panel.addEventListener('click', (event) => {
      if (event.target.closest('[data-lp-ref-close]')) closePanel(true);
      if (event.target.closest('[data-lp-ref-open]')) {
        const button = appButton();
        closePanel(true);
        if (button) button.click();
      }
    });
    panel.addEventListener('keydown', (event) => { if (event.key === 'Escape') closePanel(true); });
    tab.addEventListener('click', () => {
      if (referrerName()) { const button = appButton(); if (button) button.click(); return; }
      openPanel();
    });

    const start = () => {
      if (referrerName()) { showTab(); return; }
      if (Date.now() - store.get() < TTL) { showTab(); return; }
      const trigger = () => { window.removeEventListener('scroll', onScroll); openPanel(); };
      const onScroll = () => { if (window.scrollY > window.innerHeight * 0.35) trigger(); };
      window.addEventListener('scroll', onScroll, { passive: true });
      timer = setTimeout(trigger, 6000);
    };

    let tries = 0;
    const waitForApp = () => {
      if (appButton()) { start(); return; }
      if (++tries < 40) setTimeout(waitForApp, 250);
    };
    waitForApp();

    const banner = () => document.querySelector('.referral-banner');
    const watch = new MutationObserver(() => {
      if (referrerName()) { if (open) closePanel(true); else if (!tab.hidden) showTab(); }
    });
    const attach = () => { const b = banner(); if (b) watch.observe(b, { subtree: true, childList: true, characterData: true, attributes: true, attributeFilter: ['style'] }); };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', attach, { once: true }); else attach();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initReferralNudge, { once: true });
  else initReferralNudge();

  const whenIdle = (fn) => (window.requestIdleCallback ? requestIdleCallback(fn, { timeout: 2500 }) : setTimeout(fn, 1200));
  if (document.readyState === 'complete') whenIdle(startLazyVideos);
  else window.addEventListener('load', () => whenIdle(startLazyVideos), { once: true });

})();
