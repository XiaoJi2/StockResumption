from flask import Blueprint, render_template

from apps.MoodTable.model import ClMoodTable

moodtable_bp = Blueprint('moodtable', __name__, url_prefix='/moodtable')

@moodtable_bp.route('/')
def moodIndex():
    moodtable = ClMoodTable()
    infos = moodtable.getinfo()
    return render_template('MoodTable/index.html', infos=infos)