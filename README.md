# log4python
一个我常用的记录日志方式.
```
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        "detail": {
            "format": "%(asctime)-15s %(levelname)-5s %(filename)s +%(lineno)d %(funcName)s [%(threadName)s]: %(message)s"
```
日志位于/tmp目录下,按日期处理.
