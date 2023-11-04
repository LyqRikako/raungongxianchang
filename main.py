import pandas as pd
import os
from flask import Flask, render_template, request, jsonify

from importExcelAndGenarateMail import generate_emails_from_excel
from send_email import send_email
from individual import *
app = Flask(__name__, static_url_path="", static_folder="templates")


@app.route("/")
def home():
    return render_template("home.html")
@app.route("/upload", methods=["POST"])
def upload_file():
    # 获取上传的文件对象
    file = request.files.get('file')
    # 指定保存路径
    save_path = 'upload_file//'
    # 确保保存路径存在，如果不存在则创建目录
    os.makedirs(save_path, exist_ok=True)
    # 生成保存文件的完整路径
    global file_path
    file_path = os.path.join(save_path, file.filename)
    # 保存文件到指定路径
    file.save(file_path)
    # 返回响应
    return "文件上传成功！"
@app.route("/sendData", methods=["POST"])
def recv_xlsx():
    email_path = request.get_json()
    # 邮件发送者账号
    sender_email = '发件人邮箱'
    # SMTP服务生成的授权码
    sender_password = '你的授权码'
    # 邮件接收者账号
    receiver_emails = email_path
    # 邮件主题
    mail_subject = 'Python自动发送邮件测试'
    # file_path = 'score.xlsx'
    a = create_individual_grades(file_path)
    flag = 0
    for id,res in generate_emails_from_excel(file_path):
        attachment_path = a[flag]
        flag += 1
        print(attachment_path)
        # 发送邮件
        send_email(sender_email, sender_password, receiver_emails, mail_subject, res, attachment_path)
    return "邮件已发送"

if __name__ == "__main__":
    app.run(host="localhost", port=5555, debug=True, threaded=False)
