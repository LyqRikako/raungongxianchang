import pandas as pd
import openpyxl
def create_individual_grades(file_path):
    attachment =[]
    # 读取Excel文件
    df = pd.read_excel(file_path,header=1)
    # 按照学号分组
    grouped = df.groupby('学号')
    # 遍历分组，创建对应的成绩单Excel文件
    for student_id, group_df in grouped:
        # 创建新的DataFrame，只包含当前学生的成绩信息
        individual_df = group_df[['选课时间','学号','姓名','课程名称','学分','百分成绩', '五分成绩','考试类型','选修类型']]
        # 新建Excel文件，文件名为学号
        file_name = f'{student_id}.xlsx'
        individual_df.to_excel(file_name, index=False)
        #print(f'已创建学号为 {student_id} 的成绩单文件 {file_name}')
        attachment.append(file_name)
    return attachment
def main():
    # 总成绩单Excel文件路径
    file_path = 'C:\\Users\\12979\\Desktop\\luogu_crawler\\score.xlsx'

    # 按照学号新建对应的成绩单Excel文件
    create_individual_grades(file_path)
if __name__ == '__main__':
    main()