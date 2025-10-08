## 配置代理(动态ip需要日常更改)
失败
```shell
curl -I https://github.com
```
windows terminal
```shell
ipconfig
```
获得ip后直接前往服务器的
```shell
vim ~/.bashrc

export http_proxy="http://myip:7897"
export https_proxy="http://myip:7897"

source ~/.bashrc
```
7897 是代理服务器监听的端口


查看当前代理服务器ip：
```shell
huanghan@ub-server:/sda/huanghan/llama-factory/easy-dataset$ echo $http_proxy
http://10.192.19.232:7897
huanghan@ub-server:/sda/huanghan/llama-factory/easy-dataset$ echo $https_proxy
http://10.192.19.232:7897
```
## 进程
```shell
ps aux | grep python 
```
查找当前系统中所有与 python 相关的进程，并显示它们的详细信息（如进程号、用户、CPU/内存占用、启动命令等）。
1. ps aux

    - ps 是“process status”的缩写，用于显示当前系统中的进程信息。
    - a：显示所有用户的进程（而不仅仅是当前用户的）。
    - u：以用户为主的格式显示进程信息（会显示用户名、CPU 占用、内存占用等）。
    - x：显示没有控制终端的进程（比如后台进程）。
2. | grep python

|（管道符）把前面 ps aux 的输出结果传递给后面的命令。
grep python 用于筛选包含“python”关键字的行，也就是查找所有与 python 相关的进程。

，方便后续管理（如终止进程）。