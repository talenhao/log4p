# log4p
Simple log module for python.

Config file:
	<module dir>/log4p.json
	Default config is:
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
	            "filename": "/tmp/debug.log",
	            "when": "H",
	            "interval": 1,
	            "backupCount": 5,
	            "encoding": "utf8"
	        },
	
	        "error_file_handler": {
	            "class": "logging.handlers.RotatingFileHandler",
	            "level": "ERROR",
	            "formatter": "detail",
	            "filename": "/tmp/errors.log",
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
可以修改"filename"配置日志文件生成位置,可使用相对或绝对路径.


#Usage:
```
    Install:
        pip install log4p
    Add to you script:
        import log4p
        SCRIPT_NAME = os.path.basename(__file__)
        pLogger = log4p.GetLogger(SCRIPT_NAME, logging.DEBUG).get_l()
        pLogger.debug("Type some log.")
```
