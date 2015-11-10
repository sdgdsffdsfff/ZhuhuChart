#coding:utf-8
'''
Created on 2015年11月10日

@author: ZedLi
'''

import json
class Brain():
    def __init__(self,data):
        self.m_data = data
        self.m_likeValueList = []
        self.m_likeNumList = []
        
    def getLike(self):
        for k,v in self.m_data.items():
            if v["like"] in self.m_likeValueList:
                num = self.m_likeValueList.index(v['like'])
                self.m_likeNumList[num] = self.m_likeNumList[num] + 1
            else:
                length = len(self.m_likeNumList)
                print length
                self.m_likeNumList.append(1)
                self.m_likeValueList.append(v["like"])
        print self.m_likeNumList
        print self.m_likeValueList
        ret = {}
        ret['value'] = self.m_likeValueList;
        ret['num'] = self.m_likeNumList;
        print ret
        return json.dumps(ret)