import random
dex=0
Hp=0
Luk=0
Str=0
Sdice=0
Ldice=0
Hdice=0
Ddice=0
Dice=0
Adice=0
print('''
환자가 동면에서 깨어남을 확인 동명에서 깨어나심을 축하드립니다.
그럼 기본적인 검사를 진행합니다.
당신의 이름은 무엇입니까?
      ''')
Name=input("주인공의 이름을 입력해주세요:")
print(f'''
{Name} 확인되었습니다. 이제 당신의 능력치를 측정합니다.
      ''')
print(f'{Name} 의 능력치')
print('힘')
Str=random.randint(1,100)
print(Str)
if(Str>=95):
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
print(f'''
능력치 측정이 끝 났습니다.
이제 동면기를 벗어나 담당 의사에게 안내를 받으시기를 바랍니다.
이시간부로 본 동면기는 작동을 중지합니다.
      ''')
print(f'''
"동면? 그래 난 불치병에 걸려 치료제가 나올 때까지 동면을 선택했다.
그럼 지금은 몇 년도지? 치료제는 담당 의사는 오고 있는 건가?
그러기에는 병실이 너무 어둡다 동면기는 작동을 중지하여 불빛이 꺼지고 이제 남은 불빛은 창문으로 들어오는 햇빛뿐.
뭔가 이상하다 일단 동면기를 나온 나는 뭘 해야 하지?"
      ''')
print(f'''
1.다른동면기를 확인한다.
2.사람을 불러본다.
3.병실 밖으로 나간다.
4.담당 의사를 기다린다.
''')
Ch=input('무엇을 할까?(1~5):')
while True:
    if Ch == '1':
        print('다른 동면기들은 작동을 정지했다 하지만 사람들은 아직 동면기 안에 있다 무언가 잘못됐다.다른 걸 해보자')
        Ch=input('무엇을 할까?(1~5):') 
    elif (Ch=='2'):
        print('"저기요 거기 아무도 없어요?"...기분 나쁜 침묵만 계속될 뿐이다.다른 걸 해보자')
        Ch=input('무엇을 할까?(1~5):')
    elif (Ch=='3'):
        print('위험한 건 안다. 하지만 아무도 없는 것 같은 이곳에서 가만히 있을 수만은 없다 나가보자.')
        break
    elif (Ch=='4'):
        print('30분 동안 의사를 기다렸다 하지만 그 누구도 오지 않았다.다른 걸 해보자')
        Ch=input('무엇을 할까?(1~5):')
    else:Ch=input('무엇을 할까?(1~5):')

        

 

"""print('회피주사위') 
Dice=random.randint(1,100)
Adice=Dice+Ddice
print(f'{Dice}+{Ddice}(보정)={Adice}')
if(Adice>=50):print('회피 성공')
else:print('회피 실패')"""



