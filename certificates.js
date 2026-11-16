(() => {
  'use strict';
  const cards = [...document.querySelectorAll('.certificate-card')];
  const filters = [...document.querySelectorAll('[data-filter]')];
  const results = document.getElementById('certificate-results');
  filters.forEach(button => button.addEventListener('click', () => {
    const category = button.dataset.filter;
    filters.forEach(item => {
      item.classList.toggle('is-active', item === button);
      item.setAttribute('aria-pressed', String(item === button));
    });
    cards.forEach(card => { card.hidden = category !== 'all' && card.dataset.category !== category; });
    const count = cards.filter(card => !card.hidden).length;
    results.textContent = `Showing ${count} ${category === 'all' ? '' : category === 'ai' ? 'AI and strategy ' : 'finance and markets '}certificate${count === 1 ? '' : 's'}.`;
  }));
  const dialog = document.querySelector('.certificate-dialog');
  const image = document.getElementById('viewer-image');
  const title = document.getElementById('viewer-title');
  const issuer = document.getElementById('viewer-issuer');
  const pdf = document.getElementById('viewer-pdf');
  const count = document.getElementById('viewer-count');
  const certificateLinks = [...document.querySelectorAll('[data-certificate]')];
  let current = 0, opener;
  let visibleLinks = certificateLinks;
  function show(index) {
    current = (index + visibleLinks.length) % visibleLinks.length;
    const link = visibleLinks[current];
    image.src = link.dataset.image;
    image.alt = `${link.dataset.title} certificate awarded to Ram Arora`;
    title.textContent = link.dataset.title;
    issuer.textContent = link.dataset.issuer;
    pdf.href = link.href;
    count.textContent = `${current + 1} / ${visibleLinks.length}`;
    document.getElementById('viewer-previous').disabled = visibleLinks.length < 2;
    document.getElementById('viewer-next').disabled = visibleLinks.length < 2;
  }
  certificateLinks.forEach(link => link.addEventListener('click', event => {
    if (!dialog.showModal || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    opener = link;
    visibleLinks = certificateLinks.filter(item => !item.closest('.certificate-card').hidden);
    show(visibleLinks.indexOf(link));
    dialog.showModal();
    document.body.style.overflow = 'hidden';
    dialog.querySelector('.viewer-close').focus();
  }));
  dialog.querySelector('.viewer-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('close', () => { document.body.style.overflow = ''; opener?.focus(); });
  dialog.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft') { event.preventDefault(); show(current - 1); }
    if (event.key === 'ArrowRight') { event.preventDefault(); show(current + 1); }
  });
  document.getElementById('viewer-previous').addEventListener('click', () => show(current - 1));
  document.getElementById('viewer-next').addEventListener('click', () => show(current + 1));
  const navigationLinks = [...document.querySelectorAll('.site-nav a[href^="#"]')];
  const sectionObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) navigationLinks.forEach(link => link.classList.toggle('active', link.hash === `#${entry.target.id}`));
    });
  }, { rootMargin: '-10% 0px -60% 0px' });
  document.querySelectorAll('main > section[id]').forEach(section => sectionObserver.observe(section));
})();
