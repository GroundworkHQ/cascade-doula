// Mobile nav
document.querySelectorAll('[data-nav-toggle]').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var nav = document.getElementById('primary-nav');
    var open = nav.classList.toggle('is-open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
});

// The contact form is presentation only in this proposal. Intercept the submit
// so a visitor never sees a dead button or a page reload that loses their input.
document.querySelectorAll('[data-demo-form]').forEach(function (form) {
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var status = form.querySelector('.form-status');
    if (!status) return;
    status.classList.add('is-visible');
    status.focus();
    status.scrollIntoView({ behavior: 'smooth', block: 'center' });
  });
});

// Testimonial cards and Body Ready Method pillars share one modal.
// These used to be two separate IIFEs with two sets of listeners. Only the
// first owned the Escape handler and its focus restoration, so closing a
// pillar modal with Escape stranded focus on the hidden close button. One
// controller, one set of listeners, focus returns from either kind of card.
(function () {
  var modal = document.getElementById('review-modal');
  if (!modal) return;
  var panel = modal.querySelector('.modal__panel');
  var lead = modal.querySelector('.modal__lead');
  var body = modal.querySelector('.modal__body');
  var cite = modal.querySelector('.modal__cite');
  var lastFocused = null;

  function open(card, leadText, citeText) {
    lastFocused = card;
    lead.textContent = leadText;
    body.innerHTML = card.querySelector('.quote__full').innerHTML;
    cite.textContent = citeText;
    modal.classList.add('is-open');
    document.body.classList.add('modal-open');
    panel.scrollTop = 0;
    modal.querySelector('.modal__close').focus();
  }

  function close() {
    modal.classList.remove('is-open');
    document.body.classList.remove('modal-open');
    if (lastFocused) lastFocused.focus();
  }

  function bind(card, getLead, getCite) {
    function fire() { open(card, getLead(card), getCite(card)); }
    card.addEventListener('click', fire);
    card.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fire(); }
    });
  }

  document.querySelectorAll('.quote--open').forEach(function (card) {
    bind(card,
      function (c) { return c.querySelector('p').textContent; },
      function (c) { return c.querySelector('cite').textContent; });
  });

  document.querySelectorAll('.pillar--open').forEach(function (card) {
    bind(card,
      function (c) { return c.querySelector('h3').textContent; },
      function () { return ''; });
  });

  modal.addEventListener('click', function (e) {
    if (e.target === modal || e.target.hasAttribute('data-modal-close')) close();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && modal.classList.contains('is-open')) close();
  });
})();
