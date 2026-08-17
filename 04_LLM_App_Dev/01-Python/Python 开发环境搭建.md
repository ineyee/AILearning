## 一、本机安装 Python 环境

* macOS 自带 Python 环境，通常是 3.9.x，它主要用来给系统工具用，不建议把它作为开发主环境，建议自己安装 Python 环境
  * python 解释器：用来解释执行 .py 文件
  * python 标准库：如 os 库、sys 库、json 库、datetime 库等
  * pip：包管理工具
  * venv：虚拟环境工具，可以给每个 Python 项目单独创建一个隔离的 Python 环境，以便安装该项目的三方包，这样可以避免把三方包都安装全局 Python 里，避免跟其它项目出现依赖版本冲突（Python 包管理不是靠版本区分的那种方式，所以不能在 Python 全局里安装同一个三方包的不同版本，同一个三方包只能存在一个版本）
* 这里选择下载 Python 3.12.x
* 终端里执行 `brew install python@3.12` 安装即可，默认会安装到 /usr/local/opt/python@3.12 目录（/ 代表根目录 Macintosh HD，~/ 代表当前用户目录 /Users/ineyee）

***

* 在 .bash_profile 里配置一下环境变量：export PATH="/usr/local/opt/python@3.12/libexec/bin:$PATH"
* source ~/.bash_profile 使配置生效
* 终端执行 python --version 或 python -V 来验证是否安装成功

## 二、本机安装 Anaconda

* 但是原版 Python 环境像一个毛坯房，而 Anaconda 则是一个基于 Python、面向数据分析/机器学习/深度学习/AI 的精装房，安装了 Anaconda 你可以得到：
  * Python 解释器
  * Python 标准库
  * pip
  * venv
  * **conda：包管理工具 + 虚拟环境工具**（venv + pip 进行虚拟环境和包管理，对于普通 Python 开发完全够用，但是在数据分析/机器学习/深度学习/AI 场景下可能会有各种编译错误，使用 conda 更省心。自带了一个 base 虚拟环境，默认情况下就处于这个虚拟环境下，**但是建议给每个正式 Python 项目都单独建一个虚拟环境，不要都用这个 base 虚拟环境**）
  * **自带了大量常用的数据科学三方包**
  * Jupyter Notebook：一个终端启动、浏览器 GUI 里使用的交互式 Python 编程工具，边写代码边看结果
  * Anaconda-Navigator：如果我们不想在终端里操作，可以使用这个 GUI 工具

* Anaconda 下载地址：https://www.anaconda.com/download/success
* 这里选择下载 Anaconda 26.1.1
* 下载完双击安装即可，默认会安装到 /opt/anaconda3 目录（/ 代表根目录 Macintosh HD，~/ 代表当前用户目录 /Users/ineyee）

***

* 环境变量也自动帮我们配置好了
* 终端执行 conda --version 或 conda -V 来验证是否安装成功

> // 1、创建一个新的 conda 环境，名字叫 python_basic，里面安装 python@3.13
> conda create --name python_basic python=3.13
>
> // 2、进入某个环境
> conda activate python_basic
>
> // 3、退出某个环境
> conda deactivate
>
> // 4、查看有多少个 conda 环境
> conda env list

## 三、本机安装 PyCharm

* PyCharm 下载地址：https://www.jetbrains.com/zh-cn/pycharm/download/?section=mac
* 这里选择下载 PyCharm 2025.1
* 下载完双击安装即可，macOS 上会默认安装在应用程序

***

* 激活参考，激活码可能会失效，可以更换：https://my.feishu.cn/wiki/LybRwCIPCiyyNqk66aUcwnUpnpd

* 这是一个激活工具，把它下载到桌面并解压： [jetbra.zip](../../../../Downloads/jetbra.zip) 

