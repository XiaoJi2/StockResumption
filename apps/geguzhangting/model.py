from apps.Update.model import ZhangTingListTable


class ClGZZTTable():
    def __init__(self):
        pass
    def getinfo(self, time):
        dattable = ZhangTingListTable()
        datinfos = dattable.query.filter(ZhangTingListTable.rdatatime == time).all()
        return datinfos