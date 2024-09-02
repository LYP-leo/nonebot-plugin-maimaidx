<div align='center'>
    <a><img src='https://raw.githubusercontent.com/Yuri-YuzuChaN/nonebot-plugin-maimaidx/master/favicon.png' width='200px' height='200px' akt='maimaidx'></a>
</div>

<div align='center'>
</div>

# nonebot-plugin-maimaidx

<a href='./LICENSE'>
    <img src='https://img.shields.io/github/license/Yuri-YuzuChaN/nonebot-plugin-maimaidx' alt='license'>
</a>
<img src='https://img.shields.io/badge/python-3.9+-blue.svg' alt='python'>

## 运行本bot需要注意的内容

1. 请尽量使用 **Python 3.9 及以上** 版本运行本bot

2. ``/static/mai/pic``目录下，需新增``buddies_bg_3.png``，尺寸为``2200*800``，裁剪自文件``buddies_bg.png``的下半部

3. ``/config.py``中，``parse_obj()``函数已弃用，可能造成bot无法运行**（代码里面已经改过了）**

4. 有些功能可能需要用到水鱼的开发者token，或者说新增的一些功能暂未对没有开发者token的情况做适配

## 和原bot相比新增的功能

+ 全分数列表
  + ``13全分数列表``：把你打过的 lv13 的所有曲子都列在一张图中（图片比较大，发送可能需要较长时间）
+ b50系列
  + ``apb50`` / ``ap+b50``：对你所有 ap / ap+ 的曲目计算 b50
  + ``fcb50`` / ``fc+b50``：对你所有 fc / fc+ 的曲目计算 b50
  + ``拟合b50``：按拟合定数计算 rating 和 b50 
  + ``丢人b50``：在 Clear 的情况下，展示完成率最低的曲目
+ 含金量
  + ``最有含金量``：展示 b50 中 拟合定数-真实定数 最高的 1 首
  + ``最没含金量``：展示 b50 中 真实定数-拟合定数 最高的 1 首
  + ``含金量``：展示 b50 中 拟合定数-真实定数 最高的 10 首
  + ``含水量``：展示 b50 中 真实定数-拟合定数 最高的 10 首
+ 猜曲绘
  + ``简单猜曲绘``：和``猜曲绘``功能一样
  + ``普通猜曲绘``：比``猜曲绘``功能展示的曲绘范围更小
  + ``困难猜曲绘``：比``普通猜曲绘``功能展示的曲绘范围更小

## QQ机器人的运行教程

### 运行 NTQQ 框架

