from apps.Spiders.model import Spider
from apps.Utils.model import str_of_num
from exts import db
import time, datetime



class MoodTable(db.Model):
    # 自定义表名称
    # __tablename__ = 'moodtable'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 日期
    rdatatime = db.Column(db.String(15))
    # 涨
    hongpan = db.Column(db.Integer)
    # 跌
    lvpan = db.Column(db.Integer)
    # 实际涨停
    realzhangting = db.Column(db.Integer)
    # 实际跌停
    dieting = db.Column(db.Integer)
    # 炸板
    zhaban = db.Column(db.Integer)
    # 连板
    lianban = db.Column(db.Integer)
    # 2连板
    lianban2 = db.Column(db.Integer)
    # 3连板
    liangban3 = db.Column(db.Integer)
    # 3连板个股
    liangban3gegu = db.Column(db.String(1000))
    # 3连板以上
    liangban3up = db.Column(db.Integer)
    # 3连板个股
    liangban3upgegu = db.Column(db.String(256))
    # 金额
    Total = db.Column(db.Integer)
    zhangdie = db.Column(db.Enum('涨','跌','平','休'))

class DATListTable(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 日期
    rdatatime = db.Column(db.String(15))
    # 游资姓名
    yzname = db.Column(db.String(255))
    # 股票代码
    stockcode = db.Column(db.String(15))
    # 股票名称
    stockname = db.Column(db.String(25))
    # 买入
    buy = db.Column(db.Integer)
    # 卖出
    sell = db.Column(db.Integer)

class ZhangTingListTable(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 日期
    rdatatime = db.Column(db.String(15))
    # 股票代码
    stockcode = db.Column(db.String(15))
    # 股票名称
    stockname = db.Column(db.String(25))
    # 股票简介
    jianjie = db.Column(db.String(500))
    # 板块
    bankuai = db.Column(db.String(50))
    # 首板时间
    shoubantime = db.Column(db.String(15))
    # 尾板时间
    weibantime = db.Column(db.String(15))
    # 开板次数
    kaibancount = db.Column(db.Integer)
    # 连板
    lianban = db.Column(db.Integer)
    # 市值
    shizhi = db.Column(db.Integer)
    # 换手
    huanshou = db.Column(db.Integer)
    # 同花顺涨停理由
    ztyuanyin = db.Column(db.String(1000))

class GeGuZhangTing():
    def __init__(self):
        pass
    def update(self, updata_time):
        # 涨停
        case = []
        myspider = Spider("https://flash-api.xuangubao.cn/api/pool/detail?pool_name=limit_up")
        htmljson = myspider.getJson()
        dictDate = htmljson['message']
        if dictDate == 'OK':
            dictDate = htmljson['data']
            for list in dictDate:
                # 去除ST
                if (list["stock_chi_name"].__contains__('ST')):
                    continue
                datatable = ZhangTingListTable()
                datatable.rdatatime = str(datetime.date.today())
                datatable.stockcode = list["surge_reason"]["symbol"].split('.')[0]
                datatable.stockname = list["stock_chi_name"]
                # 简介
                datatable.jianjie = list["surge_reason"]["stock_reason"]
                # 板块
                bankuailists = list["surge_reason"]["related_plates"]
                datatable.bankuai = ''
                for bankuailist in bankuailists:
                    datatable.bankuai += bankuailist["plate_name"] + ','
                # 首板时间
                time_array = time.localtime(list["first_limit_up"])
                datatable.shoubantime = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
                # datatable.shoubantime = list["first_limit_up"]
                # 尾板时间
                time_array = time.localtime(list["last_limit_up"])
                datatable.weibantime = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
                # datatable.weibantime = list["last_limit_up"]
                # 开板次数
                datatable.kaibancount = list["break_limit_up_times"]
                # 连板
                datatable.lianban = list["limit_up_days"]
                datatable.shizhi = str_of_num(list["non_restricted_capital"])
                datatable. huanshou = list["turnover_ratio"]
                case.append(datatable)
            db.session.add_all(case)
            db.session.commit()
            return True
        return False



class UpdataQingXuBiao():
    def __init__(self):
        pass
    def update(self, datatime):
        moodtable = MoodTable()
        zhangtingmood = ''
        limitupcount = 0
        limitdowncount = 0
        risecount = 0
        fallcount = 0
        brokencount = 0
        ztcount = 0
        twocount = 0
        threecount = 0
        threeupcount = 0
        threestockname = ''
        threeupstockname = ''
        # table = MoodTable.query.filter(MoodTable.rdatatime == datatime).first()
        # if( table ):
        #     return False
        # 大盘指数
        myspider = Spider("https://api-ddc-wscn.xuangubao.cn/market/trend?fields=tick_at,close_px&prod_code=000001.SS")
        htmljson = myspider.getJson()
        dictDate = htmljson['message']
        if dictDate == 'OK':
            todayshoupan = htmljson['data']['candle']['000001.SS']['lines'][-1][-1]
            yesterdayshoupan = htmljson['data']['candle']['000001.SS']['pre_close_px']
            zhishu = todayshoupan - yesterdayshoupan
            print(zhishu)
            if zhishu > 0:
                zhangtingmood = '涨'
            elif zhishu < 0:
                zhangtingmood = '跌'
            else:
                zhangtingmood = '平'

        # 涨跌停数量
        myspider.setUrl("https://flash-api.xuangubao.cn/api/market_indicator/line?fields=limit_up_count,limit_down_count")
        htmljson = myspider.getJson()
        dictDate = htmljson['message']
        if dictDate == 'OK':
            limitupcount  = htmljson['data'][-1]["limit_up_count"]
            limitdowncount = htmljson['data'][-1]["limit_down_count"]

        # 涨跌数量
        myspider.setUrl("https://flash-api.xuangubao.cn/api/market_indicator/line?fields=rise_count,fall_count")
        htmljson = myspider.getJson()
        dictDate = htmljson['message']
        if dictDate == 'OK':
            risecount = htmljson['data'][-1]["rise_count"]
            fallcount = htmljson['data'][-1]["fall_count"]

        # 炸板数量
        myspider.setUrl("https://flash-api.xuangubao.cn/api/market_indicator/line?fields=limit_up_broken_count,limit_up_broken_ratio")
        htmljson = myspider.getJson()
        dictDate = htmljson['message']
        if dictDate == 'OK':
            brokencount = htmljson['data'][-1]["limit_up_broken_count"]

        # 涨停
        myspider.setUrl("https://flash-api.xuangubao.cn/api/pool/detail?pool_name=limit_up")
        htmljson = myspider.getJson()
        dictDate = htmljson['message']
        if dictDate == 'OK':
            dictDate = htmljson['data']
            for list in dictDate:
                # 去除ST
                if (list["stock_chi_name"].__contains__('ST')):
                    continue
                ztcount += 1
                if list["limit_up_days"] == 2:
                    twocount += 1
                if list["limit_up_days"] == 3:
                    threecount += 1
                    threestockname += list["stock_chi_name"] + ','
                if list["limit_up_days"] > 3:
                    threeupcount += 1
                    threeupstockname += list["stock_chi_name"] + '(' + str(list["limit_up_days"]) + ')' ','

        moodtable.hongpan = risecount
        moodtable.rdatatime = str(datetime.date.today())
        moodtable.lvpan = fallcount
        moodtable.realzhangting = limitupcount
        moodtable.dieting = limitdowncount
        moodtable.zhaban = brokencount
        moodtable.lianban = ztcount
        moodtable.lianban2 = twocount
        moodtable.liangban3 = threecount
        moodtable.liangban3gegu = threestockname
        moodtable.liangban3up = threeupcount
        moodtable.liangban3upgegu = threeupstockname
        moodtable.Total = 0
        moodtable.zhangdie = zhangtingmood
        db.session.add(moodtable)
        db.session.commit()
        return True


class UpdataDATList():
    def __init__(self):
        pass

    def update(self, datatime):
        case = []
        # table = DATListTable.query.filter(DATListTable.rdatatime == datatime).first()
        # if (table):
        #     return False
        myspider = Spider(
            "https://hq.kaipanla.com/w1/api/index.php?a=GetYTFP_LHBDX&c=FuPanLa&PhoneOSNew=1&DeviceID=4477a863-a14e-3284-900f-8a6e71e24349&apiv=w25&")
        htmljson = myspider.getJson()
        dataok = htmljson['Date']
        if dataok:
            lists = htmljson['List']
            for list in lists:
                buylists = list['Buy']
                for buylist in buylists:
                    dattable = DATListTable()
                    dattable.rdatatime = htmljson['Date']
                    dattable.yzname = list['BName']
                    dattable.stockcode  = buylist['Sto']
                    dattable.stockname = buylist['StoN']
                    dattable.buy = buylist['Money']
                    case.append(dattable)
                    # db.session.add(dattable)
                    # db.session.commit()
                selllists = list['Sell']
                for selllist in selllists:
                    dattable = DATListTable()
                    dattable.rdatatime = str(datetime.date.today())
                    dattable.yzname = list['BName']
                    dattable.stockcode  = selllist['Sto']
                    dattable.stockname = selllist['StoN']
                    dattable.sell = selllist['Money']
                    case.append(dattable)
            db.session.add_all(case)
            db.session.commit()
            return True
        return False