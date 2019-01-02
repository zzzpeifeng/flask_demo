from flask  import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,static_folder="static",template_folder="templates")

manager = Manager(app)
from users import users_blu
app.register_blueprint(users_blu)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/book_flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

migrate = Migrate(app,db)

#添加命令
manager.add_command("db",MigrateCommand)

class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    user = db.relationship('User', backref='role')

    #repr()方法显示一个可读字符串，
    def __repr__(self):
        return 'Role:'.format(self.name)

#定义用户
class User(db.Model):
    __talbe__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    #设置外键
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:'.format(self.username)



@app.route("/")
def index():
    return "hello "


if __name__ == '__main__':
    manager.run()