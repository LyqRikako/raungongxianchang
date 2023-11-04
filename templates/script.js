function FileUpload() {
  // 获取文件输入框元素
  var fileInput = document.getElementById('fileInput');
  // 创建FormData对象
  var formData = new FormData();
  // 将文件添加到FormData对象
  formData.append('file', fileInput.files[0]);
  // 创建XMLHttpRequest对象
  var xhr = new XMLHttpRequest();
  // 设置请求方法和URL
  xhr.open("POST", "/upload", true);
  // 监听上传完成事件
  xhr.onload = function() {
    if (xhr.status === 200) {
      alert('文件上传成功');
    } else {
      alert('请选择要上传的文件')
    }
  };

  // 发送请求
  xhr.send(formData);
}

function sendEmail() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/sendData");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
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

