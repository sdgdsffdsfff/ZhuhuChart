#coding=utf-8
'''
@author: ZedLi
'''

from flask import Flask,request,render_template
from main.zhihuAnj  import zhihuAnj
from main.brain import Brain
from main.user import User
from utils.Log import Log
import os
import time
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        startTime = time.time()
        url = request.form["url"]
        user = User(url)
        results = user.start() 
        log = Log()
        log.i("url:"+url + "  getUserInfo Time:"+str(time.time()-startTime))
        return render_template('index.html',results = results)
    else:
        return render_template('index.html')

@app.route('/url',methods=['GET', 'POST'])
def zhihu():
    log = Log() 
    startTime = time.time()
    searchUrl = request.form["url"]
    test = zhihuAnj(searchUrl)
    ret = test.start();  
    brain = Brain(ret)
    results = brain.getAll()
    log.i("url:"+searchUrl + "  getAll Time:"+str(time.time()-startTime))
    return results

@app.route('/qurl',methods=['POST'])
def getUserInfo():
    qurl = request.form["url"]
    print qurl
    

if __name__ == '__main__':
    app.debug = True
    app.run()