# 自动化抓取警告弹窗 
基于python3.6，selenium和PhantomJS



## windows部署

  - 需要python3.6 [python3.6](https://www.python.org/downloads/windows/)
  - 安装依赖
  - 安装pip [pip9.0](https://pypi.python.org/pypi/pip)
 
### pip安装

> windows的python不带包管理器pip，需要自行安装

解压pip.taz.gz到一个文件夹，然后用cmd进入解压文件夹，输入
```sh
 python setup.py install
```
环境变量要添加例如C:\Python36\Scripts;的路径
cmd输入
```sh
  pip --version
```
测试是否输出版本，输出配置完成
  

### 依赖包安装

文件夹内有requirements.txt依赖文件，安装方法
```python
  pip install -r requirements.txt
```

### PhantomJS

解压后会有一个文件PhantomJS.exe，添加这个文件路径进系统环境变量PATH
cmd输入
```sh
PhantomJS
```
如果显示
```
phantomjs>
````
部署成功

## 使用方法

cmd进入项目内，输入

```python
python main.py
```

## 功能和注意

> 输入的xlsx文件严格按照模板



| 序号 | 班别 | 姓名 | 性别 | 身份证 | 是否精准扶贫户 |
| ------ | ------ | ------ | ------ | ------ | ------ |
|  1  | 1401 | 张三 | 男 | XXXXXXXX |    |

screen_file文件夹内是每一个弹出窗口的网页截图，用来后面进行核对是否正确