+ 目前可用的框架：[Lagrange](https://github.com/LagrangeDev/Lagrange.Core)、[LLOneBot](https://llonebot.github.io/zh-CN/)等（2024.09.02）

### 运行NoneBot2

1. **安装脚手架**

   ``pip install nb-cli``

2. **在新的工程目录下创建项目**

   ``nb create``

   ```
   [?] 选择一个要使用的模板: bootstrap (初学者或用户)
   [?] 项目名称: mai-bot                                    # 可根据自己的需要命名
   [?] 要使用哪些适配器? OneBot V11 (OneBot V11 协议)
   [?] 要使用哪些驱动器? FastAPI (FastAPI 驱动器)
   [?] 立即安装依赖? (Y/n) Yes
   [?] 创建虚拟环境? (Y/n) Yes                          		# 可选
   [?] 要使用哪些内置插件?                                	  # 什么也不选
   ```

3. **配置环境**

+ 进入``/mai-bot``目录，激活虚拟环境，并安装插件（目的是安装环境依赖）

  ```
  .venv\Scripts\activate
  nb plugin install nonebot-plugin-maimaidx
  ```

+ 将本项目的 ``nonebot_plugin_maimaidx`` 文件夹拷贝至 ``/mai-bot`` 目录下

+ 按前文所述对 ``Phantom JS`` 和静态文件进行正确配置

+ 修改 ``.env.prod``

  ```
  # 设置静态文件路径
  MAIMAIDXPATH=path.to.static
  
  # 如有开发者TOKEN
  MAIMAIDXTOKEN=MAIMAITOKEN
  
  # 设置管理员QQ号
  SUPERUSERS=["QQ号"]
  ```

+ 修改 `pyproject.toml`

  ```
  [project]
  name = "test-bot"
  version = "0.1.0"
  description = "test-bot"
  readme = "README.md"
  requires-python = ">=3.9, <4.0"
  
  [tool.nonebot]
  adapters = [
      { name = "OneBot V11", module_name = "nonebot.adapters.onebot.v11" }
  ]
  
  plugins = ["nonebot_plugin_maimaidx"]    # 修改插件名称，使之使用本插件
  
  plugin_dirs = []
  builtin_plugins = []
  ```

4. **运行机器人**

   ```
   nb run
   ```



---- 以下为原内容 ----



## 重要更新

**2024-07-23**

1. 更新部分牌子完成表和 `SyncPlay` 图片，下载更新图片包 `Update.zip` 解压，将 `static` 复制并覆盖。**如果怕缺少图片请进行[使用方法第二步](#使用方法)**
   - [私人云盘](https://share.yuzuchan.moe/d/aria/Update.zip?sign=PFnIZpgyB_HptU-hHIQ-S_qhuuGTNDlmEEtmaEpmJlA=:0)
   - [onedrive](https://yuzuai-my.sharepoint.com/:u:/g/personal/yuzuchan_yuzuai_onmicrosoft_com/EcFTIQemNF9NlNQj8RZSdhABiV64tFi-X8-8a7JKxfEKJQ?e=P5nPnx)
2. 修复 `牌子进度` 指令 `sync` 未匹配的问题
3. 修复 `别名查歌` 指令查询到已删除的曲目时发生错误的问题

## 安装

1. 安装 `nonebot-plugin-maimaidx`

    - 使用 `nb-cli` 安装
        ``` python
        nb plugin install nonebot-plugin-maimaidx
   ```
    - 使用 `pip` 安装
        ``` python
        pip install nonebot-plugin-maimaidx
   ```
    - 使用源代码（不推荐） **需自行安装额外依赖**
        ``` git
        git clone https://github.com/Yuri-YuzuChaN/nonebot-plugin-maimaidx
        ```

2. 安装 `PhantomJS`，前往 https://phantomjs.org/download.html 下载对应平台支持

> [!WARNING]
> 未配置 `PhantomJS` 支持的Bot，在使用 `ginfo` 指令时会被强制关闭 Bot 进程

## 配置

1. 下载静态资源文件，将该压缩文件解压，且解压完为文件夹 `static`

    - [私人云盘](https://share.yuzuchan.moe/d/aria/Resource.zip?sign=LOqwqDVm95dYnkEDYKX2E-VGj0xc_JxrsFnuR1BcvtI=:0)
    - [onedrive](https://yuzuai-my.sharepoint.com/:u:/g/personal/yuzuchan_yuzuai_onmicrosoft_com/EaS3jPYdMwxGiU3V_V64nRIBk6QA5Gdhs2TkJQ2bLssxbw?e=Mm6cWY)

2. 在 `.env` 文件中配置静态文件绝对路径 `MAIMAIDXPATH`

    ``` dotenv
    MAIMAIDXPATH=path.to.static

    # 例如 windows 平台，非 "管理员模式" 运行Bot尽量避免存放在C盘
    MAIMAIDXPATH=D:\bot\static
    # 例如 linux 平台
    MAIMAIDXPATH=/root/static
    ```

3. 在 `.env` 文件夹中配置 `MAIMAIDXTOKEN`
   
    ``` dotenv
    # 如果没有 `diving-fish 查分器` 的开发者 `Token`，请直接留空
    MAIMAIDXTOKEN=
    # 如果有请填入 `Token`
    MAIMAIDXTOKEN=MAIMAITOKEN
    ```

> [!NOTE]
> 插件带有别名更新推送功能，如果不需要请私聊Bot使用 `全局关闭别名推送` 指令关闭所有群组推送

## 指令

![img](https://raw.githubusercontent.com/Yuri-YuzuChaN/nonebot-plugin-maimaidx/master/nonebot_plugin_maimaidx/maimaidxhelp.png)
