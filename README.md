# log4p

Simple log module for python.

## Usage

> Install:

``` shell
pip install log4p
```

> Add to you script, eg: python a_test_file.py

``` python
#-*- coding:utf8 -*-
import log4p
logger = log4p.GetLogger(__name__)
log = logger.logger
log.debug("Hello Tianfei Hao!")
log.info("Enjoy your happy time!")
log.warning("If you have any better Suggestions, please contact Tianfei Hao at talenhao@gmail.com")
log.info("Thanks for star on github: https://github.com/talenhao/log4p")
```

## demo

```shell
[Sat Jul 13 talen@tp-arch-tianfei log4p]$ python a_test_file.py
2019-07-13 01:25:29,128 - __main__ - INFO - Enjoy your happy time!
2019-07-13 01:25:29,128 - __main__ - WARNING - If you have any better Suggestions, please contact Tianfei Hao at talenhao@gmail.com
2019-07-13 01:25:29,128 - __main__ - INFO - Thanks for star on github: https://github.com/talenhao/log4p


[Sat Jul 13 talen@tp-arch-tianfei log4p]$ ls -l *.log
-rw-r--r-- 1 talen users 1195 Jul 13 01:25 log4p-debug.log
-rw-r--r-- 1 talen users    0 Jul 13 00:58 log4p-errors.log


[Sat Jul 13 talen@tp-arch-tianfei log4p]$ python a_test_file.py
2019-07-13 01:25:29,128 DEBUG a_test_file.py +5 <module> [MainThread]: Hello Tianfei Hao!
2019-07-13 01:25:29,128 INFO  a_test_file.py +6 <module> [MainThread]: Enjoy your happy time!
2019-07-13 01:25:29,128 WARNING a_test_file.py +7 <module> [MainThread]: If you have any better Suggestions, please contact Tianfei Hao at talenhao@gmail.com
2019-07-13 01:25:29,128 INFO  a_test_file.py +8 <module> [MainThread]: Thanks for star on github: https://github.com/talenhao/log4p
```

## Config file:

1. Default config file path:

\<module dir\>/log4p.json

``` shell
~/.virtualenvs/<your pyenv>/lib/python3.7/site-packages/log4p/log4p.json
```

- In my notebook, it's in:

```shell
/home/talen/.virtualenvs/log4p/lib/python3.7/site-packages/log4p/log4p.json
```

2. You can use your own config file when invoke log4p.GetLogger(config=\<your config file path\>)

- Default config file content is:

``` json
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
        "detail": {
            "format": "%(asctime)-15s %(levelname)-5s %(filename)s +%(lineno)d %(funcName)s [%(threadName)s]: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "debug_file_handler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "detail",
            "filename": "log4p-debug.log",
            "when": "D",
            "interval": 1,
            "backupCount": 30,
            "encoding": "utf8"
        },
        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "detail",
            "filename": "log4p-errors.log",
            "maxBytes": 10485760,
            "backupCount": 2,
            "encoding": "utf8"
        }
    },
    "loggers": {
        "my_module": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": "no"
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "debug_file_handler", "error_file_handler"]
    }
}
```