* 这是一个激活码

  ```
  X9MQ8ML8U7-eyJsaWNlbnNlSWQiOiJYOU1ROE1MOFU3IiwibGljZW5zZWVOYW1lIjoiY29tbXVuaXR5LXN1cHBvcnRAamV0YnJhaW5zLmNvbSIsImFzc2lnbmVlTmFtZSI6Imh0dHBzOi8vZ2l0aHViLmZscy5qZXRicmFpbnMuY29tIiwiYXNzaWduZWVFbWFpbCI6IiIsImxpY2Vuc2VSZXN0cmljdGlvbiI6IiIsImNoZWNrQ29uY3VycmVudFVzZSI6ZmFsc2UsInByb2R1Y3RzIjpbeyJjb2RlIjoiSUkiLCJmYWxsYmFja0RhdGUiOiIyMDk5LTEyLTMxIiwicGFpZFVwVG8iOiIyMDk5LTEyLTMxIiwiZXh0ZW5kZWQiOmZhbHNlfSx7ImNvZGUiOiJBQyIsImZhbGxiYWNrRGF0ZSI6IjIwOTktMTItMzEiLCJwYWlkVXBUbyI6IjIwOTktMTItMzEiLCJleHRlbmRlZCI6ZmFsc2V9LHsiY29kZSI6IkRQTiIsImZhbGxiYWNrRGF0ZSI6IjIwOTktMTItMzEiLCJwYWlkVXBUbyI6IjIwOTktMTItMzEiLCJleHRlbmRlZCI6ZmFsc2V9LHsiY29kZSI6IlBTIiwiZmFsbGJhY2tEYXRlIjoiMjA5OS0xMi0zMSIsInBhaWRVcFRvIjoiMjA5OS0xMi0zMSIsImV4dGVuZGVkIjpmYWxzZX0seyJjb2RlIjoiR08iLCJmYWxsYmFja0RhdGUiOiIyMDk5LTEyLTMxIiwicGFpZFVwVG8iOiIyMDk5LTEyLTMxIiwiZXh0ZW5kZWQiOmZhbHNlfSx7ImNvZGUiOiJETSIsImZhbGxiYWNrRGF0ZSI6IjIwOTktMTItMzEiLCJwYWlkVXBUbyI6IjIwOTktMTItMzEiLCJleHRlbmRlZCI6ZmFsc2V9LHsiY29kZSI6IkNMIiwiZmFsbGJhY2tEYXRlIjoiMjA5OS0xMi0zMSIsInBhaWRVcFRvIjoiMjA5OS0xMi0zMSIsImV4dGVuZGVkIjpmYWxzZX0seyJjb2RlIjoiUlMwIiwiZmFsbGJhY2tEYXRlIjoiMjA5OS0xMi0zMSIsInBhaWRVcFRvIjoiMjA5OS0xMi0zMSIsImV4dGVuZGVkIjpmYWxzZX0seyJjb2RlIjoiRFMiLCJmYWxsYmFja0RhdGUiOiIyMDk5LTEyLTMxIiwicGFpZFVwVG8iOiIyMDk5LTEyLTMxIiwiZXh0ZW5kZWQiOmZhbHNlfSx7ImNvZGUiOiJSQyIsImZhbGxiYWNrRGF0ZSI6IjIwOTktMTItMzEiLCJwYWlkVXBUbyI6IjIwOTktMTItMzEiLCJleHRlbmRlZCI6ZmFsc2V9LHsiY29kZSI6IlJEIiwiZmFsbGJhY2tEYXRlIjoiMjA5OS0xMi0zMSIsInBhaWRVcFRvIjoiMjA5OS0xMi0zMSIsImV4dGVuZGVkIjpmYWxzZX0seyJjb2RlIjoiUEMiLCJmYWxsYmFja0RhdGUiOiIyMDk5LTEyLTMxIiwicGFpZFVwVG8iOiIyMDk5LTEyLTMxIiwiZXh0ZW5kZWQiOmZhbHNlfSx7ImNvZGUiOiJSU1UiLCJmYWxsYmFja0RhdGUiOiIyMDk5LTEyLTMxIiwicGFpZFVwVG8iOiIyMDk5LTEyLTMxIiwiZXh0ZW5kZWQiOmZhbHNlfSx7ImNvZGUiOiJSTSIsImZhbGxiYWNrRGF0ZSI6IjIwOTktMTItMzEiLCJwYWlkVXBUbyI6IjIwOTktMTItMzEiLCJleHRlbmRlZCI6ZmFsc2V9LHsiY29kZSI6IldTIiwiZmFsbGJhY2tEYXRlIjoiMjA5OS0xMi0zMSIsInBhaWRVcFRvIjoiMjA5OS0xMi0zMSIsImV4dGVuZGVkIjpmYWxzZX0seyJjb2RlIjoiREIiLCJmYWxsYmFja0RhdGUiOiIyMDk5LTEyLTMxIiwicGFpZFVwVG8iOiIyMDk5LTEyLTMxIiwiZXh0ZW5kZWQiOmZhbHNlfSx7ImNvZGUiOiJEQyIsImZhbGxiYWNrRGF0ZSI6IjIwOTktMTItMzEiLCJwYWlkVXBUbyI6IjIwOTktMTItMzEiLCJleHRlbmRlZCI6ZmFsc2V9LHsiY29kZSI6IkRQIiwiZmFsbGJhY2tEYXRlIjoiMjA5OS0xMi0zMSIsInBhaWRVcFRvIjoiMjA5OS0xMi0zMSIsImV4dGVuZGVkIjp0cnVlfSx7ImNvZGUiOiJQREIiLCJmYWxsYmFja0RhdGUiOiIyMDk5LTEyLTMxIiwicGFpZFVwVG8iOiIyMDk5LTEyLTMxIiwiZXh0ZW5kZWQiOnRydWV9LHsiY29kZSI6IlJTIiwiZmFsbGJhY2tEYXRlIjoiMjA5OS0xMi0zMSIsInBhaWRVcFRvIjoiMjA5OS0xMi0zMSIsImV4dGVuZGVkIjp0cnVlfSx7ImNvZGUiOiJSU0MiLCJmYWxsYmFja0RhdGUiOiIyMDk5LTEyLTMxIiwicGFpZFVwVG8iOiIyMDk5LTEyLTMxIiwiZXh0ZW5kZWQiOnRydWV9LHsiY29kZSI6IlJTRiIsImZhbGxiYWNrRGF0ZSI6IjIwOTktMTItMzEiLCJwYWlkVXBUbyI6IjIwOTktMTItMzEiLCJleHRlbmRlZCI6dHJ1ZX0seyJjb2RlIjoiUFNJIiwiZmFsbGJhY2tEYXRlIjoiMjA5OS0xMi0zMSIsInBhaWRVcFRvIjoiMjA5OS0xMi0zMSIsImV4dGVuZGVkIjp0cnVlfSx7ImNvZGUiOiJQQ1dNUCIsImZhbGxiYWNrRGF0ZSI6IjIwOTktMTItMzEiLCJwYWlkVXBUbyI6IjIwOTktMTItMzEiLCJleHRlbmRlZCI6dHJ1ZX0seyJjb2RlIjoiUlNWIiwiZmFsbGJhY2tEYXRlIjoiMjA5OS0xMi0zMSIsInBhaWRVcFRvIjoiMjA5OS0xMi0zMSIsImV4dGVuZGVkIjp0cnVlfV0sIm1ldGFkYXRhIjoiMDEyMDIzMTIwOUxQQUEwMDEwMDkiLCJoYXNoIjoiVFJJQUw6MjAxNi4xIiwiZ3JhY2VQZXJpb2REYXlzIjozLCJhdXRvUHJvbG9uZ2F0ZWQiOmZhbHNlLCJpc0F1dG9Qcm9sb25nYXRlZCI6ZmFsc2V9-dtBVL2U2dlUXxVVl2pg1ZwpX3dqXYBlft78bRigYCPkmucXinFZsdSP6q30dZWgBixK5QRK449wa4EDACPaY6i2tq/Jfn7yq8KMwDe/nTulNScSvtt7Qn94fDsKOLO0icPcBW9LzqVvVMD/qX4USIOFFtTA+zsabCE0fZVr7XaS4vFiT32dbBIEaZFOSjm44fCwmyH7+1YhQozCvAUaTR8bRP4hMos3LkJNpEBxHmiHUEaWFZEHemFGu/Tr7/KjqivaXHuxFG1SKFa0cJQvcNbo/r1unvMdg2PxyEzKpItH6Pt3jWLh8ZPRoTtMWEDa66O1JHZ9Iprn/KUHErTR+pw==-MIIETzCCAjegAwIBAgIEU7kY4jANBgkqhkiG9w0BAQsFADAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBMB4XDTIyMTAxMDE2MDU0NFoXDTI0MTAxMTE2MDU0NFowHzEdMBsGA1UEAwwUcHJvZDJ5LWZyb20tMjAyMjEwMTAwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCx0QBxb4pfhYqM/RjSsvizyIncjO1EwCRgxPbKCcRFSY3ANBzS3hUdBzIxNuVbEPlnw50ItAn1iUwlyQ3QC7T+aG9E2R3IIIfEppb4F2SBi3YtgcZc3IrLgz8wa2p0iWTkkbFwnJxD4jMBfw9HDDbS5r9d9HVcPDH0rA+4nNIm7yek0wU6D77KJUWcNm7QHJfLeJAoOno+G3UIsnu7f63XRGkvdxK7L/WFzD9hCfSwZqmPZkCcrDLJTBdU4UpoJrfIoSeXZ+ssrSdQ9qY0JfUmRWvJNuUKeDBv6TI3ZCipJeZzXXafE7xD3Q57YS6KlIJEUzjZ2CRJIK3Zu5aqUTHbAgMBAAGjgZkwgZYwSAYDVR0jBEEwP4AUo562SGdCEjZBvW3gubSgUouX8bOhHKQaMBgxFjAUBgNVBAMMDUpldFByb2ZpbGUgQ0GCCQDSbLGDsoN54TAJBgNVHRMEAjAAMBMGA1UdJQQMMAoGCCsGAQUFBwMBMAsGA1UdDwQEAwIFoDAdBgNVHQ4EFgQUQ0INJl2tuM1XlTAfueTuWydc7qIwDQYJKoZIhvcNAQELBQADggIBACzJFycVHjlSCEczoAHxgtF7NG4sDcpgmLh6nrMIZpDLLGc/whCv6vpcDkBo0XvuQwmZnbpf/Ndpy4ypP2OXIw94TlfOkGKVLdHDQU8ES1HpgAtscFtNg4dyZijF4pLgiK2nbCokvHI3oWQZY3ROswrjsh0HNHWdVKooEhWt3vBpXorusNRNWbwidznxySM5aABbHrlW0+EgXuLMEHBrybLu0QenEuTFZS3E91uSa7JLpU92aQyAmZUJAhogfIvssgwnmyfnOF3csixUV6lDBCf+SUGzQbYtZd/QsGI9uUUhBbLjoZnFhVEbbOntmB4/aUvSziZnbhRAY+OhVTrNX6GtXI03cAxVBk2Kh6DE62vBW3biBGHK5ClsQGW1f5RLWhqJh0d3EP6+dsAo2P3Ic5MCuspFwSfWoK3gNhvYlr57PNrzAWhBn6Od78RMaqg+dl+GHsm5sW5mbvXpvYNukEe1RHVIONl8OTKex1U12DeS4pAIA9aQxd1vYapmNdam3rnOQbynKLYa09aDPrWO5Y+LtaCix7TBmwXPtyCxBLK4S7EZ+FE7Xz322ulpKcvLZCTKBzUH5y62xHIcSijnxJfSU0W5UCApsnwochM5S6RPuVpvyQoBR5IX3Ugjw48jpuf2TGL/INWPHQ5AjK9ZNtWAfpkYc9w+AcNAa/v6J/Ha
  ```

