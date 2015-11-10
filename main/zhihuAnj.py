# -*- coding: utf-8 -*-  

import urllib
import json
import re
from flaskweb.start import zhihuAnj

class zhihuAnj():

    def __init__(self,url):
        self.m_url = url;
        
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
        next = jsonRet['paging']['next']
        follows = next.split('follows=')
        print follows[1]
        return total,follows[1]

    
    def getPayLoad(self,total,offset,follows):
        url = self.m_url + "/voters_profile?total="+str(total)+"&offset="+str(offset)+"&follows="+follows;
        html = self.getHtml(url)
        try:
            jsonRet = json.loads(html)
        except Exception,e:
            print e
        payLoad = jsonRet['payload']
        return payLoad
        
    def anjPayLoad(self,payLoad):
#         reg = re.compile('r[\s\S]*?<div class="author ellipsis">[\s\S]*?>([\s\S]*?)</a>[\s\S]*?<span>([\s\S]*?)</span>[\s\S]*?<span>([\s\S]*?)</span>[\s\s]*?<a[\s\S]*?>([\s\S]*?)</a>[\s\S]*?target="_blank">([\s\S]*?)</a>')
        reg = re.compile(r'<[^>]+>', re.S)
        result = reg.sub('',payLoad)
#         return result.replace("\r\n"," ");
        return result.split()
    
    def start(self):
#         ȡtotal,follow
        total,follows = self.getInfo(self.m_url+"/voters_profile")
        offsets = total/10;
        for i in range(offsets):
            payLoad = self.getPayLoad(total, 10*i, follows)
            for s in payLoad:
                result = self.anjPayLoad(s)
#                 print result
                if len(result)!=0:
                    try:
                        print result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9]
                    except Exception,e:
                        print result
#             print len(result)
        
# if __name__ == '__main__':
#      url = "http://www.zhihu.com/answer/23990424"
# #      test = zhihuAnj("http://www.zhihu.com/answer/23966524")
#      test = zhihuAnj(url)
#      test.start();  
#         
        