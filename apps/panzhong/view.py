from flask import Blueprint, render_template, request

from apps.panzhong.model import PanZhongData

pztable_bp = Blueprint('panzhongshishi', __name__, url_prefix='/panzhongshishi')

@pztable_bp.route('/', methods=['GET', 'POST'])
def panzhongshishi():
    if request.method == 'POST':
        pass
    pz_data = PanZhongData()
    news_data = pz_data.getnews()
    zb_data = pz_data.getdapanzhibo()
    dx_data = pz_data.duanxianjingling()
    ggrq_data = pz_data.gegurenqi()
    bkrq_data = pz_data.bankuairenqi()
    bkgg_data = pz_data.bankuaigegu()
    return render_template('panzhong/index.html', news=news_data, dapanzhibos=zb_data, duanxian=dx_data, gegurenqi=ggrq_data, bankuairenqi=bkrq_data, bankuaigegu=bkgg_data)
