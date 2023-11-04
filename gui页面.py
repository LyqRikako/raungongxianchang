import tkinter as tk
from tkinter import filedialog

def import_scores():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    # 实现导入成绩表的逻辑

def generate_notify():
    # 实现生成成绩单通知的逻辑

def send_emails():
    # 实现发送邮件的逻辑

# 创建主窗口
root = tk.Tk()
root.title("自动化学生成绩通知程序")

# 导入成绩表按钮
import_button = tk.Button(root, text="导入成绩表", command=import_scores)
import_button.pack(pady=10)

# 生成成绩单通知按钮
generate_button = tk.Button(root, text="生成成绩单通知", command=generate_notify)
generate_button.pack(pady=10)

# 发送邮件按钮
send_button = tk.Button(root, text="发送成绩单邮件", command=send_emails)
send_button.pack(pady=10)

# 启动主循环
root.mainloop()
