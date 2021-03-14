import datetime

from about_user import get_id
from summarized_sqlite import exec, select


# タスクを追加する
def add_task(form):
    title = form.get('title', '')
    if title == '':
        msg = 'タイトルが未記入です'
        return False, msg
    memo = form.get('memo', '')
    now = get_datetime_now()
    year = form.get('year', '')
    month = form.get('month', '')
    day = form.get('day', '')
    hour = form.get('hour', '')
    minute = form.get('minute', '')
    deadline = '{}/{}/{} {}：{}'.format(year, month, day, hour, minute)
    user_name = get_id()
    msg = None
    task_id = exec('INSERT INTO tasks (user_name, title, memo, start, deadline) VALUES(?, ?, ?, ?, ?)',
                   user_name, title, memo, now, deadline)
    return task_id, msg


def get_datetime_now():
    now = datetime.datetime.now()
    return "{0:%Y/%m/%d %H：%M}".format(now)  # 0:は何番目の要素に適応するか指定する
