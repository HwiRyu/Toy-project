from datetime import datetime, timedelta
import os
import shutil
import interpreter
# 현재 날짜를 가져옵니다.

today = datetime.now().strftime('%Y-%m-%d')
time = datetime.now().strftime('%H:%M:%S')


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

        youdolist = youdo.split(',')
        youdidlist = youdid.split(',')
        result1 = []  # 결과를 저장할 빈 리스트
        result2 = []  # 결과를 저장할 빈 리스트

        # 각 단어의 길이를 합산할 변수와 초기값 설정
        total_length1 = 0
        total_length2 = 0

        for index, word in enumerate(youdolist):
            if index == 0:
                criterion1 = 45 - len("Today, you should ")
            else:
                criterion1 = 45
            result1.append(word)
            total_length1 += len(word)

            # 단어를 결과에 추가하고 길이를 누적
            if total_length1 > criterion1:
                result1[index] = '\n' + result1[index]
                total_length1 = 0
        # 결과를 다시 문장으로 합치기
        youdo = ','.join(result1)

        for index, word in enumerate(youdidlist):
            if index == 0:
                criterion2 = 45 - len("Yesterday, you did ")
            else:
                criterion2 = 45
            result2.append(word)
            total_length2 += len(word)

            # 단어를 결과에 추가하고 길이를 누적
            if total_length2 > criterion2:
                result2[index] = '\n' + result2[index]
                total_length2 = 0
        # 결과를 다시 문장으로 합치기
        youdid = ','.join(result2)



        first = form.format("User_Name", today,youdid,youdo)

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
# a9 = 오늘 한거 목록
now = 0

def super(nowday, select = 0):
    word_length = 0

    with open('date.txt','r') as data:
        data = data.read()
        a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12 = second_data(data,now)
        with open('second.txt','r') as file:
            file = file.read()
            if select > 0 and not len(a9.replace(" ", "")) == 0 :

                A9 = a9.split(',')
                A9[select-1] = ' - '+A9[select-1].strip()
                index_end = A9[select-1]
                a9 = ",".join(A9)

                index = a9.find(index_end)
                extracted_text = a9[:index]
                # 추출된 문자열의 길이
                length = len(extracted_text)
                if length + len(index_end) > 55:
                    a9 = a9[length - (55 - len(index_end)):]
            second = file.format(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)

    return second

def backup():
    backup_folder = "backup"  # 백업 폴더 이름
    if not os.path.exists(backup_folder):
        os.mkdir(backup_folder)
    source_folder = "."  # 현재 작업 디렉토리
    file_name = "date.txt"  # 수정할 텍스트 파일 이름
    new_file_name = f"{today}_{time}.txt"

    # 원본 파일 경로
    source_file_path = os.path.join(source_folder, file_name)

    # 백업 파일 경로 (백업 폴더 안에 저장)
    backup_file_path = os.path.join(backup_folder, new_file_name)

    # 텍스트 파일 이름 수정 및 백업 폴더에 복사
    shutil.copy(source_file_path, backup_file_path)

