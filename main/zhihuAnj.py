# -*- coding: utf-8 -*-  

import urllib
from json import JSONDecoder,JSONEncoder
import json
from bs4 import BeautifulSoup
from utils.Log import Log
class zhihuAnj():

    def __init__(self,url):
        self.m_url = url
        self.m_ret = dict()
        self.m_log = Log()
        
    def getHtml(self,url):
#         url = "http://www.zhihu.com/answer/23966524"
#         url = self.url + "/voters_profile"
        html = urllib.urlopen(url).read()
        return html;
    
    def getInfo(self,url):
        #
        html = self.getHtml(url);
        print html
        jsonRet = json.loads(html);
        #
        total = jsonRet['paging']['total']
        #
        if int(total)>10:
            next = jsonRet['paging']['next']
            follows = next.split('follows=')
            print follows[1]
            return total,follows[1]
        else:
            return total,None

    
    def getPayLoad(self,total,offset,follows):
        if follows != None:
            url = self.m_url + "/voters_profile?total="+str(total)+"&offset="+str(offset)+"&follows="+follows
        else:
            url = self.m_url + "/voters_profile"
            
        html = self.getHtml(url)
        try:
            jsonRet = json.loads(html)
        except Exception,e:
            self.m_log.e(e)
            return
        payLoad = jsonRet['payload']
        return payLoad
        
    def anjPayLoad(self,payLoad):
#         reg = re.compile(r'<[^>]+>', re.S)
#         result = reg.sub('',payLoad)
#         print payLoad
        soup = BeautifulSoup(payLoad)
        name = soup.find('a',class_='zg-link')
        info = soup.find('span',class_='bio hidden-phone')
        status = soup.find('ul',class_='status')
        nameStr = None
        infoStr = None
        like = None
        thank = None
        question = None
        answer = None
        if name!=None:
            nameStr = name.string
        else:
            nameStr = "知乎用户"
            
        if info:
            infoStr = info.string
        else:
            infoStr = ""
            
        if status:
            statusStr = (status.text).split()
            like = statusStr[0]
            thank = statusStr[2]
            question = statusStr[4]
            answer = statusStr[6]
        else:
            like = 0
            thank = 0
            question = 0
            answer = 0
        
        result = {'name':nameStr,'info':infoStr,'like':like,'thank':thank,'question':question,'answer':answer}
        return result
    
    def appendDic(self,result):
     
        length = len(self.m_ret)
        self.m_ret[length] = result
        return self.m_ret
        
    def start(self):
        total,follows = self.getInfo(self.m_url+"/voters_profile")
        offsets = total/10;
        for i in range(offsets):
            payLoad = self.getPayLoad(total, 10*i, follows)
            for s in payLoad:
                result = self.anjPayLoad(s)
                self.appendDic(result)
        return self.m_ret      
        