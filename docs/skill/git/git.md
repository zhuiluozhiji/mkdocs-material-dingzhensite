
# Git
??? bug "`git_auto.py`脚本"
    **一份`git_auto.py`脚本实现自动拉取并提交**
    ```py
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
    ```

??? success "`git.sh`脚本"

    ```bash
    #!/bin/bash
    # filepath: /home/man567/code/sfml-template/git_push.sh

    # 提示用户输入提交信息
    echo "请输入提交信息："
    read commit_message

    # 执行 Git 命令
    git add .
    git commit -m "$commit_message"
    git push origin master

    # 提示完成
    echo "代码已成功提交并推送到远程仓库！"
    ```

## 🧭 建仓库
```shell
git clone git@github.com:用户名/仓库名.git
```

而后直接
```
git add .
git commit -m "1"
git push origin master
```

??? success "`git.sh`脚本"

    ```bash
    #!/bin/bash
    # filepath: /home/man567/code/sfml-template/git_push.sh

    # 提示用户输入提交信息
    echo "请输入提交信息："
    read commit_message

    # 执行 Git 命令
    git add .
    git commit -m "$commit_message"
    git push origin master

    # 提示完成
    echo "代码已成功提交并推送到远程仓库！"
    ```
    
### 若本地仓库上传github
如果已经有本地仓库已有内容，想上传到github上某个新建仓库：

```shell
git init
git remote add origin git@github.com:zhuiluozhiji/minisql.git #添加远程

ssh -T git@github.com #检查链接

git remote -v # 检查

git add .
git commit -m "Initial commit"
git push -u origin master # -u是 --set-upstream 的简写，作用是将本地分支与远程分支建立追踪关系

# 加了-u 以后只需
# 以后只需
git push
git pull
```


## 之后的更改仅需要的操作



远程仓库 main 分支已经有提交（如：README.md），而你本地的 main 分支是空的或没有这些提交，所以你直接推送被拒绝了。

**✅ 解决方案：先拉取远程内容（合并或重建历史）
拉取远程并合并（推荐）
保持远程历史，适合你希望保留远程已有文件：**
``` bash
git pull --rebase origin main
git pull origin main
```

![](image/git/2025-07-20-09-28-38.png)




## 开发分支
查看历史提交,找到你要恢复的版本
```shell
git log --oneline
```
✅ 想创建新分支从旧版本开发
基于那个 commit 创建一个新分支
```shell
git checkout -b fix-from-old 4e5f6g7
# 创建一个新分支叫 fix-from-old,把你切换到这个旧版本上
#  -b 参数的作用是创建并切换到新分支。
```
强行回退到某个版本,会丢失未提交的更改
```shell
git reset --hard 4e5f6g7
```
在这个分支上修改和提交,推送你的分支到 GitHub远程
```shell
git push origin fix-from-old
```
改完后合并回主分支：
```bash
# 切换回主分支
git checkout main

# 拉取最新代码（确保干净）：
git pull origin main

# 合并你的新分支：(可能需要你手动操作合并选项)选蓝色/绿色模块
git merge fix-from-old

# 推送到 GitHub：
git push origin main
```



!!! question
    ```
    (data-marketplace) [dingzhen@77qq data-marketplace]$ git pull
    Enter passphrase for key : 
    There is no tracking information for the current branch.
    Please specify which branch you want to merge with.
    See git-pull(1) for details.

        git pull <remote> <branch>

    If you wish to set tracking information for this branch you can do so with:

        git branch --set-upstream-to=origin/<branch> fix-io-based-on-old
    ```
    你的 Git 报错说明：**你当前所在的分支 `fix-io-based-on-old` 没有设置上游（remote tracking）分支**，所以 Git 不知道该从哪个远程分支拉代码。

    ---

    - **💡 解决方法：设置远程跟踪分支**

    你只需要执行下面这条命令 **一次性绑定远程分支**，下次就能直接 `git pull` 了：

    ```bash
    git branch --set-upstream-to=origin/fix-io-based-on-old
    ```

    或者更明确地指定：

    ```bash
    git branch --set-upstream-to=origin/fix-io-based-on-old fix-io-based-on-old
    ```

    - **🛠️ 如果你刚创建并推送了该分支（推荐用法）**

    你可以也用这种一次性命令推送并建立 tracking：

    ```bash
    git push -u origin fix-io-based-on-old
    ```

    解释：

    * `-u`（或 `--set-upstream`）表示建立远程追踪关系
    * 之后就可以直接用 `git pull`、`git push`，不用再指定远程分支

    ---

    ✅ 之后你就可以正常使用：

    ```bash
    git pull
    git push
    ```


你不确定当前在哪个分支、工作区干不干净
```shell
git checkout 分支名 # 切换分支
git branch #查看所有本地分支
git status
```

![1753581880763](image/git/1753581880763.png)


## tag & release
本地创建tag再推送
```shell
# 1. 查看当前 commit id（可选）
git log --oneline

# 2. 在当前提交上打 tag
git tag v1.0.0

# 3. 推送 tag 到远程
git push origin v1.0.0

```

### 使用github action来自动化release（没有尝试过）










---





