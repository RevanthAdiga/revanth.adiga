register_form = document.querySelector(".register_form");
pwshowhide = document.querySelectorAll(".showhidepw");
pwfields = document.querySelectorAll(".password");

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

register_form.addEventListener("submit", (e) => {
    e.preventDefault();
    firstname = register_form.first_name.value;
    lastname = register_form.last_name.value;
    username = register_form.username.value;
    pass1 = register_form.register_pass1.value;
    pass2 = register_form.register_pass2.value;
    if (pass1 === pass2) {
        console.log("Data successfully stored");
        password = pass1;
        UserRegister(firstname, lastname, username, password);
    }
    else {
        console.log("Password did not match!");
    }
});