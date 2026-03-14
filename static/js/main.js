'use strict';

/* ======================================
   MAGNUM — Main JS
   Mobile-First, iOS Safari compatible
   ====================================== */

// ── Apply language from django_language cookie before first paint ──
(function () {
  const match = document.cookie.match(/django_language=([^;]+)/);
  if (match) document.documentElement.lang = match[1];
}());

// ── Header scroll effect ──────────────────────────────────────────
const header = document.getElementById('site-header');
if (header) {
  const onScroll = () => {
    header.classList.toggle('scrolled', window.scrollY > 40);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

// ── Mobile Nav ────────────────────────────────────────────────────
const navToggle = document.getElementById('nav-toggle');
const mainNav   = document.getElementById('main-nav');
const overlay   = document.getElementById('nav-overlay');

function openNav() {
  navToggle.classList.add('open');
  navToggle.setAttribute('aria-expanded', 'true');
  mainNav.classList.add('open');
  overlay.classList.add('visible');
  document.body.style.overflow = 'hidden';
}

function closeNav() {
  navToggle.classList.remove('open');
  navToggle.setAttribute('aria-expanded', 'false');
  mainNav.classList.remove('open');
  overlay.classList.remove('visible');
  document.body.style.overflow = '';
}

if (navToggle && mainNav) {
  navToggle.addEventListener('click', () => {
    const isOpen = mainNav.classList.contains('open');
    isOpen ? closeNav() : openNav();
  });

  overlay && overlay.addEventListener('click', closeNav);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mainNav.classList.contains('open')) closeNav();
  });

  mainNav.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth < 768) closeNav();
    });
  });
}

// ── Smooth scroll for same-page anchor links ──────────────────────
document.querySelectorAll('a[href*="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    const href = anchor.getAttribute('href');
    const hashIdx = href.indexOf('#');
    if (hashIdx === -1) return;
    const hash = href.substring(hashIdx);
    if (!hash || hash === '#') return;

    const isExternalPage = href.substring(0, hashIdx).length > 0
      && !href.substring(0, hashIdx).endsWith(window.location.pathname);

    if (isExternalPage) return;

    const target = document.querySelector(hash);
    if (!target) return;

    e.preventDefault();
    const top = target.getBoundingClientRect().top + window.scrollY - 72;
    window.scrollTo({ top, behavior: 'smooth' });
    history.replaceState(null, '', hash);
  });
});

// ── Scroll to hash on page load (for cross-page anchor links) ─────
window.addEventListener('DOMContentLoaded', () => {
  const hash = window.location.hash;
  if (hash) {
    const target = document.querySelector(hash);
    if (target) {
      setTimeout(() => {
        const top = target.getBoundingClientRect().top + window.scrollY - 72;
        window.scrollTo({ top, behavior: 'smooth' });
      }, 100);
    }
  }
});

// ── Language form — keep current path for Django set_language ──────
const langNext = document.getElementById('lang-next');
if (langNext) {
  langNext.value = window.location.pathname;
}

// ── HTMX CSRF token injection ─────────────────────────────────────
document.addEventListener('htmx:configRequest', (e) => {
  const csrfInput = document.querySelector('[name=csrfmiddlewaretoken]');
  if (csrfInput) {
    e.detail.headers['X-CSRFToken'] = csrfInput.value;
  }
});

// ── Product gallery thumbnail switcher ───────────────────────────
const galleryMainImg = document.getElementById('gallery-main-img');
if (galleryMainImg) {
  document.querySelectorAll('.thumb-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const src = btn.dataset.src;
      if (!src) return;

      galleryMainImg.style.opacity = '0';
      galleryMainImg.style.transform = 'scale(0.98)';
      galleryMainImg.style.transition = 'opacity 0.2s ease, transform 0.2s ease';

      setTimeout(() => {
        galleryMainImg.src = src;
        galleryMainImg.style.opacity = '1';
        galleryMainImg.style.transform = 'scale(1)';
      }, 180);

      document.querySelectorAll('.thumb-btn').forEach(b => b.classList.remove('thumb-btn--active'));
      btn.classList.add('thumb-btn--active');
    });
  });
}

// ── HTMX — preserve scroll after form submission ──────────────────
document.addEventListener('htmx:afterSwap', (e) => {
  if (e.target.id === 'contact-form-wrap') {
    e.target.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
});

// ── Intersection Observer — reveal on scroll ──────────────────────
if ('IntersectionObserver' in window) {
  const revealEls = document.querySelectorAll(
    '.service-item, .preview-card, .stat-item, .product-row'
  );

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  revealEls.forEach((el, i) => {
    el.style.setProperty('--reveal-delay', `${i * 60}ms`);
    observer.observe(el);
  });
}

// ── iOS viewport height fix ───────────────────────────────────────
function setVH() {
  const vh = window.innerHeight * 0.01;
  document.documentElement.style.setProperty('--vh', `${vh}px`);
}
setVH();
window.addEventListener('resize', setVH, { passive: true });
