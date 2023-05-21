(() => {
  let form = document.querySelector('.needs-validation');

  form.addEventListener('submit', (event) => {
    if (!form.checkValidity()) {
      form.classList.add('was-validated');

      event.preventDefault();
      event.stopPropagation();
    }
  });
})();