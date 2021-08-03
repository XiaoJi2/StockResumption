from flask import Blueprint, render_template, request

from apps.Update.model import UpdataQingXuBiao, UpdataDATList, GeGuZhangTing

update_bp = Blueprint('update', __name__, url_prefix='/update')

@update_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('Update/index.html')

@update_bp.route('/update', methods=['GET', 'POST'])
def getdata():
    if request.method == 'POST':
        pass
    time = request.args.get('time')
    qingxu = UpdataQingXuBiao()
    isok = qingxu.update(time)
    datlist = UpdataDATList()
    datlist.update(time)
    geguzhangtinglist = GeGuZhangTing()
    geguzhangtinglist.update(time)
    if isok:
        return render_template('Update/index.html')
    else:
        return "数据已经更新"

