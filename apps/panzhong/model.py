from apps.Spiders.model import Spider
import time, datetime

from apps.Utils.model import str_of_num


class PanZhongData():
    def __init__(self):
        pass
    def getnews(self):
        myspider = Spider("https://api.xuangubao.cn/api/pc/msgs?subjids=9,10,723,35,469,821&limit=30")
        htmljson = myspider.getJson()
        dictDate = htmljson['NewMsgs']
        datalist = []
        if dictDate:
            for list in dictDate:
                datadict = {}
                title = list['Title']
                summary = list['Summary']
                timeArray = time.localtime(list['CreatedAtInSec'])
                ZhiBodatatime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                datadict['title'] = title
                datadict['summary'] = summary
                datadict['datatime'] = ZhiBodatatime
                datalist.append(datadict)
            return datalist
        else:
            return False

    def getdapanzhibo(self):
        myspider = Spider("https://hq.kaipanla.com/w1/api/index.php?st=10&a=ZhiBoContent&apiv=w24&c=ConceptionPoint&PhoneOSNew=1&DeviceID=4477a863-a14e-3284-900f-8a6e71e24349&index=0&")
        htmljson = myspider.getJson()
        dictDate = htmljson['List']
        datalist = []
        if dictDate:
            for list in dictDate:
                zhibodict = {}
                timeArray = time.localtime(list['Time'])
                ZhiBodatatime = time.strftime("%H:%M:%S", timeArray)
                comment = list['Comment']
                stocks = list['Stock']
                stocklists = []
                for stockls in stocks:
                    stock = stockls[1]
                    increase = stockls[2]
                    stls = [stock, increase]
                    stocklists.append(stls)
                zhibodict['time'] = ZhiBodatatime
                zhibodict['comment'] = comment
                zhibodict['stock'] = stocklists
                datalist.append(zhibodict)
            return datalist
        else:
            return False

    def duanxianjingling(self):
        post_data = {
            'a': 'Radar',
            'st': '100',
            'apiv': 'w25',
            'c': 'HomeDingPan',
            'PhoneOSNew': '1',
            'DeviceID': '4477a863-a14e-3284-900f-8a6e71e24349',
            'Index': '0',
        }
        my_spider = Spider("https://hq.kaipanla.com/w1/api/index.php")
        html_json = my_spider.getPostjson(post_data)
        print(html_json)
        dict_date = html_json['list']
        data_list = []
        if dict_date:
            for dx_list in dict_date:
                dx_dict = {}
                time_array = time.localtime(dx_list['time'])
                dx_time = time.strftime("%H:%M:%S", time_array)
                stock_name = dx_list['stock_name']
                dx_status = dx_list['status']
                dx_content = dx_list['content']
                dx_dict['time'] = dx_time
                dx_dict['stock'] = stock_name
                dx_dict['status'] = dx_status
                dx_dict['content'] = dx_content
                data_list.append(dx_dict)
            return data_list
        else:
            return False

    def gegurenqi(self):
        my_spider = Spider(
            "https://hq.kaipanla.com/w1/api/index.php?Order=1&a=GetHotPHB&st=30&apiv=w25&Type=1&c=StockBidYiDong&PhoneOSNew=1&UserID=879026&DeviceID=4477a863-a14e-3284-900f-8a6e71e24349&Token=d993f4b77d9d16b9585a504e58795dbf&Index=0&")
        html_json = my_spider.getJson()
        print(html_json)
        print('-------------------------')
        dict_date = html_json['List']
        data_list = []
        if dict_date:
            for list1 in dict_date:
                ggrq_list = {}
                stock_name = list1[1]
                change = list1[3]
                increase = list1[2]
                ggrq_list = [stock_name, change, increase]
                print(ggrq_list)
                data_list.append(ggrq_list)
            return data_list
        else:
            return False

    def bankuairenqi(self):
        my_spider = Spider(
            "https://hq.kaipanla.com/w1/api/index.php?Order=1&a=RealRankingInfo&st=30&apiv=w25&Type=1&c=ZhiShuRanking&PhoneOSNew=1&DeviceID=4477a863-a14e-3284-900f-8a6e71e24349&Index=0&ZSType=7&")
        html_json = my_spider.getJson()
        dict_date = html_json['list']
        data_list = []
        if dict_date:
            for list1 in dict_date:
                bk_code = list1[0]
                bk_name = list1[1]
                bk_popularity = list1[2]
                bk_speed = list1[4]
                bk_zhuli = str_of_num(list1[6])
                bkrq_list = [bk_code, bk_name, bk_popularity, bk_speed, bk_zhuli]
                data_list.append(bkrq_list)
            return data_list
        else:
            return False

    def bankuaigegu(self):
        my_spider = Spider(
            "https://hq.kaipanla.com/w1/api/index.php?Order=1&st=30&a=ZhiShuStockList_W8&c=ZhiShuRanking&PhoneOSNew=1&old=1&DeviceID=4477a863-a14e-3284-900f-8a6e71e24349&Token=d993f4b77d9d16b9585a504e58795dbf&Index=0&apiv=w25&Type=6&UserID=879026&PlateID=801001&")
        html_json = my_spider.getJson()
        dict_date = html_json['list']
        data_list = []
        if dict_date:
            for list1 in dict_date:
                gp_code = list1[0]
                gp_name = list1[1]
                gp_zhangfu = list1[6]
                gp_zongchengjiao = list1[7]
                gp_zhuli = list1[24]
                gp_zhulijinge = list1[13]
                gp_lianban = list1[23]
                gp_bankuai = list1[4]
                bkgg_list = [gp_code, gp_name, gp_zhangfu, gp_zongchengjiao, gp_zhuli, gp_zhulijinge, gp_lianban,
                             gp_bankuai]
                data_list.append(bkgg_list)
            return data_list
        else:
            return False

