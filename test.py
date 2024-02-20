#2023/11/15
import logging
# 创建一个日志对象
logger = logging.getLogger('my_app')
print(logger.name)#"my_app"

# 设置日志级别
logger.setLevel(logging.DEBUG)
# 创建一个文件处理器，将日志记录到文件中
file_handler = logging.FileHandler('my_app.log')
file_handler.setLevel(logging.ERROR)  # 设置文件处理器的日志级别为 ERROR

# 创建一个控制台处理器，将日志输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # 设置控制台处理器的日志级别为 INFO

# 创建一个格式化器，指定日志的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 将格式化器添加到处理器
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将处理器添加到日志对象
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 记录不同级别的日志
logger.debug('This is a debug message') # 低于控制台和文件处理器的级别，不会被记录
logger.info('This is an info message')   # 高于控制台处理器的级别，会被记录到控制台
logger.warning('warning ')#高于控制台处理器和文件处理器的级别，会被记录到控制台和文件
logger.error(' error ') # 高于控制台处理器和文件处理器的级别，会被记录到控制台和文件
logger.critical('critical')#高于控制台处理器和文件处理器的级别，会被记录到控制台和文件
"""
Python提供了一组标准的日志级别，以下是Python中常用的日志级别(从低到高)：
DEBUG：最低级别的日志级别，用于调试目的。通常在开发和调试过程中使用，记录详细的调试信息。
INFO：普通的信息级别。用于确认程序正常运行的关键事件和里程碑。
WARNING：警告级别，表示存在一些非致命性的问题或潜在错误，程序仍然可以正常运行。
ERROR：错误级别，表示出现了错误，但不会导致程序立即停止。通常用于记录一些严重的问题。
CRITICAL：最高级别的日志级别，表示非常严重的错误，可能会导致程序崩溃或无法继续执行

非常抱歉，我之前的回答有误。实际上，如果将日志对象的级别设置为ERROR，
而文件处理器的级别设置为DEBUG，文件处理器会受到日志对象级别的限制，
只记录高于或等于日志对象级别的日志消息。因此，在这种情况下，
虽然文件处理器的级别是DEBUG，它仍然会受到日志对象级别的限制，
只记录ERROR级别及以上的日志消息，不会记录DEBUG和INFO级别的消息。
感谢您的指正，我之前的回答有误，希望这次能够解答清楚您的问题。
"""

#2024/02/15
import logging
import logging.config

# 通过配置文件设置全局日志配置
logging.config.fileConfig('logging.conf')#自动获取系统编码格式不能指定

# 创建日志记录器
logger = logging.getLogger('sampleLogger')

# 输出日志信息
logger.debug('This is a debug message')

#root表示全局配置
logging_config = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        }
    },
    "root": {#root表示全局配置
        "level": "DEBUG",
        "handlers": ["console"]
    }
}

logging.config.dictConfig(logging_config)

logger = logging.getLogger("my_logger")
logger.debug("Debug message")

import logging
logging.basicConfig(#简单全局配置，类似root
    filename='app.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)

#logging.conf文件中的内容
"""
[loggers]
keys=root,sampleLogger

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_sampleLogger]
level=INFO
handlers=fileHandler
qualname=sampleLogger
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=handlers.RotatingFileHandler
level=INFO
formatter=simpleFormatter
args=('example.log', 'a', 1024, 3)
#gnfdk
[formatter_simpleFormatter]
format=%(asctime)s %(levelname)s: %(message)s
datefmt=%Y-%m-%d %H:%M:%S
"""
"""
[loggers]：这个部分指定了所有的日志记录器。在这里，我们定义了两个记录器，分别为root和sampleLogger。
[handlers]：这个部分指定了所有的日志处理器。在这里，我们定义了两个处理器，分别为consoleHandler和fileHandler。
[formatters]：这个部分指定了所有的日志格式化器。在这里，我们只定义了一个名为simpleFormatter的格式化器。
[logger_root]：这个部分定义了根日志记录器的配置。在这里，我们将根日志记录器的日志级别设置为DEBUG，并将它的处理器设置为consoleHandler。
[logger_sampleLogger]：这个部分定义了名为sampleLogger的日志记录器的配置。在这里，我们将sampleLogger的日志级别设置为INFO，并将它的处理器设置为fileHandler。qualname参数指定了这个记录器的全名，propagate参数指定了这个记录器是否要向父级记录器传递日志消息。
[handler_consoleHandler]：这个部分定义了一个输出到控制台的日志处理器。在这里，我们使用内置的StreamHandler类来创建这个处理器，并将它的日志级别设置为DEBUG。formatter参数指定了这个处理器使用的格式化器，args参数指定了这个处理器需要的其他参数，比如输出流。
[handler_fileHandler]：这个部分定义了一个输出到文件的日志处理器。在这里，我们使用handlers.RotatingFileHandler类来创建这个处理器，并将它的日志级别设置为INFO。formatter参数指定了这个处理器使用的格式化器，args参数指定了这个处理器需要的其他参数，比如日志文件名和最大文件大小。

[formatter_simpleFormatter]：这个部分定义了一个名为simpleFormatter的日志格式化器。在这里，我们使用%(asctime)s、%(levelname)s和%(message)s等占位符来定义日志消息的输出格式。datefmt参数指定了时间戳的输出格式。
总体来说，这个配置文件的作用是定义了两个日志记录器、两个日志处理器和一个日志格式化器，并指定了它们之间的关系和具体的配置参数。当你在代码中调用logging.config.fileConfig()函数并传递这个配置文件的路径时，就可以使用这些配置参数来管理日志记录。
调用logging.basicConfig()会设置一些默认的日志行为，具体包括以下几个方面：
默认的日志级别： 如果没有指定level参数，那么默认的日志级别是logging.WARNING。这意味着只有达到WARNING级别或更高级别的日志消息才会被记录。如果需要记录更低级别的消息，比如DEBUG级别，就需要显式地指定level参数为logging.DEBUG。
默认的日志输出位置： 如果没有指定filename参数，日志消息将被输出到标准输出流（通常是控制台）。如果指定了filename参数，日志消息将被输出到指定的文件中。
默认的日志输出格式： 如果没有指定format参数，日志消息将以默认格式输出，包括日志级别、日志内容等信息。如果想要自定义输出格式，可以通过指定format参数来实现。
默认的日期时间格式： 如果没有指定datefmt参数，日期时间的格式将按照默认方式显示。如果需要自定义日期时间格式，可以通过指定datefmt参数来实现
如果你希望对特定的Logger进行特殊配置，你可以使用Logger对象的方法进行自定义设置，例如setLevel()、addHandler()等。这样，该Logger实例将不再受到全局配置的影响。
还可以通过json格式进行配置

"""