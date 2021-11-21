var you = "";
var me = "";
var mail = "";
var you_num = "";
var msg_box = document.getElementById('msg-box');

var input = document.getElementById("msg-input");
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("send-msg").click();
    }
});


window.addEventListener("beforeunload", function(event) {
    event.closeDWin
    event.preventDefault();
    window.location.assign("/timeline/logout/");
});

function getUser() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var data = this.responseText;
            console.log(data);
        }
    }
    xmlhttp.open("GET", "/timeline/getuser/?me=" + me, true);
    xmlhttp.send();
}

function sendmsg() {
    var msg = document.getElementById('msg-input');
    if (msg.value !== "" && msg.value.length < 100) {
        if (you === "" || you === null || me === "" || me === null) {
            var name = document.getElementById("name").innerText;
            alert("Hey, " + name + "\n\tPlease select a friend to chat. Thankyou")
        } else {
            const today = new Date();
            var hour = today.getHours();
            var min = today.getMinutes();
            if (hour === 0) {
                hour = 12;
            } else if (hour < 10) {
                hour = "0" + hour;
            } else {
                hour = hour;
            }
            if (min < 10) {
                min = "0" + min;
            } else {
                min = min;
            }
            if (today.getHours() < 12) {
                var msg_time = hour + ":" + min + " AM";
            } else {
                var msg_time = hour + ":" + min + " PM";
            }
            if (msg.length !== "") {
                var xmlhttp = new XMLHttpRequest();
                xmlhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        var data = this.responseText;
                        if (data == "Send") {
                            time += " " + data;
                        } else {
                            time += " Fail";
                        }
                    }
                }
                xmlhttp.open("GET", "/timeline/savemessage/?msg" + msg.value + "&you=" + you + "&me=" + me + "&time=" + msg_time, true);
                xmlhttp.send();
            }
            var d = document.createElement("div");
            var p = document.createElement("p");
            p.innerText = msg.value;
            d.append(p);
            msg_box.innerHTML += "<div class='my-msg'><div class='my'>" + d.innerHTML + "<div class='msg-time'><p>" + msg_time + "</p></div></div><img src='../static/Image/user.jpg' alt='User Avtar'>";
            msg.value = "";
            const scrollHeight = msg_box.scrollHeight;
            msg_box.scrollTo({
                top: scrollHeight,
                behavior: "smooth",
            });
        }
    }
}

var height = 0
msg_box.addEventListener("scroll", (e) => {
    if (height > msg_box.scrollTop) {
        document.getElementById("bottom-btn").style = "display: flex;";
    }
    height = msg_box.scrollTop;
});

function slideToBottol() {
    const scrollHeight = msg_box.scrollHeight;
    msg_box.scrollTo({
        top: scrollHeight,
        behavior: "smooth",
    })
    document.getElementById("bottom-btn").style.display = "none";
}


function setUserId() {
    me = document.getElementById("sender-id").value;

}

function SendtoChat(str) {
    you = str;
    var name = document.getElementById("name-" + str).innerHTML;
    mail = document.getElementById("mail-" + str).innerHTML;
    var image = document.getElementById("img-" + str).getAttribute("src");
    var uStatus = document.getElementById("status-" + str).value;
    you_num = document.getElementById("number-" + str).value;
    if (uStatus === "1") {
        uStatus = "Online";
    } else {
        uStatus = "Offline";
    }
    document.getElementById("s-u-i").setAttribute("src", image);
    document.getElementById("s-u-n").innerHTML = name;
    if (uStatus === "Online") {
        document.getElementById("s-u-s").style.color = "#55ff55";
    } else {
        document.getElementById("s-u-s").style.color = "#aa5555";
    }
    document.getElementById("s-u-s").innerHTML = uStatus;
    document.getElementById("s-u-num").value = you_num;
}


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function closeDWin() {
    var ele = document.getElementById("container");
    document.getElementById("show-d").style = "animation: none; animation: zoom-out-win 350ms ease, reverse-win 350ms ease;";
    await sleep(350);
    ele.style = "display: none;";
}

