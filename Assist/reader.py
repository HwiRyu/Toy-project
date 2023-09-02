from datetime import datetime, timedelta
import interpreter
# 현재 날짜를 가져옵니다.

today = datetime.now().strftime('%Y-%m-%d')

# 어제의 날짜를 계산합니다


def yesterday(data):
    # 데이터 문자열을 줄 단위로 분할합니다.
    lines = data.strip().split('\n')
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    today = datetime.now().strftime('%Y-%m-%d')
    # 어제의 활동을 저장할 변수를 초기화합니다.
    yesterday_activities = "Nothing"
    today_activities = "Free"

    # 데이터를 순회하면서 어제의 활동을 찾습니다.
    for line in lines:
        if yesterday in line:
            # 어제의 활동을 가져옵니다.
            y_activities = line.split("'")[1::2]  # ' 사이에 있는 내용들을 가져옵니다.
            # , 로 연결하여 문자열로 만듭니다.
            yesterday_activities = ', '.join(y_activities) if y_activities else "Nothing"
        if today in line:
            # 오늘의 활동을 가져옵니다.
            t_activities = line.split("'")[1::2]  # ' 사이에 있는 내용들을 가져옵니다.
            # , 로 연결하여 문자열로 만듭니다.
            today_activities = ', '.join(t_activities) if t_activities else "Free"
            break  # 활동을 찾았으면 반복을 종료합니다.


    return yesterday_activities, today_activities

with open('first.txt', 'r') as form:
    with open('date.txt', 'r') as date:
        form = form.read()
        data = date.read()
        youdid, youdo = yesterday(data)
        first = form.format("SpiralShot", today,youdid,youdo)

def second_data(data, nowday):
    lines = data.strip().split('\n')
    yesyesterday = (datetime.now() - timedelta(days=nowday+2)).strftime('%Y-%m-%d')
    yesterday = (datetime.now() - timedelta(days=nowday+1)).strftime('%Y-%m-%d')
    today = (datetime.now() - timedelta(days=nowday)).strftime('%Y-%m-%d')
    tomorrow = (datetime.now() - timedelta(days=nowday-1)).strftime('%Y-%m-%d')
    empty = " "
    yesyesterday_d,yesterday_d,today_d,tomorrow_d = " "," "," "," "

    for line in lines:
        if yesyesterday in line:
            yesyesterday_d = line.split("'")[1::2]  # ' 사이에 있는 내용들을 가져옵니다.
            # , 로 연결하여 문자열로 만듭니다.
            yesyesterday_d = ', '.join(yesyesterday_d)
        if yesterday in line:
            # 어제의 활동을 가져옵니다.
            yesterday_d = line.split("'")[1::2]  # ' 사이에 있는 내용들을 가져옵니다.
            # , 로 연결하여 문자열로 만듭니다.
            yesterday_d = ', '.join(yesterday_d)
        if today in line:
            # 오늘의 활동을 가져옵니다.
            today_d = line.split("'")[1::2]  # ' 사이에 있는 내용들을 가져옵니다.
            # , 로 연결하여 문자열로 만듭니다.
            today_d = ', '.join(today_d)
        if tomorrow in line:
            # 오늘의 활동을 가져옵니다.
            tomorrow_d = line.split("'")[1::2]  # ' 사이에 있는 내용들을 가져옵니다.
              # , 로 연결하여 문자열로 만듭니다.
            tomorrow_d = ', '.join(tomorrow_d)
            break  # 활동을 찾았으면 반복을 종료합니다.

    return empty, yesyesterday, yesyesterday_d, empty, yesterday, yesterday_d, "-", today, today_d, empty, tomorrow, tomorrow_d

now = 0
def super(nowday):
    with open('date.txt','r') as data:
        data = data.read()
        a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12 = second_data(data,now)
        with open('second.txt','r') as file:
            file = file.read()
            second = file.format(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)

    return second


print(super(now))

# with open('second.txt', 'r') as file:
#     with open('date.txt', 'r') as date:
#         form = file.read()
#         data = date.read()
#         second = form.format(second_data(data, 0))