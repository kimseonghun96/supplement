'''
n = 0
while n<3:
    print(n)
    n = n+1

print(n)
'''

#내장함수 예시
'''
def 함수이름():(띄어쓰기x, 한글x, 되도록 소문자, 특수문자x)
->[계산값] return 값(필수x) / print() -> 출력
'''

'''
#근의 공식
(-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
(-b - (b**2 - 4*a*c)**(1/2)) / (2*a)
'''
#딕셔너리를 활용하여 평균 구하기

'''lunch = {'슬로우캘리' : 12000, '잭슨피자' : 8000}

    a = lunch('슬로우캘리') #12000
    b = lunch['잭슨피자'] #8000

sum_lunch = a + b'''
         
        

#print('{}. {}' .format(idx, value))

#윤년 판단
year = int(input()) 
if ((year % 4 == 0) & (year % 100 == 0)!= 0) or (year % 400 ==0):
    print('윤년입니다.')
else:
    print('윤년이 아닙니다.')

'''
a = int(input()) 
def leap_year(year):
    if ((year % 4 == 0) & (year % 100 == 0)!= 0) or (year % 400 ==0):
      return True
    else:
      return False

answer = leap_year(a)
'''
'''
def leap_year2(year):
    import calendar
    calendar.isleap(year)
    if calendar .isleap(year):
        print('윤년입니다.')
    else:
        print('윤년이 아닙니다.')'''

