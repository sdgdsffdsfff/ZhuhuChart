#coding:utf-8
'''
@author: ZedLi
'''

from flask import Flask,request,render_template
from main.zhihuAnj  import zhihuAnj
from main.brain import Brain
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/url',methods=['GET', 'POST'])
def zhihu():
    searchUrl = request.form["url"]
    test = zhihuAnj(searchUrl)
    ret = test.start();  
    print ret
    brain = Brain(ret)
    
    return brain.getAll()



if __name__ == '__main__':
    app.debug = True
    app.run()