* 终端执行 `sh /Users/yiyi/Desktop/jetbra/scripts/uninstall.sh`

* 终端执行 `sh /Users/yiyi/Desktop/jetbra/scripts/install.sh`

* 打开 PyCharm - 左下角齿轮按钮 - Manage Licenses - Active Another Subscription - Activation code - 把激活码复制进去 - Activate - 激活时间到 2099/12/31

* 关闭 PyCharm 的自动检查更新，IntelliJ IDEA - Settings - Appearance & Behavior - System Settings - Updates - 取消勾选

***

* IDEA - New Project - Pure Python
* Location：项目所在父目录 + 项目名，/Users/yiyi/Desktop/hello-python
* Interpreter Type：解释器类型
  * Project venv：会用原版 Python 为每个项目创建一个独立的虚拟环境，不推荐
  * Base conda：所有项目都是用 Anaconda 自带的 base 虚拟环境，不推荐
  * Custom environment：我们可以用 Anaconda 为每个项目创建一个独立的虚拟环境，推荐

* Environment：Generate new（建议总是“一个项目 = 一个独立虚拟环境”，除非几个项目只是很简单的练习项目，而且依赖几乎一样）
* Type：Conda
* Python version：选择相应版本的 python
* Name：虚拟环境的名字
* Path to conda：PyCharm 要通过哪个 conda 程序来创建和管理环境
* Create（这样就创建好了项目）

