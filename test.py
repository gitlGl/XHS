#2024/02/19
from datetime import timedelta,datetime
"""时间段"""
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
c.days#2
c.seconds#37800
c.seconds / 3600#10.5
c.total_seconds() / 3600#58.5

"""时间段与时间运算"""
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))#2012-10-03 00:00:00

b = datetime(2012, 12, 21)
d = b - a
d.days#89

now = datetime.today()
print(now)#2012-12-21 14:54:43.094063
print(now + timedelta(minutes=10))#2012-12-21 15:04:43.094063

"""字符串转时间"""
date_str = "2024-02-19 08:30:00"
date_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(date_time)#2024-02-19 08:30:00


"""时间转字符串"""
date_time = datetime.now()
date_str = date_time.strftime("%Y-%m-%d %H:%M:%S")
print(date_str)#2024-02-19 16:26:36

def parse_ymd(s):
    """性能更高"""
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))