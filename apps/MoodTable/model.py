from apps.Update.model import MoodTable


class ClMoodTable():
    def __init__(self):
        pass
    def getinfo(self):
        moodtable = MoodTable()
        moodinfo = MoodTable.query.all()
        return moodinfo