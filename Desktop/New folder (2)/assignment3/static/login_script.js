const container = document.querySelector(".container"),
  pwshowhide = document.querySelectorAll(".showhidepw"),
  pwfields = document.querySelectorAll(".password"),
  login_form = document.querySelector(".login_form");


pwshowhide.forEach((eyeIcon) => {
  eyeIcon.addEventListener("click", () => {
    pwfields.forEach((pwfield) => {
      console.log(pwfield.type);
      if (pwfield.type === "password") {
        pwfield.type = "text";

        pwshowhide.forEach((icon) => {
          icon.classList.replace("uil-eye-slash", "uil-eye");
        });
      } else {
        pwfield.type = "password";

        pwshowhide.forEach((icon) => {
          icon.classList.replace("uil-eye", "uil-eye-slash");
        });
      }
    });
  });
});

login_form.addEventListener("submit", (e) => {
  e.preventDefault();
  username = login_form.username.value;
  password = login_form.pass.value;
  UserLogin(username, password).then((data) => {
    if (data != undefined) {
      location.href = 'index.html';
    }
  });

});



