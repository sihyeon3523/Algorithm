# B1
# 2007년
# 7시 15분 ~ 37분

# 1 3 5 7 8 10 12 --> 31일 
# 2 --> 28일
# 4 6 9 11 --> 30일

x, y = map(int, input().split())
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

# 1월부터 12월까지 월별 일수 
calender = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = sum(calender[0:x-1]) + y
print(week[days%7-1])