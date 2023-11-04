import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from importExcelAndGenarateMail import generate_emails_from_excel
import openpyxl
def send_email(sender_email, sender_password, receiver_emails, mail_subject, mail_content, attachment_path=None):
    """
    发送邮件函数
    :param sender_email: 邮件发送者账号
    :param sender_password: 邮件发送者密码，不是QQ登录密码，是开启SMTP服务生成的授权码
    :param receiver_emails: 邮件接收者账号，可以是多个，用列表表示
    :param mail_subject: 邮件主题
    :param mail_content: 邮件内容，可以是HTML格式的文本，也可以是纯文本格式
    :param attachment_path: 邮件附件路径，默认为None（即没有附件）
    """
    # 创建一个带附件的邮件实例
    message = MIMEMultipart()
    # 邮件正文
    message.attach(MIMEText(mail_content, 'html', 'utf-8'))
    # 添加附件
    if attachment_path:
        with open(attachment_path, 'rb') as f:
            attachment = MIMEApplication(f.read())
            attachment.add_header('Content-Disposition', 'attachment', filename=attachment_path.split('\\')[-1])
            message.attach(attachment)

    # 设置邮件主题、发件人和收件人
    message['Subject'] = mail_subject
    message['From'] = sender_email
    message['To'] = ', '.join(receiver_emails)
    # 发送邮件
    try:
        smtp_obj = smtplib.SMTP_SSL('smtp.qq.com', 465)
        smtp_obj.login(sender_email, sender_password)
        smtp_obj.sendmail(sender_email, receiver_emails, message.as_string())
        print('邮件发送成功！')
    except Exception as e:
        print('邮件发送失败：', e)
    finally:
        smtp_obj.quit()

