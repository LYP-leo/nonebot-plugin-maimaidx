<div align='center'>
    <a><img src='https://raw.githubusercontent.com/Yuri-YuzuChaN/nonebot-plugin-maimaidx/master/favicon.png' width='200px' height='200px' akt='maimaidx'></a>
</div>

<div align='center'>

# nonebot-plugin-maimaidx

<a href='./LICENSE'>
    <img src='https://img.shields.io/github/license/Yuri-YuzuChaN/nonebot-plugin-maimaidx' alt='license'>
</a>
<img src='https://img.shields.io/badge/python-3.8+-blue.svg' alt='python'>
</div>

## 重要更新

**2024-06-07**  

1. 更新至 `舞萌DX 2024`
2. 更换所有图片绘制，需删除除 `json` 后缀的所有文件，**请重新进行使用方法第二步**
3. 更改部分 `json` 文件名称，便于识别，具体文件如下，**请务必修改文件名，否则开关文件以及本地别名文件将不会被读取**
   - `all_alias.json`    修改为 `music_alias.json`
   - `local_alias.json`  修改为 `local_music_alias.json`
   - `chart_stats.json`  修改为 `music_chart.json`
   - `group_alias.json`  修改为 `group_alias_switch.json`
   - `guess_config.json` 修改为 `group_guess_switch.json`
4. 新增管理员私聊指令 `更新完成表`，用于更新 `BUDDiES` 版本 `双系` 牌子
5. 新增指令 `完成表`，可查询牌子完成表，例如：`祝极完成表`
6. 新增指令 `猜曲绘`
7. 查看谱面支持计算个人加分情况，指令包括 `是什么歌`，`id`
8. 指令 `mai什么` 支持随机发送推分谱面，指令中需包含 `加分`，`上分` 字样，例如：`今日mai打什么上分`
9. 修改指令 `分数列表` 和 `进度` 发送方式
10. 优化所有模块

**时间紧凑，以下实现未完成，将在后续更新跟进**  

1. 修改牌子进度为图片形式，详细各个谱面完成进度
2. 宴会场定数表
3. 新的 `help` 图片

## 安装

1. 安装 `nonebot-plugin-maimaidx`

    - 使用 `nb-cli` 安装

        ``` shell
        nb plugin install nonebot-plugin-maimaidx
        ```

    - 使用 `pip` 安装

        ``` shell
        pip install nonebot-plugin-maimaidx
        ```

    - 使用源代码安装（不推荐） **需自行安装额外依赖**

        ``` shell
        git clone https://github.com/Yuri-YuzuChaN/nonebot-plugin-maimaidx
        ```

2. 安装 `PhantomJS`，前往 <https://phantomjs.org/download.html> 下载对应平台支持

> [!WARNING]
> 未配置 `PhantomJS` 支持的Bot，在使用 `ginfo` 指令时会被强制关闭 Bot 进程

## 配置

