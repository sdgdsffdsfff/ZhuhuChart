#coding:utf-8
'''
@author: ZedLi
'''

from flask import Flask,request,render_template
from main.zhihuAnj  import zhihuAnj
from main.brain import Brain
from main.user import User
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        url = request.form["url"]
        user = User(url)
        results = user.start()
        return render_template('index.html',results = results,i=1)
    else:
        return render_template('index.html')

@app.route('/url',methods=['GET', 'POST'])
def zhihu():
    searchUrl = request.form["url"]
    test = zhihuAnj(searchUrl)
    ret = test.start();  
    print ret
    brain = Brain(ret)
    
    return brain.getAll()

@app.route('/qurl',methods=['POST'])
def getUserInfo():
    qurl = request.form["url"]
    print qurl
    

if __name__ == '__main__':
    app.debug = True
    app.run()