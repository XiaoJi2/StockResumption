from flask import Blueprint, render_template, request

from apps.panzhong.model import PanZhongData

bkgg_id = 801001

pztable_bp = Blueprint('panzhongshishi', __name__, url_prefix='/panzhongshishi')

@pztable_bp.route('/', methods=['GET', 'POST'])
def panzhongshishi():
    if request.method == 'POST':
        pass
    global bkgg_id
    pz_data = PanZhongData()
    news_data = pz_data.getnews()
    zb_data = pz_data.getdapanzhibo()
    dx_data = pz_data.duanxianjingling()
    ggrq_data = pz_data.gegurenqi()
    bkrq_data = pz_data.bankuairenqi()

    print("2", bkgg_id)
    bkgg_data = pz_data.bankuaigegu(bkgg_id)
    print(bkgg_data)
    return render_template('panzhong/index.html', news=news_data, dapanzhibos=zb_data, duanxian=dx_data, gegurenqi=ggrq_data, bankuairenqi=bkrq_data, bankuaigegu=bkgg_data)


@pztable_bp.route('/bankuaigegu', methods=['GET', 'POST'])
def bankuaigegu():
    if request.method == 'POST':
        pass
    data_id = request.args.get('id')
    pz_data = PanZhongData()
    bkgg_data = pz_data.bankuaigegu(data_id)
    global bkgg_id
    bkgg_id = data_id
    print("1", bkgg_id)
    return bkgg_data