from flask import Blueprint, render_template, request

from apps.geguzhangting.model import ClGZZTTable

ggzttable_bp = Blueprint('geguzhangting', __name__, url_prefix='/geguzhangting')

@ggzttable_bp.route('/', methods=['GET', 'POST'])
def geguzhangting():
    if request.method == 'POST':
        pass
    return render_template('geguzhangting/index.html')

@ggzttable_bp.route('/getdata', methods=['GET', 'POST'])
def getdata():
    if request.method == 'POST':
        pass
    time = request.args.get('time')
    dattable = ClGZZTTable()
    infos = dattable.getinfo(time)
    return render_template('geguzhangting/index.html', infos=infos)