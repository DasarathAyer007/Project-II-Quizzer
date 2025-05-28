document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('loginForm');
  const email = document.getElementById('email');
  const password = document.getElementById('pass');
  const emailError = document.getElementById('emailError');
  const passwordError = document.getElementById('passwordError');

  form.addEventListener('submit', (e) => {
    let isValid = true;
    emailError.classList.add('hidden');
    passwordError.classList.add('hidden');

    if (!email.value || !/\S+@\S+\.\S+/.test(email.value)) {
      emailError.classList.remove('hidden');
      isValid = false;
    }

    if (!password.value || password.value.length < 6) {
      passwordError.classList.remove('hidden');
      isValid = false;
    }

    if (!isValid) {
      e.preventDefault();
    }
  });
});