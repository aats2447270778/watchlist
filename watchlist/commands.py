import click
from watchlist import app, db
from watchlist.models import User, Movie


# 自定义initdb
@app.cli.command()
@click.option('--drop', is_flag=True, help='删除之后再创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库')


# 自定义命令forge，把数据写入数据库
@app.cli.command()
def forge():
    db.create_all()
    name = "Bruce"
    movies = [
        {'title': '杀破狼','content':"1" ,'author':'1','pubdate': '2003'},
        {'title': '杀破狼','content':"1" ,'author':'1','pubdate': '2003'},
        {'title': '杀破狼','content':"1" ,'author':'1','pubdate': '2003'},
        {'title': '杀破狼','content':"1" ,'author':'1','pubdate': '2003'},

    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], content=m['content'], author=m['author'],pubdate=m['pubdate'])
        db.session.add(movie)
    db.session.commit()
    click.echo('数据导入完成')


# 生成admin账号的函数
@app.cli.command()
@click.option('--username', prompt=True, help="用来登录的用户名")
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help="用来登录的密码")
def admin(username, password):
    db.create_all()
    user = User.query.first()
    if user is not None:
        click.echo('更新用户')
        user.username = username
        user.set_password(password)
    else:
        click.echo('创建用户')
        user = User(username=username, name="雷洛")
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('创建管理员账号完成')