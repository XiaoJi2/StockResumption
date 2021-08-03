from flask import Blueprint, render_template, request

from apps.DragonAndTigerList.model import ClDATTable
from apps.MoodTable.model import ClMoodTable

dattable_bp = Blueprint('longhubang', __name__, url_prefix='/longhubang')

@dattable_bp.route('/', methods=['GET', 'POST'])
def longhubang():
    if request.method == 'POST':
        pass
    return render_template('DragonAndTigerList/index.html')

@dattable_bp.route('/getdata', methods=['GET', 'POST'])
def getdata():
    if request.method == 'POST':
        pass
    time = request.args.get('time')
    dattable = ClDATTable()
    infos = dattable.getinfo(time)
    return render_template('DragonAndTigerList/index.html', infos=infos)