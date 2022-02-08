import random
dex=0
Hp=0
Luk=0
Str=0
Sdice=0
Ldice=0
Hdice=0
Ddice=0
Name=input("주인공의 이름을 입력해주세요:")
print(f'{Name} 의 능력치')
print('힘')
Str=random.randint(1,100)
print(Str)
if(Str>95):
    Sdice=20
    print(f'{Name} 의 힘은 Ex등급으로 힘에 관련된 주사위에 20의 보정이 붙습니다.')
if(Str<94 and 80<Str):
    Sdice=10
    print(f'{Name} 의 힘은 A등급으로 힘에 관련된 주사위에 10의 보정이 붙습니다.')
if(Str<79 and 70<Str):
    Sdice=5
    print(f'{Name} 의 힘은 B등급으로 힘에 관련된 주사위에 5의 보정이 붙습니다.')
if(Str<69 and 40<Str):
    Sdice=3
    print(f'{Name} 의 힘은 C등급으로 힘에 관련된 주사위에 3의 보정이 붙습니다.')
if(Str<39 and 20<Str):
    Sdice=-3
    print(f'{Name} 의 힘은 D등급으로 힘에 관련된 주사위에 -3의 보정이 붙습니다.')
if(Str<19 and 0<Str):
    Sdice=-5
    print(f'{Name} 의 힘은 E등급으로 힘에 관련된 주사위에 -5의 보정이 붙습니다.')
print(Sdice)
Lck=random.randint(1,100)
print('운')
print(Lck)
if(Lck>95):
    Ldice=20
    print(f'{Name} 의 운은 Ex등급으로 힘에 관련된 주사위에 20의 보정이 붙습니다.')
if(Lck<94 and 80<Lck):
    Ldice=10
    print(f'{Name} 의 운은 A등급으로 힘에 관련된 주사위에 10의 보정이 붙습니다.')
if(Lck<79 and 70<Lck):
    Ldice=5
    print(f'{Name} 의 운은 B등급으로 힘에 관련된 주사위에 5의 보정이 붙습니다.')
if(Lck<69 and 40<Lck):
    Ldice=3
    print(f'{Name} 의 운은 C등급으로 힘에 관련된 주사위에 3의 보정이 붙습니다.')
if(Lck<39 and 20<Lck):
    Ldice=-3
    print(f'{Name} 의 운은 D등급으로 힘에 관련된 주사위에 -3의 보정이 붙습니다.')
if(Lck<19 and 0<Lck):
    Ldice=-5
    print(f'{Name} 의 운은 E등급으로 힘에 관련된 주사위에 -5의 보정이 붙습니다.')
print(Ldice)
Hp=random.randint(1,100)
print('체력')
print(Hp)
if(Hp>95):
    Hdice=20
    print(f'{Name} 의 체력은 Ex등급으로 힘에 관련된 주사위에 20의 보정이 붙습니다.')
if(Hp<94 and 80<Hp):
    Hdice=10
    print(f'{Name} 의 체력은 A등급으로 힘에 관련된 주사위에 10의 보정이 붙습니다.')
if(Hp<79 and 70<Hp):
    Hdice=5
    print(f'{Name} 의 체력은 B등급으로 힘에 관련된 주사위에 5의 보정이 붙습니다.')
if(Hp<69 and 40<Hp):
    Hdice=3
    print(f'{Name} 의 체력은 C등급으로 힘에 관련된 주사위에 3의 보정이 붙습니다.')
if(Hp<39 and 20<Hp):
    Hdice=-3
    print(f'{Name} 의 체력은 D등급으로 힘에 관련된 주사위에 -3의 보정이 붙습니다.')
if(Hp<19 and 0<Hp):
    Hdice=-5
    print(f'{Name} 의 체력은 E등급으로 힘에 관련된 주사위에 -5의 보정이 붙습니다.')
print(Hdice)
Dex=random.randint(1,100)
print('민첩')
print(Dex)
if(Dex>95):
    Ddice=20
    print(f'{Name} 의 민첩은 Ex등급으로 힘에 관련된 주사위에 20의 보정이 붙습니다.')
if(Dex<94 and 80<Dex):
    Ddice=10
    print(f'{Name} 의 민첩은 A등급으로 힘에 관련된 주사위에 10의 보정이 붙습니다.')
if(Dex<79 and 70<Dex):
    Ddice=5
    print(f'{Name} 의 민첩은 B등급으로 힘에 관련된 주사위에 5의 보정이 붙습니다.')
if(Dex<69 and 40<Dex):
    Ddice=3
    print(f'{Name} 의 민첩은 C등급으로 힘에 관련된 주사위에 3의 보정이 붙습니다.')
if(Dex<39 and 20<Dex):
    Ddice=-3
    print(f'{Name} 의 민첩은 D등급으로 힘에 관련된 주사위에 -3의 보정이 붙습니다.')
if(Dex<19 and 0<Dex):
    Ddice=-5
    print(f'{Name} 의 민첩은 E등급으로 힘에 관련된 주사위에 -5의 보정이 붙습니다.')
print(Ddice)
"""print('회피주사위') 
a=random.randint(1,100)
b=a+dex
print(f'{a}+{dex}(보정)={b}')
if(b>=50):print('회피 성공')
else:print('회피 실패')"""


