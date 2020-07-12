#Работа с логером
import logging
import shutil

MainLoger = logging.getLogger("Shedul")
MainLoger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
fh = logging.FileHandler("ShedulLogging.log")
fh.setFormatter(formatter)
MainLoger.addHandler(fh)

def loger(part):
    return logging.getLogger(MainLoger.name + "." + part)

def droplog():
    shutil.copy("ShedulLogging.log", 'LogBackup')
    reset = open("ShedulLogging.log", 'w')
    reset.close()
    MainLoger.info("Логи были обнулены")