1. 下载静态资源文件，将该压缩文件解压，且解压完为文件夹 `static` 。[下载链接](https://share.yuzuchan.moe/d/aria/Resource.zip?sign=LOqwqDVm95dYnkEDYKX2E-VGj0xc_JxrsFnuR1BcvtI=:0)
2. 在 `.env` 文件中配置静态文件绝对路径 `MAIMAIDXPATH`

   ``` dotenv
   MAIMAIDXPATH=path.to.static

   # 例如 windows 平台，非 "管理员模式" 运行Bot尽量避免存放在C盘
   MAIMAIDXPATH=D:\bot\static
   # 例如 linux 平台
   MAIMAIDXPATH=/root/static
   ```

3. 可选，如果拥有 `diving-fish 查分器` 的开发者 `Token`，在 `.env` 文件夹中配置 `MAIMAIDXTOKEN`

   ``` dotenv
   MAIMAIDXTOKEN=MAIMAITOKEN
   ```

> [!NOTE]
> 插件带有别名更新推送功能，如果不需要请私聊Bot使用 `全局关闭别名推送` 指令关闭所有群组推送

## 运行 QQ 机器人

### 运行 NTQQ 框架

由于QQ官方针对协议库的围追堵截，不断更新加密方案，目前 `go-cqhttp` 已经很难再成功运行，因此改用 `无头NTQQ` 框架。  
目前可使用的框架有 [Lagrange](https://github.com/LagrangeDev/Lagrange.Core) ，截至2024.6.17仍然可用。如该框架无法使用，可考虑更换其他框架。

### 运行 NoneBot2

本项目仅支持 **Python 3.9 以上** 版本，运行NoneBot2的方法可参考 [NoneBot官网](https://nonebot.dev/) 。  
使用脚手架运行该项目的方法可参考 [NoneBot快速上手](https://nonebot.dev/docs/quick-start) 。  

1. 安装脚手架

   ``` shell
   python -m pip install --user pipx
   python -m pipx ensurepath
   pipx install nb-cli
   ```

2. 在新的工程目录下（而非本文件夹下）创建项目

   ``` shell
   nb create
   ```

   在创建过程中，依次选择：

   ``` shell
   [?] 选择一个要使用的模板: bootstrap (初学者或用户)
   [?] 项目名称: test-bot                                   # 可根据自己的需要命名
   [?] 要使用哪些适配器? OneBot V11 (OneBot V11 协议)
   [?] 要使用哪些驱动器? FastAPI (FastAPI 驱动器)
   [?] 立即安装依赖? (Y/n) Yes
   [?] 创建虚拟环境? (Y/n) Yes                              # 可选
   [?] 要使用哪些内置插件?                                  # 什么也不选
   ```

3. 进入 `/test-bot` 目录，激活虚拟环境，安装本插件后再卸载，目的是安装 [官方](https://github.com/Yuri-YuzuChaN/nonebot-plugin-maimaidx) 提供的环境

   ```shell
   # 如果选择了“创建虚拟环境”，则需要激活虚拟环境
   .venv\Scripts\activate

   nb plugin install nonebot-plugin-maimaidx
   pip uninstall nonebot-plugin-maimaidx
   ```

4. 在 `/test-bot` 目录下执行如下操作：

   - 拷贝插件  
   将本项目的 `nonebot_plugin_maimaidx` 文件夹拷贝至 `test-bot` 目录下

   - 配置插件  
   按前文所述对 `Phantom JS` 和静态文件进行正确配置

   - 修改 `.env.prod`

     ``` dotenv
     # 设置静态文件路径
     MAIMAIDXPATH=path.to.static
     
     # 如有开发者TOKEN
     MAIMAIDXTOKEN=MAIMAITOKEN
     
     # 设置管理员QQ号
     SUPERUSERS=["QQ号"]
     ```

5. 修改 `pyproject.toml` ，令机器人使用本插件

   ``` toml
   [project]
   name = "test-bot"
   version = "0.1.0"
   description = "test-bot"
   readme = "README.md"
   requires-python = ">=3.8, <4.0"
   
   [tool.nonebot]
   adapters = [
       { name = "OneBot V11", module_name = "nonebot.adapters.onebot.v11" }
   ]

   plugins = ["nonebot_plugin_maimaidx"]    # 修改插件名称，使之使用本插件

   plugin_dirs = []
   builtin_plugins = []
   ```

6. 运行机器人

   ``` shell
   nb run
   ```

   如果运行过程中没有报错，并给出了如下提示：

   ``` plaintext
   [SUCCESS] nonebot | NoneBot is initializing...
   [INFO] nonebot | Current Env: prod
   [SUCCESS] nonebot | Succeeded to load plugin "nonebot_plugin_apscheduler"
   [SUCCESS] nonebot | Succeeded to load plugin "nonebot_plugin_maimaidx"
   [SUCCESS] nonebot | Running NoneBot...
   ...
   [INFO] nonebot_plugin_apscheduler | Scheduler Started
   [INFO] nonebot_plugin_maimaidx | 正在获取maimai所有曲目信息
   [INFO] nonebot_plugin_maimaidx | 正在获取maimai所有曲目别名信息
   [INFO] nonebot_plugin_maimaidx | 正在初始化猜歌数据
   [SUCCESS] nonebot_plugin_maimaidx | maimai数据获取完成
   ...
   [INFO] nonebot | OneBot V11 | Bot xxx(QQ号) connected
   [INFO] websockets | connection open
   ```

   说明Bot成功运行。

## 指令

如果没有开发者Token，则无法获取ap50、fc50的dx分。  
其余使用说明：

![img](https://raw.githubusercontent.com/Yuri-YuzuChaN/nonebot-plugin-maimaidx/master/nonebot_plugin_maimaidx/maimaidxhelp.png)
