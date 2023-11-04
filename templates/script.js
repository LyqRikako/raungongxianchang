function showScore() {
    document.getElementById('score-box').classList.remove('hidden');
}

function hideScore() {
    document.getElementById('score-box').classList.add('hidden');
}


function sendEmail() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/sendData");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            var recvData = JSON.parse(this.responseText);
            // TODO: recvData处理
        }
    };

    var email = document.getElementById('email-input').value;
    if (email) {
        xhr.send(JSON.stringify(email));
        alert('成绩单已发送至 ' + email);
    } else {
        alert('请输入邮箱');
    }
}

