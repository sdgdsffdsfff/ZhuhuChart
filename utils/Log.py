#coding=utf-8
'''
Created on 2015年11月17日

@author: ZedLi
'''

import logging
import datetime

class Log():
    def __init__(self):
        format = '%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s'
        curData = datetime.date.today() - datetime.timedelta(days = 0)
        infoLogName = r'E:/workspace/ZhuhuChart/log/info_%s.log' % curData
        errorLogName = r'E:/workspace/ZhuhuChart/log/error_%s.log' % curData
        
        formatter = logging.Formatter(format)
        
        self.m_infoLogger =logging.getLogger('infoLog')
        self.m_errorLogger = logging.getLogger('errorLog')
        
        self.m_infoLogger.setLevel(logging.INFO)
        self.m_errorLogger.setLevel(logging.ERROR)
        
        infoHandler = logging.FileHandler(infoLogName,'a')
        infoHandler.setLevel(logging.INFO)
        infoHandler.setFormatter(formatter)
        
        errorHandler = logging.FileHandler(errorLogName,'a')
        errorHandler.setLevel(logging.ERROR)
        errorHandler.setFormatter(formatter)
        
        self.m_infoLogger.addHandler(infoHandler)
        self.m_errorLogger.addHandler(errorHandler)
    
    def i(self,msg):
        self.m_infoLogger.info(msg)
    def e(self,msg):
        self.m_errorLogger.error(msg)