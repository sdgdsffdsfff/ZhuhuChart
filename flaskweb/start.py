#coding:utf-8
'''
@author: ZedLi
'''

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/url',methods=['GET', 'POST'])
def zhihuAnj():
    print request.form
    searchUrl = request.form["url"]
    
    return searchUrl



if __name__ == '__main__':
    app.debug = True
    app.run()