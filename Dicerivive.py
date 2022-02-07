import random
dex=10
a=0
print('회피주사위') 
a=random.randint(1,100)
b=a+dex
print(f'{a}+{dex}(보정)={b}')
if(b>=50):print('회피 성공')
else:print('회피 실패')
a=random.randint(1,100)
b=a+dex
print(f'{a}+{dex}(보정)={b}')
if(b>=50):print('회피 성공')
else:print('회피 실패')


