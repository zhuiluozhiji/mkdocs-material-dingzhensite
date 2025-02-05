# mkdocs-method
## 调试
在终端或者cmd中跳转到`cd fortesting`路径下，
> 建议是cmd单开一个输入，因为INFO实时更新 

``` bash
mkdocs serve
```
`contrl+C`退出

- `git remote -v`检查所连接的远程仓库
- `git branch`查看当前分支

!!! info "note"

    我所采用的本地仓库与git仓库间的连接方式由HTTPS协议改为了SSH协议,否则默认的HTTPS协议总是在执行`git push origin main`命令时候由于链接超时而挂掉


## 修改本地文件后同步到部署站点
在终端`PS C:\Users\78100\fortesting>`路径下操作（命令行或许也是可以的）


要将本地修改的 `md` 文件同步到 GitHub 并部署到 GitHub Pages，你可以按照以下步骤操作：

### 1. **确保你的本地仓库是最新的**

首先，确认你本地的 Git 仓库是最新的，并且连接的是正确的远程仓库。

- 在本地仓库目录中，打开终端或命令行，使用 `git status` 查看当前状态：
  ```bash
  git status
  ```
  这会显示你本地的修改状态，确保你已经保存了修改。

### 2. **添加并提交修改**

你对 `.md` 文件的修改需要添加并提交到本地仓库：

- 添加修改的文件：
  ```bash
  git add .
  ```
  或者，你也可以只添加特定的文件：
  ```bash
  git add <filename>.md
  ```

- 提交修改，并写上简短的提交信息：
  ```bash
  git commit -m "更新了MD文件，修改了xxx内容"
  ```

### 3. **推送修改到 GitHub**

将本地提交的修改推送到 GitHub 仓库。你可以使用以下命令将修改推送到 GitHub：

- 推送到 `main` 分支（或者你设置的其他分支）：
  ```bash
  git push origin main
  ```

### 4. **等待 GitHub Pages 更新**

GitHub 会自动重新部署你的站点，通常几分钟内，更新就会在 GitHub Pages 上生效。你可以访问你部署站点的 URL（如 `https://username.github.io/repository-name/`）来查看更新是否成功。

### 5. **如果使用静态站点生成器（例如 MkDocs）**

如果你使用了像 **MkDocs** 这样的静态站点生成器，可能需要先生成站点内容（比如将 `.md` 文件渲染成 HTML），然后将生成的文件推送到 GitHub。

假设你使用 **MkDocs**，你通常需要：

- **构建站点**：
  ```bash
  mkdocs build
  ```

- **将生成的 `site/` 目录内容推送到 GitHub**：
  如果你使用 `gh-pages` 分支来部署站点，可以执行：
  ```bash
  git subtree push --prefix site origin gh-pages
  ```

