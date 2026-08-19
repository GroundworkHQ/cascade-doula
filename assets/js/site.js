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
