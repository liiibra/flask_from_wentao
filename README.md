

### 一个典型的 Flask 项目通常包括以下结构：

#### 1. 应用主目录结构：

app/: 包含整个应用程序的代码。
static/: 静态文件，如 CSS、JavaScript 和图像文件。
templates/: Flask 模板文件（Jinja2模板）。
#### 2. 主要文件和文件夹：

app/__init__.py: 初始化应用程序及其相关设置。
app/routes.py: 包含应用程序的路由和视图函数。
app/models.py: 数据模型，如果应用需要与数据库交互。
app/forms.py: 表单定义（如果应用需要用户输入）。
app/config.py: 应用程序配置参数。
app/extensions.py: Flask 扩展的初始化。
app/utils.py: 实用工具函数。
#### 3. 配置文件：

config.py: 包含不同配置（开发、生产、测试环境等）的变量。
#### 4. 其他文件：

requirements.txt: 列出项目所需的 Python 包及其版本信息。
run.py: 启动应用的入口文件。
```arduino
your_project/
    |- app/
    |   |- __init__.py
    |   |- routes.py
    |   |- models.py
    |   |- forms.py
    |   |- config.py
    |   |- extensions.py
    |   |- utils.py
    |
    |- static/
    |   |- css/
    |   |- js/
    |   |- img/
    |
    |- templates/
    |   |- index.html
    |   |- ...
    |
    |- config.py
    |- requirements.txt
    |- run.py

```


### 数据库构建
日期 测试版本 平台 通过率 测试Log路径# flask_from_wentao
