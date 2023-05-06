(() => {
  var forms = document.querySelectorAll('.needs-validation');

  Array.prototype.slice.call(forms)
    .forEach((form) => {
      form.addEventListener('submit', (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add('was-validated');
      }, false);
    });
})();

(() => {
  window.onload = function () {
    var pos = window.name || 0;
    window.scrollTo(0, pos);
  }

  window.onunload = function () {
    window.name = self.pageYOffset || (document.documentElement.scrollTop + document.body.scrollTop);
  }
})();