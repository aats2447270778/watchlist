#coidng:utf-8
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def editor():
    #如果是post方法就返回tinymce生成html代码，否则渲染editor.html
    if request.method=='POST':
        return request.form['content']
    return render_template('editor.html')

if __name__ == '__main__':
    app.run()
