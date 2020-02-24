from flask import Flask
app =Flask(__name__)

@app.route('/')
def hello():
    return "欢迎大家来到我的项目"