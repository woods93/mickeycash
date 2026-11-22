(function () {
  // Click-to-load YouTube players: nothing from YouTube loads until a viewer presses play.
  document.querySelectorAll('button.yt').forEach(function (b) {
    b.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + b.getAttribute('data-id') + '?autoplay=1&rel=0';
      f.title = b.getAttribute('aria-label') || 'YouTube video';
      f.allow = 'accelerometer; autoplay; encrypted-media; picture-in-picture; fullscreen';
      f.allowFullscreen = true;
      b.replaceWith(f);
    });
  });

  // Email link is assembled here so the address isn't sitting in the page source for scrapers.
  document.querySelectorAll('a.mail').forEach(function (a) {
    var addr = a.getAttribute('data-u') + '@' + a.getAttribute('data-d');
    a.href = 'mailto:' + addr;
    a.textContent = addr;
  });

  var y = document.getElementById('yr');
  if (y) y.textContent = new Date().getFullYear();

  // Contact form via Web3Forms, without leaving the page.
  var form = document.getElementById('contact-form');
  if (!form) return;
  var status = form.querySelector('.form-status');
  var btn = form.querySelector('button[type="submit"]');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    status.className = 'form-status';
    if (!form.getAttribute('data-key')) {
      status.className = 'form-status err';
      status.textContent = 'The contact form is not switched on yet. Please use the email address above.';
      return;
    }
    status.textContent = 'Sending…';
    btn.disabled = true;
    fetch(form.action, { method: 'POST', headers: { 'Accept': 'application/json' }, body: new FormData(form) })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        if (d.success) { status.className = 'form-status ok'; status.textContent = 'Thanks! Your message was sent.'; form.reset(); }
        else { throw new Error(d.message || 'failed'); }
      })
      .catch(function () { status.className = 'form-status err'; status.textContent = 'Sorry, that didn’t go through. Please use the email address above.'; })
      .then(function () { btn.disabled = false; });
  });
})();
