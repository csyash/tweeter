document.addEventListener("DOMContentLoaded", () => {
  login_form = document.getElementById("login-form");
  reg_form = document.getElementById("registration-form");
  sign_up = document.getElementById("sign-up");
  sign_in = document.getElementById("sign-in");

  sign_up.onclick = () => {
    login_form.style.display = "none";
    reg_form.style.display = "block";
  };

  sign_in.onclick = () => {
    reg_form.style.display = "none";
    login_form.style.display = "block";
  };

  reg_form.style.display = "none";
});
