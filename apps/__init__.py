from flask import Flask

from apps.DragonAndTigerList.view import dattable_bp
from apps.MoodTable.view import moodtable_bp
from apps.Update.view import update_bp
from apps.geguzhangting.view import ggzttable_bp
from apps.panzhong.view import pztable_bp
from exts import db, bootstrap
from settings import DevelopmentConfig


def creat_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(DevelopmentConfig)
    # 初始化db
    db.init_app(app=app)
    # 初始化bootstrap
    bootstrap.init_app(app=app)
    # 注册蓝图
    app.register_blueprint(moodtable_bp)
    app.register_blueprint(dattable_bp)
    app.register_blueprint(update_bp)
    app.register_blueprint(ggzttable_bp)
    app.register_blueprint(pztable_bp)
    print(app.url_map)

    return app