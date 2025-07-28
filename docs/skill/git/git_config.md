# config
## git免密操作

使用无密码的 SSH 密钥
```shell
# -N "" 表示空密码
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
```
覆盖现有密钥（如果不再需要旧密钥）
```shell
# （-y 表示强制覆盖）
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -y
```
将公钥添加到远程仓库（GitHub/GitLab等）
```shell
cat ~/.ssh/id_ed25519.pub
```

Git Bash 仍然尝试使用旧的 RSA 密钥,确保 SSH 使用 id_ed25519 而不是 `id_rsa`
```shell
mv ~/.ssh/id_rsa ~/.ssh/id_rsa.backup  # 备份旧密钥（可选）
mv ~/.ssh/id_rsa.pub ~/.ssh/id_rsa.pub.backup
```
然后确认公钥内容：
```shell
cat ~/.ssh/id_ed25519.pub
```
将输出添加到github：登录 GitHub → Settings → SSH and GPG keys → New SSH key。
粘贴 id_ed25519.pub 的内容。

修复权限（Windows Git Bash）：
```bash
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chmod 700 ~/.ssh
```


**验证**
```shell
ssh -T git@github.com
```
成功的返回
```
Hi 你的用户名! You've successfully authenticated...
```


现在就可以成功使用git pull/push的免密操作