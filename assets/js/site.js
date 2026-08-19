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

// Testimonial cards open the full review in a modal.
(function () {
  var modal = document.getElementById('review-modal');
  if (!modal) return;
  var panel = modal.querySelector('.modal__panel');
  var lead = modal.querySelector('.modal__lead');
  var body = modal.querySelector('.modal__body');
  var cite = modal.querySelector('.modal__cite');
  var lastFocused = null;

  function open(card) {
    lastFocused = card;
    lead.textContent = card.querySelector('p').textContent;
    body.innerHTML = card.querySelector('.quote__full').innerHTML;
    cite.textContent = card.querySelector('cite').textContent;
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

  document.querySelectorAll('.quote--open').forEach(function (card) {
    card.addEventListener('click', function () { open(card); });
    card.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(card); }
    });
  });

  modal.addEventListener('click', function (e) {
    if (e.target === modal || e.target.hasAttribute('data-modal-close')) close();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && modal.classList.contains('is-open')) close();
  });
})();

// Body Ready Method pillars reuse the same modal as the reviews.
(function () {
  var modal = document.getElementById('review-modal');
  if (!modal) return;
  var lead = modal.querySelector('.modal__lead');
  var body = modal.querySelector('.modal__body');
  var cite = modal.querySelector('.modal__cite');
  var last = null;

  function open(card) {
    last = card;
    lead.textContent = card.querySelector('h3').textContent;
    body.innerHTML = card.querySelector('.quote__full').innerHTML;
    cite.textContent = '';
    modal.classList.add('is-open');
    document.body.classList.add('modal-open');
    modal.querySelector('.modal__panel').scrollTop = 0;
    modal.querySelector('.modal__close').focus();
  }

  document.querySelectorAll('.pillar--open').forEach(function (card) {
    card.addEventListener('click', function () { open(card); });
    card.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(card); }
    });
  });

  modal.addEventListener('click', function (e) {
    if (e.target === modal || e.target.hasAttribute('data-modal-close')) {
      if (last) last.focus();
    }
  });
})();
