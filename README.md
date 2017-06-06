# 自动化抓取警告弹窗 
基于python3.6，selenium和PhantomJS



## windows部署

  - 需要python3.6 [python3.6](https://www.python.org/downloads/windows/)
  - 安装依赖
  - 部署PhantomJS [PhantomJS](http://phantomjs.org/download.html)
  - 安装tesseract
  
### 依赖包安装

文件夹内有requirements.txt依赖文件，安装方法
```python
  pip install -r requirements.txt
```

### PhantomJS

解压后bin文件夹会有一个文件PhantomJS.exe，添加这个文件路径进系统环境变量PATH
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
### tesseract-ORC安装

[官方安装文档](https://github.com/tesseract-ocr/tesseract/wiki)


## 功能和注意

> 输入的xlsx文件严格按照模板



| 序号 | 班别 | 姓名 | 性别 | 身份证 | 是否精准扶贫户 |
| ------ | ------ | ------ | ------ | ------ | ------ |
|  1  | 1401 | 张三 | 男 | XXXXXXXX |    |

screen_file文件夹内是每一个弹出窗口的网页截图，用来后面进行核对是否正确