function showDetails() {
    var name = document.getElementById("s-u-n").innerHTML;
    var image = document.getElementById("s-u-i").getAttribute("src");
    var ele = document.getElementById("container");
    document.getElementById("s-detail-u-n").innerHTML = name;
    document.getElementById("s-detail-u-m").innerHTML = mail;
    document.getElementById("s-detail-u-i").setAttribute("src", image);
    document.getElementById("s-detail-u-num").innerHTML = you_num;
    ele.style = "display: flex;";
    document.getElementById("show-d").style = "animation: changeplace 350ms ease, scale 350ms ease;";

}

function getStatus(str) {
    setInterval(() => {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                var nStatus = this.responseText;
                if (nStatus == 0) {
                    document.getElementById("s-u-s").style.color = "#aa5555";
                    nStatus = "Offline";
                } else {
                    nStatus = "Online";
                    document.getElementById("s-u-s").style.color = "#55ff55";
                }
                document.getElementById("s-u-s").innerHTML = nStatus;
            }
        };
        xmlhttp.open("GET", "/timeline/getstatus/?q=" + str, true);
        xmlhttp.send();
    }, 250);
}


async function openClip() {
    var attenment = document.getElementById("attenment");
    var plusIcon = document.getElementById("plus-icon");
    if (window.getComputedStyle(attenment).width === "30px") {
        plusIcon.style = "animation: rotate45 250ms ease;";
        attenment.style = "animation: expandWidth 250ms ease-in;";
        await sleep(250);
        plusIcon.style = "transform: rotate(45deg);"
        attenment.style = "width: 190px;"
    } else {
        plusIcon.style = "animation: rotate0 250ms ease;";
        attenment.style = "animation: srinkdWidth 250ms ease-in;";
        await sleep(250);
        attenment.style = "width: 30px;"
        plusIcon.style = "transform: rotate(0deg);"
    }
}

function searchUser(str) {
    if (str.length == 0) {
        return;
    } else {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                var data1 = this.responseText;
                data = data1.split("[");
                if ((data1) == "No data available") {
                    document.getElementById("userlist").innerHTML = "<h4>" + data + "</h4>";
                } else {
                    var temp_array = []
                    data.forEach((value, index, array) => {
                        var temp = value.split(", ");
                        temp_array.push(temp)
                    });
                    temp_array.splice(0, 1)
                    var html_data = ""
                    temp_array.forEach((value, index, array) => {
                        var nametemp = value[0].split("");
                        var mailtemp = value[1].split("");
                        let counter;
                        if (value[0].length < 20) {
                            counter = value[0].length - 1;
                        } else {
                            counter = 20;
                        }
                        for (var i = 0; i < counter; i++) {
                            if (i === 1) {
                                value[0] = nametemp[i]
                            } else {
                                value[0] += nametemp[i]
                            }
                        }
                        if (value[1].length < 25) {
                            counter = value[1].length - 1;
                        } else {
                            counter = 25;
                        }
                        for (var i = 0; i < counter; i++) {
                            if (i === 1) {
                                value[1] = mailtemp[i]
                            } else {
                                value[1] += mailtemp[i]
                            }
                        }
                        if (value[0].length === 19) {
                            value[0] += "...";
                        }
                        if (value[1].length === 24) {
                            value[1] += "...";
                        }
                        html_data += "<li onclick='SendtoChat(this.id), getStatus(this.id)' id='" + value[3].slice(1, -1) + "'><div class='user-tile'><div class='user-details-tile'><img class='avtar-img' src=" + value[2] + " alt='User Avtar' id='img-" + value[3].slice(1, -1) + "'><div><input type='hidden' name='userid' value='" + value[3].slice(1, -1) + "'/><input type='hidden' name='userStatus' value='" + value[4].slice(0, 1) + "' id='status-" + value[3].slice(1, -1) + "'/><input type='hidden' name='userNumber' value='" + value[5].slice(1, -1) + "' id='number-" + value[3].slice(1, -1) + "'/><h3 id='name-" + value[3].slice(1, -1) + "'>" + value[0] + "</h3><p id='mail-" + value[3].slice(1, -1) + "'>" + value[1] + "</p></div></div></div></li>";
                    });
                    document.getElementById("userlist").innerHTML = html_data;
                }
            }
        };
        xmlhttp.open("GET", "/timeline/searchUser/?q=" + str + "&user={{mail}}", true);
        xmlhttp.send();
    }
}