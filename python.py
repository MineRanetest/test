import os
import sys
import platform
import subprocess
import time

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
