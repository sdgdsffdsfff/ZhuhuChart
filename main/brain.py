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
        
        self.m_likeSpace = [0,100,200,300,400]
        self.m_likeNumRangeList = [0,0,0,0,0,0]
        self.m_likeValueRangeList = ["0","0-100","100-200","200-300","300-400","400以上"]
        
        self.m_thankSpace = [0,50,100,150,200]
        self.m_thankNumRangeList = [0,0,0,0,0,0]
        self.m_thankValueRangeList = ["0","0-50","50-100","100-150","150-200","200以上"]
        
        self.m_questionSpace = [0,5,10,15,20]
        self.m_questionNumRangeList = [0,0,0,0,0,0]
        self.m_questionValueRangeList = ["0","0-5","5-10","10-15","15-20","20以上"]
        
        self.m_answerSpace = [0,5,10,15,20]
        self.m_answerNumRangeList = [0,0,0,0,0,0]
        self.m_answerValueRangeList = ["0","0-5","5-10","10-15","15-20","20以上"]
        
        self.m_numberRangeList = {"like":self.m_likeNumRangeList,"thank":self.m_thankNumRangeList,"question":self.m_questionNumRangeList,"answer":self.m_answerNumRangeList}
        self.m_spaceRangeList = {"like":self.m_likeSpace,"thank":self.m_thankSpace,"question":self.m_questionSpace,"answer":self.m_answerSpace}
        
    def check(self,item,key):
        if str(item[key]).find('K') != -1:
            item[key] = item[key][:str(item[key]).find('K')] + "000"
            
        if int(item[key]) == self.m_spaceRangeList[key][0]:
            self.m_numberRangeList[key][0] = self.m_numberRangeList[key][0] + 1                       
        elif int(item[key])>self.m_spaceRangeList[key][0] and int(item[key])<=self.m_spaceRangeList[key][1]:
            self.m_numberRangeList[key][1] = self.m_numberRangeList[key][1] + 1             
        elif int(item[key])>self.m_spaceRangeList[key][1] and int(item[key])<=self.m_spaceRangeList[key][2]:
            self.m_numberRangeList[key][2] = self.m_numberRangeList[key][2] + 1              
        elif int(item[key])>self.m_spaceRangeList[key][2] and int(item[key])<=self.m_spaceRangeList[key][3]:
            self.m_numberRangeList[key][3] = self.m_numberRangeList[key][3] + 1               
        elif int(item[key])>self.m_spaceRangeList[key][3] and int(item[key])<=self.m_spaceRangeList[key][4]:
            self.m_numberRangeList[key][4] = self.m_numberRangeList[key][4] + 1               
        elif int(item[key])>self.m_spaceRangeList[key][4]:
            self.m_numberRangeList[key][5] = self.m_numberRangeList[key][5] + 1    
     
    def getAll(self):
        for k,v in self.m_data.items():
            self.check(v,"like") 
            self.check(v,"thank")
            self.check(v,"question")
            self.check(v,"answer")
        ret = {}
        ret['like_value'] = self.m_likeValueRangeList
        ret['like_num'] = self.m_likeNumRangeList
        ret['thank_value'] = self.m_thankValueRangeList
        ret['thank_num'] = self.m_thankNumRangeList
        ret['question_value'] = self.m_questionValueRangeList
        ret['question_num'] = self.m_questionNumRangeList
        ret['answer_value'] = self.m_questionValueRangeList
        ret['answer_num'] = self.m_questionNumRangeList
        return json.dumps(ret)
    def getLike(self):
        for k,v in self.m_data.items():
            if v["like"] in self.m_likeValueList:
                num = self.m_likeValueList.index(v['like'])
                self.m_likeNumList[num] = self.m_likeNumList[num] + 1
            else:
                length = len(self.m_likeNumList)
                self.m_likeNumList.append(1)
                self.m_likeValueList.append(str(v["like"]))
        print self.m_likeNumList
        print self.m_likeValueList
        ret = {}
        ret['value'] = self.m_likeValueList;
        ret['num'] = self.m_likeNumList;
        print ret
        return json.dumps(ret)
    
    def getLikeByRange(self):
        for k,v in self.m_data.items():
            #有的点赞为14k的形式
            if str(v["like"]).find('K') != -1:
               v["like"] = str(v["like"][:str(v["like"]).find('K')]) + "000"            
            if int(v["like"]) == 0:
                self.m_likeNumRangeList[0] = self.m_likeNumRangeList[0] + 1                       
            elif int(v["like"])>0 and int(v["like"])<=100:
                self.m_likeNumRangeList[1] = self.m_likeNumRangeList[1] + 1             
            elif int(v["like"])>100 and int(v["like"])<=200:
                self.m_likeNumRangeList[2] = self.m_likeNumRangeList[2] + 1              
            elif int(v["like"])>200 and int(v["like"])<=300:
                self.m_likeNumRangeList[3] = self.m_likeNumRangeList[3] + 1               
            elif int(v["like"])>300 and int(v["like"])<=400:
                self.m_likeNumRangeList[4] = self.m_likeNumRangeList[4] + 1               
            elif int(v["like"])>400:
                self.m_likeNumRangeList[5] = self.m_likeNumRangeList[5] + 1
               
        ret = {}
        ret['like_value'] = self.m_likeValueRangeList
        ret['like_num'] = self.m_likeNumRangeList
        return json.dumps(ret)
    
    def getThankByRange(self):
        for k,v in self.m_data.items():
            #有的点赞为14k的形式
            if str(v["thank"]).find('K') != -1:
               v["thank"] = str(v["thank"][:str(v["thank"]).find('K')]) + "000"            
            if int(v["thank"]) == 0:
                self.m_thankNumRangeList[0] = self.m_thankNumRangeList[0] + 1                       
            elif int(v["thank"])>0 and int(v["thank"])<=50:
                self.m_thankNumRangeList[1] = self.m_thankNumRangeList[1] + 1             
            elif int(v["thank"])>50 and int(v["thank"])<=100:
                self.m_thankNumRangeList[2] = self.m_thankNumRangeList[2] + 1              
            elif int(v["thank"])>100 and int(v["thank"])<=150:
                self.m_thankNumRangeList[3] = self.m_thankNumRangeList[3] + 1               
            elif int(v["thank"])>150 and int(v["thank"])<=200:
                self.m_thankNumRangeList[4] = self.m_thankNumRangeList[4] + 1               
            elif int(v["thank"])>200:
                self.m_thankNumRangeList[5] = self.m_thankNumRangeList[5] + 1
               
        ret = {}
        ret['thank_value'] = self.m_thankValueRangeList
        ret['thank_num'] = self.m_thankNumRangeList
        return json.dumps(ret)
    
    def getQuestionByRange(self):
        for k,v in self.m_data.items():
            #有的点赞为14k的形式
            if str(v["question"]).find('K') != -1:
               v["question"] = str(v["question"][:str(v["question"]).find('K')]) + "000"            
            if int(v["thank"]) == 0:
                self.m_questionNumRangeList[0] = self.m_questionNumRangeList[0] + 1                       
            elif int(v["question"])>0 and int(v["question"])<=5:
                self.m_questionNumRangeList[1] = self.m_questionNumRangeList[1] + 1             
            elif int(v["question"])>5 and int(v["question"])<=10:
                self.m_questionNumRangeList[2] = self.m_questionNumRangeList[2] + 1              
            elif int(v["question"])>10 and int(v["question"])<=15:
                self.m_questionNumRangeList[3] = self.m_questionNumRangeList[3] + 1               
            elif int(v["question"])>15 and int(v["question"])<=20:
                self.m_questionNumRangeList[4] = self.m_questionNumRangeList[4] + 1               
            elif int(v["question"])>20:
                self.m_questionNumRangeList[5] = self.m_questionNumRangeList[5] + 1
               
        ret = {}
        ret['question_value'] = self.m_questionValueRangeList
        ret['question_num'] = self.m_questionNumRangeList
        return json.dumps(ret)
    
    def getAnswerByRange(self):
        for k,v in self.m_data.items():
            #有的点赞为14k的形式
            if str(v["answer"]).find('K') != -1:
               v["answer"] = str(v["answer"][:str(v["answer"]).find('K')]) + "000"            
            if int(v["thank"]) == 0:
                self.m_answerNumRangeList[0] = self.m_answerNumRangeList[0] + 1                       
            elif int(v["answer"])>0 and int(v["answer"])<=5:
                self.m_answerNumRangeList[1] = self.m_answerNumRangeList[1] + 1             
            elif int(v["answer"])>5 and int(v["answer"])<=10:
                self.m_answerNumRangeList[2] = self.m_answerNumRangeList[2] + 1              
            elif int(v["answer"])>10 and int(v["answer"])<=15:
                self.m_answerNumRangeList[3] = self.m_answerNumRangeList[3] + 1               
            elif int(v["answer"])>15 and int(v["answer"])<=20:
                self.m_answerNumRangeList[4] = self.m_answerNumRangeList[4] + 1               
            elif int(v["answer"])>20:
                self.m_answerNumRangeList[5] = self.m_answerNumRangeList[5] + 1    
                           
        ret = {}
        ret['answer_value'] = self.m_questionValueRangeList
        ret['answer_num'] = self.m_questionNumRangeList
        return json.dumps(ret)
    
        