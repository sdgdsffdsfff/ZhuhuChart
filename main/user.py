#coding=utf-8
'''
Created on 2015年11月12日

@author: ZedLi
'''

import urllib
import re
class User():
    def __init__(self,url):
        self.m_url = url
        
    def getHtml(self,url):
        return urllib.urlopen(url).read()
    
    #第一个参数是答案id,第二个是昵称，第三个是点赞数
    def getInfo(self,html):
        reg =re.compile(r'<div tabindex="-1"[\s\S]*?data-aid="([\s\S]*?)"[\s\S]*?<a class="author-link"[\s\S]*?>([\s\S]*?)</a>[\s\S]*?data-votecount="([\s\S]*?)"')
        results = reg.findall(html)
        return results
    
    def start(self):
        return self.getInfo(self.getHtml(self.m_url))    