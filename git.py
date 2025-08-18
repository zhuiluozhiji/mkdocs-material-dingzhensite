import subprocess
import sys

def run_command_interactive(command):
    """执行需要交互输入的命令"""
    try:
        print(f"执行命令: {command}")
        result = subprocess.run(command, shell=True, text=True, encoding='utf-8')
        return result.returncode == 0
    except Exception as e:
        print(f"执行命令时出错: {e}")
        return False

def run_command(command):
    """执行不需要交互的命令"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
        if result.returncode != 0:
            print(f"错误: {result.stderr}")
            return False
        if result.stdout.strip():
            print(result.stdout)
        return True
    except Exception as e:
        print(f"执行命令时出错: {e}")
        return False

def main():
    print("=== Git 自动提交推送脚本 ===")
    
    # 获取提交信息
    commit_msg = input("请输入提交信息: ")
    if not commit_msg.strip():
        print("错误：提交信息不能为空！")
        return
    
    print("\n开始执行 Git 操作...")
    '''
    # 1. Git pull (需要交互输入密码)
    print("[1/4] 正在拉取远程更新...")
    print("可能需要输入 SSH 密钥的 passphrase...")
    if not run_command_interactive("git pull"):
        print("Git pull 失败！")
        return
    '''
    # 2. Git add .
    print("[2/4] 正在添加所有更改...")
    if not run_command("git add ."):
        print("Git add 失败！")
        return
    
    # 3. Git commit
    print("[3/4] 正在提交更改...")
    if not run_command(f'git commit -m "{commit_msg}"'):
        print("Git commit 失败或没有更改需要提交")
    
    # 4. Git push (可能也需要交互输入密码)
    print("[4/4] 正在推送到远程仓库...")
    # print("可能需要输入 SSH 密钥的 passphrase...")
    # if not run_command_interactive("git push"):  # 现在我已经做了ssh免密配置了
    if not run_command("git push"):
        print("Git push 失败！")
        return
    
    print("\n✅ 所有操作完成！")

if __name__ == "__main__":
    main()