(function () {
  function init(root) {
    var form = root.querySelector('form');
    if (!form) return;
    var prices = root.querySelectorAll('[data-lmv-price]');
    form.querySelectorAll('input[name=id]').forEach(function (r) {
      r.addEventListener('change', function () {
        prices.forEach(function (p) { p.textContent = r.getAttribute('data-price'); });
      });
    });
    var q = form.querySelector('input[name=quantity]');
    var dec = form.querySelector('[data-lmv-dec]');
    var inc = form.querySelector('[data-lmv-inc]');
    if (dec) dec.addEventListener('click', function () { q.value = Math.max(1, (+q.value || 1) - 1); });
    if (inc) inc.addEventListener('click', function () { q.value = Math.min(10, (+q.value || 1) + 1); });
    var bar = root.querySelector('[data-lmv-bar]');
    var buy = root.querySelector('#buy');
    if (bar && buy && 'IntersectionObserver' in window) {
      new IntersectionObserver(function (e) {
        bar.classList.toggle('on', !e[0].isIntersecting && e[0].boundingClientRect.top < 0);
      }).observe(buy);
    }
  }
  function boot() { document.querySelectorAll('.lmv').forEach(init); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();