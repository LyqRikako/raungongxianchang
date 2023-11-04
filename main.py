import pandas as pd
from flask import Flask, render_template, request, jsonify

from importExcelAndGenarateMail import generate_emails_from_excel
from send_email import send_email

app = Flask(__name__, static_url_path="", static_folder="templates")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/sendData", methods=["POST"])
def recv_xlsx():
    email_path = request.get_json()
    # 邮件发送者账号
    sender_email = '1297963210@qq.com'
    # 邮件发送者密码，不是QQ登录密码，是开启SMTP服务生成的授权码
    sender_password = 'rkcgtvcmehmfffgi'
    # 邮件接收者账号，可以是多个，用列表表示
    receiver_emails = ['1297963210@qq.com']
    # 邮件主题
    mail_subject = 'Python自动发送邮件测试'

    # 邮件附件路径
    attachment_path = 'score.xlsx'

    # TODO: xlsx 文件格式转换

    for id, res in generate_emails_from_excel(attachment_path):
        # 发送邮件
        send_email(email_path, sender_password, receiver_emails, mail_subject, res, attachment_path)


if __name__ == "__main__":
    app.run(host="localhost", port=5555, debug=True, threaded=False)
