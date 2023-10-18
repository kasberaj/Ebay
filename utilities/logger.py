import logging
import inspect


class Log_Generator:

    @staticmethod
    def log_gen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        # Gave location for logfile
        logfile = logging.FileHandler("C:\\Users\\Raj\\PycharmProjects\\CredKartNew\\Logs\\Cred.log")
        #   Set format for logs
        format = logging.Formatter("%(asctime)s | %(levelname)s | %(lineno)d | %(funcName)s | %(message)s")

        logfile.setFormatter(format)
        # Assigned file for storing logs
        logger.addHandler(logfile)
        # set level for log file
        logger.setLevel(logging.INFO)
        return logger
