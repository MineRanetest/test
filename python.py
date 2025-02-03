import tkinter as tk
from tkinter import messagebox
import subprocess
import platform

class PrecisionShutdownApp:
    def __init__(self, master):
        self.master = master
        master.title("精准关机程序")
        master.geometry("350x220")
        
        # 系统检查
        if platform.system() != "Windows":
            messagebox.showerror("错误", "本程序仅支持Windows系统")
            master.destroy()
            return

        # 初始化变量
        self.shutdown_scheduled = False
        self.remaining_seconds = 0

        # 创建界面
        self.create_widgets()

    def create_widgets(self):
        # 输入区
        input_frame = tk.Frame(self.master)
        input_frame.pack(pady=15)

        tk.Label(input_frame, text="关机倒计时（秒）:").grid(row=0, column=0, padx=5)
        self.entry = tk.Entry(input_frame, width=10)
        self.entry.grid(row=0, column=1, padx=5)

        # 按钮区
        btn_frame = tk.Frame(self.master)
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(
            btn_frame,
            text="开始关机",
            command=self.start_shutdown,
            bg="#2196F3",
            fg="white",
            width=10
        )
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.cancel_btn = tk.Button(
            btn_frame,
            text="取消关机",
            command=self.cancel_shutdown,
            bg="#FF5722",
            fg="white",
            state=tk.DISABLED,
            width=10
        )
        self.cancel_btn.pack(side=tk.LEFT, padx=5)

        # 倒计时显示
        self.countdown_label = tk.Label(
            self.master,
            text="00:00:00",
            font=("Arial", 24, "bold"),  # 修改为通用字体
            fg="#4CAF50"
        )
        self.countdown_label.pack(pady=15)

        # 状态提示
        self.status_label = tk.Label(self.master, text="", fg="#666")
        self.status_label.pack()

    def start_shutdown(self):
        # 输入验证
        try:
            seconds = int(self.entry.get())
            if seconds <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的正整数")
            self.entry.delete(0, tk.END)
            return

        # 执行关机命令
        try:
            subprocess.run(f"shutdown /s /t {seconds}", check=True, shell=True)
            self.status_label.config(text="关机计划已设置", fg="#4CAF50")
        except subprocess.CalledProcessError:
            messagebox.showerror("权限错误", "请右键以管理员身份运行本程序")
            return

        # 初始化倒计时
        self.shutdown_scheduled = True
        self.remaining_seconds = seconds
        self.toggle_buttons()
        self.update_countdown()

    def cancel_shutdown(self):
        try:
            subprocess.run("shutdown /a", check=True, shell=True)
            self.status_label.config(text="关机已取消", fg="#FF5722")
            self.shutdown_scheduled = False
            self.countdown_label.config(text="00:00:00")
            self.toggle_buttons()
        except subprocess.CalledProcessError:
            messagebox.showerror("错误", "取消关机失败")

    def update_countdown(self):
        if self.shutdown_scheduled and self.remaining_seconds > 0:
            # 转换为时:分:秒
            hours = self.remaining_seconds // 3600
            minutes = (self.remaining_seconds % 3600) // 60
            seconds = self.remaining_seconds % 60
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.countdown_label.config(text=time_str)
            
            self.remaining_seconds -= 1
            self.master.after(1000, self.update_countdown)
        elif self.shutdown_scheduled:
            self.countdown_label.config(text="00:00:00")

    def toggle_buttons(self):
        # 修正后的状态切换逻辑
        if self.shutdown_scheduled:
            self.start_btn.config(state=tk.DISABLED)
            self.cancel_btn.config(state=tk.NORMAL)
            self.entry.config(state=tk.DISABLED)
        else:
            self.start_btn.config(state=tk.NORMAL)
            self.cancel_btn.config(state=tk.DISABLED)
            self.entry.config(state=tk.NORMAL)

    def on_closing(self):
        if self.shutdown_scheduled:
            self.cancel_shutdown()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PrecisionShutdownApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
