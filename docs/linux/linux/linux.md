## pacman
pacman -S 用法

```shell
# -S 表示 "Sync" - 同步/安装软件包
sudo pacman -S package_name

# 常用组合：
sudo pacman -S sfml          # 安装 sfml
sudo pacman -Sy             # 同步软件包数据库
sudo pacman -Su             # 升级所有已安装的软件包
sudo pacman -Syu            # 同步数据库并升级系统（完整系统更新）
sudo pacman -Ss search_term # 搜索软件包
sudo pacman -Si package     # 显示软件包详细信息
```

主要 pacman 操作：
- -S (Sync) - 安装/同步软件包
-  -R (Remove) - 删除软件包
- -Q (Query) - 查询已安装的软件包
- -U (Upgrade) - 从本地文件安装/升级

