中国象棋棋谱爬虫脚本
====
项目简介
----
    基于Python Selemium的谷歌浏览器爬中国象棋棋谱的脚本
    爬的网站是东萍象棋，通过对JS文件的反编译实现对加密字符串解密成象棋步骤。
    
项目依赖
----
- Python 3.6
- Selemium
- Chrome核心

项目文件
----
    - jiemi.py 是对东平象棋返回的加密字符串进行解密
    - main.py 是在当前文件夹下自动生成象棋棋谱

爬虫对象
----
[东萍象棋](http://www.dpxq.com)