## 服务器安装 Anaconda（暂时放在这里，后续移到部署章节）

开发项目时本机用 Anaconda 创建虚拟环境，把项目部署到服务器时虚拟环境不会自带到服务器，所以服务器就无法运行我们的项目，因此服务器也得安装 Anaconda 来给项目创建跟开发时一致的虚拟环境（**当然实际开发中，我们更推荐用 Docker 来部署项目，直接把项目代码和环境一起打包，这样一来服务器就不用安装 Anaconda 来创建虚拟环境了**）

* 终端执行 `uname -m` 确认服务器架构
  * 如果是 x86_64 架构，在 https://repo.anaconda.com/archive/ 找到 https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Linux-x86_64.sh 之类的脚本待用
  * 如果是 aarch64 架构，在 https://repo.anaconda.com/archive/ 找到 https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Linux-aarch64.sh 之类的脚本待用
* 终端执行 `sudo apt install -y wget curl bzip2 ca-certificates` 或 `sudo yum install -y wget curl bzip2 ca-certificates` 安装基础工具
* 终端执行 `cd /tmp` 进入临时目录
* 终端执行 `wget https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Linux-x86_64.sh` 下载官方安装包
* 终端执行 `bash Anaconda3-2025.12-2-Linux-x86_64.sh` 即可开始安装流程
  * 第一步：看到欢迎信息后按 Enter
  * 第二步：阅读协议后输入 yes
  * 第三步：选择安装路径，会提示默认安装路径 /root/anaconda3，一般直接按 Enter 就行
  * 第四步：安装快结束时会问“是否自动初始化 conda”，建议输入 yes，这一步会自动修改服务器的 shell 配置文件（~/.bashrc 或 ~/.zshrc）来为 conda 配置环境变量
  * 第五步：此时 Anaconda 建议我们安装完成后关闭并重新打开终端来时配置生效，我们也可以终端执行 `source ~/.bashrc` 或 `source ~/.zshrc` 使配置生效
* 终端执行 conda --version 或 conda -V 来验证是否安装成功
* 安装成功后，会看到命令行前面多了一个 (base)，这表示当前处于 conda 的自带的 base 环境。建议终端执行 `conda config --set auto_activate_base false` 关闭自动激活 base，以后需要用 conda 时再手动激活环境，关闭后记得终端执行 `source ~/.bashrc` 或 `source ~/.zshrc` 使配置生效

