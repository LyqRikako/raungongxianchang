import pandas as pd

def generate_emails_from_excel(excel_file):
    # 读取Excel文件
    grades_df = pd.read_excel(excel_file, header=1)

    # 初始化邮件内容列表
    email_contents = []

    # 遍历每个学生
    for student_id, student_grades in grades_df.groupby('学号'):
        # 获取学生姓名
        student_name = student_grades.iloc[0]['姓名']

        # 生成邮件内容
        email_content = f"亲爱的{student_name}同学:\n\n祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。\n\n"

        # 遍历每门课程
        for index, row in student_grades.iterrows():
            course_name = row['课程名称']
            course_grade = row['百分成绩']
            email_content += f"{course_name}: {course_grade}\n"

        email_content += "\n希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。\n\n再次恭喜您，祝您学习进步、事业成功！\n\n教务处"

        # 将学生姓名和邮件内容作为元组添加到列表中
        email_contents.append((student_id, email_content))

    return email_contents