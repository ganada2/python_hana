

# class Animal:
#     tribe = '동물'
#     def __init__(self, name):
#         self.name = name
#
#     def getInfo(self):
#         print('나는', self.tribe,  self.name, '입니다.')
#
# # Animal의 자식클래스, Carnivore 클래스
# class Carnivore(Animal):
#     def __init__(self, name):
#         self.name = name
#         self.tribe = '육식동물'
#
#     def favoriteFood(self):
#         print('나는 고기를 좋아합니다.')
#
# # Animal의 자식클래스, Herbivore 클래스
# class Herbivore(Animal):
#     def __init__(self, name):
#         self.name = name
#         self.tribe = '초식동물'
#
#     def favoriteFood(self):
#         print('나는 풀을 좋아합니다.')
# \
# print('-' * 50, "\n[Carnivore 객체 생성]")
# tiger = Carnivore('호랑이')
# tiger.getInfo()
# tiger.favoriteFood()
#
# print('-' * 50, "\n[Herbivore 객체 생성]")
# rabit = Herbivore('토끼')
# rabit.getInfo()
# rabit.favoriteFood()



# 클래스 초기화 함수, __init__() 재정의
# class MyClass:
#     def __init__(self, name): # 초기화 함수 재정의
#         self.name = name
#
#     def sayHello(self):
#         hello = "Hello, " + self.name + "\t It's Good day !"
#         print(hello)
#
# # 객체 생성, 인스턴스화
# # myClass = MyClass()
# myClass = MyClass('채영')
# myClass.sayHello()
# print(myClass.name )


# # 클래스 정의
# class MyClass:
#     name = str()
#     print (type(name) )
#
#     def sayHello(self):
#         hello = "Hello, " + self.name + "\t It's Good day !"
#         print(hello)
#
# # 객체 생성, 인스턴스화
# myClass = MyClass()
# myClass.name = '준영'
# myClass.sayHello()



#
# var = '파이썬, 클래스와 객체'
# print('var       \t: ', var)
# print('id(var)   \t: ', id(var))
# print('type(var) \t: ', type(var))
#
# # str, str의 타입, str의 식별자 확인
# print('\nstr       \t: ', str)
# print('type(str) \t: ', type(str))
# print('id(str)   \t: ', id(str))
#
# #var 지역변수 __class__ 값 확인
# print('\nvar.__class__ : ', var.__class__)
#
# var2 = var.replace('파이썬', 'Python')
# print('\nvar2    \t: ', var2)

# # 클래스 정의 : X
# class MyClass:
#     def __init__(self, name): #초기화 시 오류 발생
#         self.name = name
#
#     name = '희영'
#
#     def sayHello(self):
#         hello = "Hello, " + self.name + "\t It's Good day !"
#         return hello
#
#
# myClass = MyClass('')
# obj_name = myClass.name
# obj_method = myClass.sayHello()
#
# print('Object name   :', obj_name)
# print('Object method :', obj_method)







# break vs. continue vs. pass
# scope = list(range(1, 100))
# print(scope)
# print(len(scope))
#
# for num in scope:
#     print('num',num)
#         if num <= 10:
#
#         if num % 2 == 0:
#             pass
#             #print(num, 'is even number.')
#         else:
#             continue
#             #print(num, 'is odd number.')
#     else:
#         print(num, 'is bigger than ten')
#         break
#         print('after break')
#
# print('프로그램을 종료합니다.')


