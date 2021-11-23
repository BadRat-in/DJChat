function matchnum(str) {
    var mail = document.getElementById("mail");
    var num = document.getElementById("number");
    var otp_f = document.getElementById("otp");
    var regexp = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    if (num.value.length === 10 && regexp.test(String(mail.value).toLowerCase())) {
        document.getElementById("loader").style = "display: flex";
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                var response = this.responseText;
                response = response.split("\n");
                console.log(typeof response)
                if ((typeof response).toString() === "object") {
                    document.getElementById("error-div").innerHTML = "OPT send.";
                    var otp = document.createElement("input");
                    var hashid = document.createElement("input");
                    otp.type = "hidden";
                    hashid.type = "hidden";
                    otp.value = response[0];
                    hashid.value = response[1];
                    otp.id = "hexotp";
                    hashid.id = "hashid";
                    var pr = mail.parentElement;
                    pr.append(otp);
                    pr.append(hashid);
                    mail.setAttribute("readonly", true);
                    num.setAttribute("readonly", true);
                    mail.className = "input_field not";
                    num.className = "input_field not";
                    otp_f.removeAttribute("readonly");
                    otp_f.style = "cursor: auto;";
                    document.getElementById("error-div").style = "display: block; color: green;";
                    document.getElementById(str).value = "Submit";
                    document.getElementById("sub-btn").style = "cursor: pointer;";
                    document.getElementById("sub-btn").setAttribute("onclick", "matchotp()");
                    document.getElementById("loader").style = "display: none;";
                } else if (response === "not-match") {
                    document.getElementById("error-div").innerHTML = "Number or Mail dose not match.";
                    document.getElementById("error-div").style = "display: block; color: #ee3333;";
                    document.getElementById("loader").style = "display: none;";
                } else {
                    document.getElementById("error-div").innerHTML = "OPT not send.";
                    document.getElementById("error-div").style = "display: block; color: #ee3333;";
                    document.getElementById("loader").style = "display: none;";
                }
            }
        }
        xmlhttp.open("GET", "/matchnum/?num=" + num.value + "&mail=" + mail.value, true);
        xmlhttp.send();
    }
}

function check() {
    var mail = document.getElementById("mail");
    var num = document.getElementById("number");
    var regexp = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    if (num.value.length === 10 && regexp.test(String(mail.value).toLowerCase())) {
        document.getElementById("sub-btn").style = "cursor: pointer;"
    } else {
        document.getElementById("sub-btn").style = "cursor: not-allowed;"
    }

}

function matchotp() {
    var hashid = document.getElementById("hashid");
    var otp_f = document.getElementById("otp");
    var hexotp = document.getElementById("hexotp");
    var hash = CryptoJS.MD5(otp_f.value);
    if (hash.toString() === hexotp.value) {
        window.location.assign("/forgotpasswd/resetpass/?hashid=" + hashid.value);
    } else {
        document.getElementById("error-div").style = "display: block; color: #ee3333;";
        document.getElementById("error-div").innerHTML = "OTP not match.";
    }
}


function matchpass() {
    var pass = document.getElementById("pass");
    var conf = document.getElementById("conform");
    if (pass.value === conf.value) {
        document.getElementById("sub-btn").style = "cursor: pointer;"
        conf.style = "border: none";
    } else {
        document.getElementById("sub-btn").style = "cursor: not-allowed;"
        conf.style = "border:solid 1px red;";
    }
}

function savepass() {
    var hashid = document.getElementById("hashid");
    var pass = document.getElementById("pass");
    var conf = document.getElementById("conform");
    if (pass.value === conf.value) {
        document.getElementById("loader").style = "display: flex;";
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                var response = this.responseText;
                if (response === "Done") {
                    window.location.assign("/")
                } else {
                    document.getElementById("loader").style = "display: none;";
                    document.getElementById("error-div").style = "display: block; color: #ee3333;";
                    document.getElementById("error-div").innerHTML = "Password Not Changed. Please try after some time";
                }
            }
        }
        xmlhttp.open("GET", "/forgotpasswd/savepass/?hashid=" + hashid.value + "&passwd=" + conf.value, true);
        xmlhttp.send();
    }
}