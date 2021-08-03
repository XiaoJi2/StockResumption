from apps.Update.model import DATListTable


class ClDATTable():
    def __init__(self):
        pass
    def getinfo(self, time):
        dattable = DATListTable()
        datinfos = DATListTable.query.filter(DATListTable.rdatatime == time).all()
        return datinfos