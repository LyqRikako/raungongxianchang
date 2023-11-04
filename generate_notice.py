import pandas as pd
from openpyxl import load_workbook
from tkinter import filedialog, messagebox
from tkinter import Tk

# 定义函数来处理Excel文件
def import_excel():
    Tk().withdraw()  # 隐藏Tkinter窗口
    file_path = filedialog.askopenfilename()  # 打开文件对话框
    if file_path:
        try:
            # 读取Excel文件
            wb = load_workbook(file_path)
            sheet = wb.active
            data = pd.DataFrame(sheet.values, columns=['选课时间', '学号', '姓名', '课程名称', '学分', '百分成绩', '五分成绩', '考试类型', '选修类型'])

            # 调用生成成绩单的函数
            generate_grade_report(data)
        except Exception as e:
            messagebox.showerror("错误", f"导入失败: {e}")
    else:
        messagebox.showinfo("提示", "请选择Excel文件。")

# 定义函数生成成绩单并打印
def generate_grade_report(data):
    # 根据姓名分组，将每个学生的成绩按照课程名称和百分成绩格式化输出
    grouped_data = data.groupby('姓名')
    for name, group in grouped_data:
        print(f"亲爱的{name}同学: 这学期的成绩如下\n")
        for index, row in group.iterrows():
            course_name = row['课程名称']
            percentage_grade = row['百分成绩']
            print(f"[{course_name}]： [{percentage_grade}] \n", end="" )
        print("\n\n希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。"\
              "如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。"\
              "我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。"\
              "请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。\n"\
              "再次恭喜您，祝您学习进步、事业成功！\n\n"\
              "教务处\n")
        print("=" * 50)  # 打印分隔线

# 简单的GUI界面
from tkinter import Tk, Button

root = Tk()
root.title("成绩单处理程序")

import_button = Button(root, text="导入成绩表", command=import_excel)
import_button.pack()

root.mainloop()
