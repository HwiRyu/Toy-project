from datetime import datetime, timedelta

# 현재 날짜 가져오기
current_date = datetime.now() - timedelta(days = 365)

# 1년 동안의 날짜 생성
end_date = current_date + timedelta(days=1065)

# 날짜를 생성하여 리스트에 저장
date_list = []
while current_date <= end_date:
    date_list.append(current_date.strftime('%Y-%m-%d'))
    current_date += timedelta(days=1)

# 날짜를 줄로 구분하여 파일에 저장
with open('date.txt', 'w') as file:
    file.write('\n'.join(date_list))
