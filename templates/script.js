function sendData() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/sendData");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            var recvData = JSON.parse(this.responseText);
            // TODO: recvData处理
        }
    };

    var data = {}// 发送data
    xhr.send(JSON.stringify(data));
}