from apps import creat_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from exts import db
from apps.Update.model import MoodTable  # 很重要，不然创建不了数据库
from apps.Update.model import DATListTable, ZhangTingListTable

app = creat_app()

manager = Manager(app=app)

migrate = Migrate(app=app, db=db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