# for Ex1
# bts_members = ['RM', '슈가', '진', '제이홉', '지민', '뷔', '정국']
# num = 0
#
#
# for member in bts_members:
#     num += 1
#     print('멤버%d ====> %s  \t(이름길이:%d)' % (num, member, len(member)))
#
# # for Ex2
# # size = len(bts_members)
# #
# # for idx in range(size):
# #     print('멤버%d ====> %s  \t(이름길이:%d)' % (id x +1, bts_members[idx], len(bts_members[idx])))
# # 멤버1 = == => RM  	(이름길이 :2)
# # 멤버2 = == => 슈가  	(이름길이 :2)
# # 멤버3 = == => 진  	(이름길이 :1)
# # 멤버4 = == => 제이홉  	(이름길이 :3)
# # 멤버5 = == => 지민  	(이름길이 :2)
# # 멤버6 = == => 뷔  	(이름길이 :1)
# # 멤버7 = == => 정국  	(이름길이 :2)
# # draw triangle with for
# # # 삼각형1
# for i in range(1, 10, 2):
#     mark = "*" * i
#     print(mark)
# *
# * **
# * ** **
# * ** ** **
# * ** ** ** **
# # 삼각형2
# for i in range(1, 10, 2):
#     mark = " " * int((1 0 -i ) /2) + "*" * i
#     print(mark)
#
#     *
# * **
# * ** **
# * ** ** **
# * ** ** ** **
# nested for
# # 중첩 for문
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# for x in range(3):
#     for y in range(3):
#         # print('matrix[', x, '][', y, ']:', matrix[x][y], end=', \t')
#         print('matrix[%d][%d]: ' %(x, y), matrix[x][y], end=' \t')
#     else:
#         print('')
#
#
# # while Ex01
# idx = 0
#
# while idx < 5:
#     print(idx)
#     idx += 1
#     print(idx)
#
# print('프로그램 종료!')
#
# while Ex02. 루프탈출
# num, sum = 1, 0
#
# while True:
#     sum += num
#     if sum > 100:
#         break
#     else:
#         num += 1
#     print(num)
#
#
# print('num 값이 %d 일때 while문 탈출 !!' % num)
# num 값이 14 일때 while문 탈출 !!
# # while Ex03
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# idx, sum = 0, 0
# print( 'len : ', len(numbers) )
# print(numbers[idx])
#
# while idx < len(numbers):
#     num = numbers[idx]
#     sum += idx
#     print('%s += %s ' %(sum, idx ) )
#     idx += 1
#     print(idx)
#
# print('numbers의 합계는', sum, '입니다.')
#
#
# # while Ex04
# sigmal_color = ''
#
# while sigmal_color != 'blue' and sigmal_color != 'red':
#     sigmal_color = input('색을 영문으로 입력하세요 (blue/red) : ')
#
#     if sigmal_color == 'blue':
#         print('신호등은 파란색 입니다. 길을 건너세요!!')
#     elif sigmal_color == 'red':
#         print('신호등은 빨간색 입니다. 기다리세요.')
#     else:
#         print('잘못된 색입니다. 다시 입력해 주세요!!')
#
# print('프로그램을 종료합니다.')
#
#
#
#
# ## if for while 문
#
# condition = False
#
# if condition:
#     print("조건을 충족함, condition met")
# if not condition:
#     #print("조건 충족 못함, condition not met")
#
#
# print('END')
#
#
#
# # if - else
# num_a = 100
# num_b = 200
#
# if num_a > num_b:
#     print('숫자A가 숫자B보다 더 큰수입니다.')
# else:
#     print('숫자A는 숫자B와 같거나 더 작은수입니다.')
# 숫자A는 숫자B와 같거나 더 작은수입니다.
# # if - elif -else
# num_a = 100
# num_b = 200
#
# if num_a > num_b:
#     print('숫자A가 더 큰수입니다.')
#     max = num_a
# elif num_a < num_b:
#     print('숫자B가 더큰수입니다.')
#     max = num_b
# else:
#     print('숫자A와 숫자B는 같습니다.')
#
# print('숫자A와 숫자B중 최대값은', max, '입니다.')
# 숫자B가 더큰수입니다.
# 숫자A와 숫자B중 최대값은 200 입니다.
# 조건값 : 논리연산자
# # if - else 문 예시
# signal_color = input('색을 영문으로 나타내어 보세요.')
#
# if signal_color == 'blue':
#     print('신호등은 파란색 입니다. 건너가 주세요.')
# else:
#     print('신호등은 빨간색 입니다. 기다려 주세요.')
#
#
# # 사전형 생성
# bans = { '잎새반':'찬영이',
#          '열매반':'예영이',
#          '햇살반':'준영이',
#          '열매반':'채영이', }
#
# print(type(bans))
# print('반의수 : ', len(bans))
#
# # 읽기
# print('bans 읽기 :', bans)
#
# # 추가
# a= bans.keys()
# bans.values()
# print('print bans : ', len(a) )
#
# bans['꽃잎반'] = '희영이'
# print('bans 추가 :', bans)
#
# # 변경
# bans['잎새반'] = '서영이'
# print('bans 변경 :', bans)
#
# # 삭제
# del bans['햇살반']
# print('bans 삭제 :', bans)
#
# #
# customer = {
#     "name"    : "김진수",
#     'gender'  : '남자',
#     "email"   : "bigpycraft@gmail.com",
#     "company" : "빅파이크래프트",
#     "address" : "서울시 중구 청파로"
# }
#
# print('customer.keys()   \t= ', customer.keys())
# print('customer.values() \t= ', customer.values())
# print('customer.items()  \t= ', customer.items())
# print('-'*50)
#
# for key, value in customer.items():
#     print('%s\t : %s' %(key, value))
#
#
# ## class set
#
# a = set ('aaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccc')
# print('set = %s'                %(a))
#
# '''set ->> list sort available'''
# b=list(a)
# print('b is not sorted = %s \t ' %(b), type(b) )
#
# c=sorted(b)
# print('c is sorted = \t %s \t' %(c), type(c) )
#
#
# # 리스트 응용
# solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']
# print('태양계 :', solarsys)
#
# type=type(solarsys)
# print(type)
#
# distant=5
#
# near_solar = solarsys[:distant]
# print('near_solar : ', near_solar)
# idx_near_solar = len(near_solar)
# print(idx_near_solar)
#
# far_solar= solarsys[idx_near_solar:idx_near_solar+distant]
# print('far_solar :', far_solar)

#
# # 리스트에서 특정 요소의 위치 구하기(index)
# planet = '지구'
# pos = solarsys.index(planet)
# print('%s 행성은 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos+1))
#
# type=type(solarsys)
# print(type)
#
# idx_plt= len(solarsys)
# print('idx_plt = %d' %(idx_plt) )
#
# solarsys.append('나로호')
# print('태양계 :', solarsys)
#
# pop=solarsys.pop(0)
# print('태양계 :', solarsys)
# print('pop = %s' %(pop) )