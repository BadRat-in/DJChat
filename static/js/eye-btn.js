function showpass(id0, id1) {
    const passwd = document.querySelector("#" + id0);
    const passwd_icon = document.querySelector("#" + id1);
    if (passwd.getAttribute("type") === "text") {
        passwd.setAttribute("type", "password");
        passwd_icon.className = "far fa-eye passwd-icon";
        passwd_icon.style = "left: -26px; font-size: 18px;";

    } else {
        passwd.setAttribute("type", "text");
        passwd_icon.className = "far fa-eye-slash passwd-icon";
        passwd_icon.style = "left: -27px;"

    }
}


function showpassSignup(id0, id1) {
    const passwd = document.querySelector("#" + id0);
    const passwd_icon = document.querySelector("#" + id1);
    if (passwd.getAttribute("type") === "text") {
        passwd.setAttribute("type", "password");
        passwd_icon.className = "far fa-eye passwd-icon";
        passwd_icon.style = "left: -26px; font-size: 18px;";

    } else {
        passwd.setAttribute("type", "text");
        passwd_icon.className = "far fa-eye-slash passwd-icon";
        passwd_icon.style = "left: -27px;"

    }
}