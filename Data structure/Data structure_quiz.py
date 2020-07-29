from random import *

users = range(1, 21) # 1부터 20까지 숫자를 생성
users = list(users)
shuffle(users) # 그냥 이렇게만 해줘야 됨, users 섞어주기

users_chiken = sample(users, 1)
users.pop(users_chiken[0]) # users에서 치킨 당첨자 빼기
users_coffee = sample(users, 3)

print(" -- 당첨자 발표 -- ")
print(" 치킨 당첨자 : %s"%users_chiken[0])
print(" 커피 당첨자 : %s"%users_coffee)
print(" -- 축하합니다 -- ")

# 강사 답

users = range(1, 21)
users = list(users)
shuffle(users)

winners = sample(users, 4)

print(" -- 당첨자 발표 -- ")
print(" 치킨 당첨자 : {0}".format(winners[0]))
print(" 커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")
