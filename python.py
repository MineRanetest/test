import turtle
import os
import sys
import platform
import subprocess
import time

def draw_concentric_circles(num_circles, start_radius, step):
    """
    绘制同心圆
    :param num_circles: 要绘制的圆的数量
    :param start_radius: 第一个圆的半径
    :param step: 每个后续圆的半径增加量
    """
    turtle.speed('fastest')  # 设置绘图速度为最快
    for i in range(num_circles):
        radius = start_radius + i * step
        turtle.penup()
        turtle.goto(0, -radius)
        turtle.pendown()
        turtle.circle(radius)
def get_shutdown_command(seconds):
    """根据操作系统返回对应的关机命令"""
    system = platform.system().lower()
    
    if system == 'windows':
        return f'shutdown /s /t {seconds}'
    elif system in ('linux', 'darwin'):  # darwin是macOS的内核名称
        mins = max(seconds // 60, 1)     # 转换为至少1分钟
        return f'shutdown -h +{mins}' if system == 'linux' else f'shutdown -h +{mins}'
    else:
        raise OSError("不支持的操作系统")

def main():
    turtle.setup(width=800, height=600)  # 设置窗口大小
    turtle.bgcolor("white")  # 设置背景颜色
    turtle.color("black")  # 设置画笔颜色
    turtle.title("Concentric Circles")  # 设置窗口标题
    num_circles = 10  # 同心圆的数量
    start_radius = 20  # 第一个圆的半径
    step = 20  # 每个圆的半径增加量
    draw_concentric_circles(num_circles, start_radius, step)
    turtle.done()  # 结束绘图
    try:
        # 获取关机延迟时间
        delay = int(input("请输入关机延迟时间（秒）: "))
        if delay < 0:
            raise ValueError("时间不能为负数")
            
        # 获取关机命令
        cmd = get_shutdown_command(delay)
        
        # 执行关机命令
        if platform.system().lower() == 'windows':
            subprocess.run(cmd, shell=True, check=True)
        else:
            subprocess.run(cmd.split(), check=True)
            
        print(f"系统将在{delay}秒后关机，若要取消可以按Ctrl+C！")
        
        # 倒计时显示
        while delay > 0:
            mins, secs = divmod(delay, 60)
            print(f"\r剩余时间: {mins:02d}:{secs:02d}", end="")
            time.sleep(1)
            delay -= 1
            
    except ValueError as e:
        print(f"错误: {e}，请输入有效的正整数")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("关机命令执行失败，请尝试用管理员/root权限运行")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n关机已取消")
        # 取消Windows关机计划
        if platform.system().lower() == 'windows':
            subprocess.run('shutdown /a', shell=True)
    except Exception as e:
        print(f"发生未知错误: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
