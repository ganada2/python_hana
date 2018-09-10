# import turtle as t
#
# def turn_right():
#     t.setheading(0)
#     t.forward(10)
#
# def turn_up():
#     t.setheading(90)
#     t.forward(10)
#
# def turn_left():
#     t.setheading(180) #angle
#     t.forward(10)
#
# def turn_down():
#     t.setheading(270)
#     t.forward(10)
#
# def blank():
#     '''DEF BLANK'''
#     t.clear()
#
# print(blank.__doc__)
#
# t.shape("turtle")
# t.speed(10)
# t.onkeypress(turn_right, "Right")
# t.onkeypress(turn_up,"Up")
# t.onkeypress(turn_left,"Left")
# t.onkeypress(turn_down,"Down")
# t.onkeypress(blank, "Escape")
# t.listen()
# t.mainloop()


# 마우스클릭으로 이어그리기
import turtle as t

t.speed(1)
t.pensize(5)
t.shape("turtle")

# t.hideturtle()
t.onscreenclick(t.goto)
t.mainloop()


'''#import this'''

# def add(a, b):
#     return a + b
#
# data = (10, 20)    # tuple
# #print(add(data))
# #print(add(*data))  # unpacking
# print(type(data) )
# print(type(add(*data)))
# print(data)
# print(add(*data))


# def introduce(name, b):
#     return "{}님, {}".format(
#         name,
#         b,
#     )
#
# introduce_dict = {
#     "name" : "김진수",
#     "b" : "안녕하세요",
# }
# print(introduce(**introduce_dict))


# def introduceMyFamily(my_name, *family_names, **family_info):
#     print('안녕하세요, 저는 %s 입니다.' % (my_name) )
#     print('-' * 35)
#     print('제 가족들의 이름은 아래와 같아요. ')
#
#     for name in family_names:
#         print('* %s ' % (name))
#     else:
#         print()
#     print('-' * 35)
#
#     for key in family_info.keys():
#         print('- %s : %s ' % (key, family_info[key]))
#
#
# introduceMyFamily('진수', '희영', '찬영', '준영', '채영',
#                   주소='롯데캐슬', 가훈='극기상진', 소망='세계일주')

# # Keyword Arguments, 키워드 인자 활용하기
# def introduceMyCar(brand, seats=4, type='세단'):
#     print('나의 차는 {b} {s}인승 {t}이다'.format(b = brand,s = seats,t = type)  )
#     # print('나의 차는', brand, '의', seats, '인승', type, '이다')
# introduceMyCar('아우디','10')


# # 위치 인자 값 1개
# introduceMyCar('아우디')
#
# # 키워드 인자 값 1개
# introduceMyCar(brand='렉서스')
#
# # 위치 인자 값 1개, 키워드 인자 값 1개, 혼용으로 사용 가능
# introduceMyCar('제규어', seats=2)
#
# # 키워드 인자 값 2개
# introduceMyCar(brand='머큐리', type='머슬카')
#
# # 순서 바뀐 키워드 인자 값2개, 순서가 바뀐 경우는 반드시 키워드 인자값 사용
# introduceMyCar(type='미니벤', brand='카니발')
#
# # 순서를 지킨 위치 인자 값 3개, 순서가 같다면 모두 위치 인지 값 사용 가능
# introduceMyCar('카니발', 9, '미니벤')
#
# # 순서 바뀐 키워드 인자 값3개, 순서가 바뀐 경우는 반드시 키워드 인자값 사용
# introduceMyCar('쉐보레', type='SUV ', seats=7)


# result1 = list(range(10))
#
# # range() 인자값 2개
# result2 = list(range(5, 10))
#
# # range() 인자값 3개
# result3 = list(range(1, 10, 2))
#
# print('range(10)     \t= ', result1)
# print('range(5,10)   \t= ', result2)
# print('range(1,10,2) \t= ', result3)
#
# # 함수 생성1
# def add_txt(arg1, arg2):
#     print(arg1, arg2)
#
# param1 = '대~한민국~'
# param2 = '짝짝~짝~ 짝.짝!!'
# add_txt(param1, param2)
#
# # 함수 생성2
# def add_num(num1, num2):
#     result = num1 + num2
#     return result
#
# param1 = 40
# param2 = 50
# sum = add_num(param1, param2)
# print('%d와 %d의 합은 %d입니다.' % (param1, param2, sum))
#
#
# # 함수 호출1,  No Return Function
# def sayHello():
#     print('Hi, Guys !!')
#
# sayHello()
# # print(sayHello())
#
#
# # 함수 호출2
# def exchangeUSDtoKRW(dollar):
#     won = dollar * 1065
#     return won
#
# usd = 2000
# krw = exchangeUSDtoKRW(usd)
# print('환전한 금액은 %d 원 입니다.'%(krw))