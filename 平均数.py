import pandas as pd

# 读取Excel成绩表
df = pd.read_excel('成绩表.xlsx')

# 打印每个学生的成绩
for index, row in df.iterrows():
    print(row['姓名'], row['学号'], row['成绩'])
def analyze_scores(df, class_name):
    # 计算班级平均分
    class_scores = df.loc[df['班级'] == class_name]['成绩']
    class_mean = class_scores.mean()

    # 计算班级最高分
    class_max = class_scores.max()

    # 计算班级最低分
    class_min = class_scores.min()

    # 返回计算结果
    return {'班级': class_name, '平均分': class_mean, '最高分': class_max, '最低分': class_min}

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(from_addr, password, smtp_server, smtp_port, to_addr, subject, body):
    # 创建邮件对象
    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = Header(from_addr)
    message['To'] = Header(to_addr)
    message['Subject'] = Header(subject)

    # 发送邮件
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, message.as_string())
    server.quit()

# 主程序
if __name__ == '__main__':
    # 读取Excel成绩表
    df = pd.read_excel('成绩表.xlsx')

    # 计算班级成绩统计信息
    class1_stats = analyze_scores(df, '1班')
    class2_stats = analyze_scores(df, '2班')

    # 生成成绩单并发送邮件
    for index, row in df.iterrows():
        # 构造成绩单内容
        body = f"尊敬的{row['姓名']}同学：\n您在本次考试中的成绩为{row['成绩']}分，班级排名为第{df.loc[df['班级'] == row['班级']]['成绩'].rank(method='min', ascending=False)[index]}名。"

        # 发送邮件
        send_email('发件人邮箱账号', '发件人邮箱密码', 'SMTP服务器地址', 'SMTP服务器端口号', row['邮箱'], '成绩单', body)
