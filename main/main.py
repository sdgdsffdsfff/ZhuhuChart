#coding=utf-8
'''
Created on 
@author: ZedLi
'''
import threading
from zhihuAnj import zhihuAnj
from brain import Brain
import urllib2
from user import User
class ZhihuThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        url = "http://www.zhihu.com/answer/24001938"
#         url = "http://www.zhihu.com/answer/23990424/voters_profile"
#      test = zhihuAnj("http://www.zhihu.com/answer/23966524")
        test = zhihuAnj(url)
        ret = test.start();
        brain = Brain(ret)  
#         print brain.getLikeByRange()
        user = User("http://www.zhihu.com/question/29739045")
        print user.start()
        
if __name__ == '__main__':
    zhihuThread = ZhihuThread();
    zhihuThread.start()