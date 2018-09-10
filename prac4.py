#
# # swap case
# s = 'The BigpyCraft find the information to design valuable society with Technology & Craft.'
# # s = input('영어 대소문자로 이루어진 문장을 입력하세요.\n')  # 문자열 입력
#
# print('모두 대문자로 출력\n' + s.upper())   # 대문자로 모두 변환
#
# print('모두 소문자로 출력\n' + s.lower())   # 소문자로 모두 변환
#
# new_s = str()   # 신규 문자열 형 변수 선언
#
# for c in s:     # 입력 받은 문자를 하나씩 꺼내서 c에 대입
#
#     if c.islower():         # 해당 문자가 소문자이면
#         new_s += c.upper()  # 대문자로 변경하여 new_s에 붙이기
#     else:                   # 해당 문자가 대문자이면
#         new_s += c.lower()  # 소문자로 변경하여 new_s에 붙이
#
# print('대소문자 바꿔서 출력\n' + new_s)             # 최종 변환 결과 출력
#
# print('대소문자 바꿔서 출력\n' + s.swapcase())      # 대소문자 모두 변환

# reverse case
s = 'Lief is too short, You nee Python.'
#s = input('영어 문장을 입력하세요.\n')  # 문자열 입력

new_s = str()                       # 신규 문자열형 변수 선언

#for x in range(len(s)-1,-1, -2):
#for x in range(len(s)-1, -1, -1):   # range()를 활용한 역순 인덱스 추출
 #   new_s += s[x]                   # 문자열을 끝에서부터 앞으로 신규 변수에 붙이기

print(s)                        # 위 결과 출력
print(s[1::10])
#print(s[::-1])                      # 인덱스 사용법으로 역순 출력


# # # dan = input('출력할 단을 입력해주세요.[2~9] ')
# # dan = 5
# # dan = int(dan)
# # gop = 0
# #
# # print(dan, '단 출 력 \n' + '-'*20)
# # # print(dan, '단 출 력 - Case1\n' + '-'*20)
# # for i in range(9):
# #     num = i + 1
# #     gop = dan * num
# #     print(dan, '*', num, '=', gop)
# # 5 단 출 력
# # --------------------
# # 5 * 1 = 5
# # 5 * 2 = 10
# # 5 * 3 = 15
# # 5 * 4 = 20
# # 5 * 5 = 25
# # 5 * 6 = 30
# # 5 * 7 = 35
# # 5 * 8 = 40
# # 5 * 9 = 45
# # 팩토리얼 표: 0~100 까지의 Factorial Table
# # # 팩토리얼 표: 0~100 까지의 Factorial Table
# # idx, gop, sum  = 0, 0, 0
# # factorial = [ ]
# # total_sum = [ ]
# #
# # # 입력값 확인
# # # num_check = list(range(10))
# # num_chk_list = list('0123456789')
# # # print(num_chk_list)
# # chk = True
# #
# # while True:
# #     input = input(' 숫자 입력 = ')
# #     chk *= input
# #
# #     print(chk)
#     # for char in num_chk_list:
#     #     if( chk != 0 ):
#     #         print('num')
#     #     else:
#     #         print('not')
#     #         break
# # while True:
# #     key_in = input('숫자를 입력해 주세요. (1~100)')
# #     chk_num = True
# #     for char in key_in:
# #         is_num = char in num_chk_list
# #         chk_num *= is_num
# #         if not is_num:
# #             break
# #         # print(char, is_num, chk_num)
# #
# #     if chk_num:
# #         last_num = int(key_in)
# #         print('입력한 숫자 :', last_num)
# #         break
# #     else:
# #         print('입력한 값이 숫자가 아닙니다.')
# #
# # print('숫자확인 완료!')
# # last_num = 10
# #
# #
# # # 입력값이 숫자인 경우, 미션 수행
# # title =  str(last_num) + '까지의 팩토리얼 테이블 구하기!!'
# # print('-'*100)
# # print(title)
# # print('-'*100)
# #
# # numbers = list(range(last_num+1))
# # # print('numbers :', numbers)
# #
# # while idx < len(numbers):
# #     num = numbers[idx]
# #     gop *= num
# #     # if gop < 1:
# #     #     gop = 1
# #     gop = 1 if gop<1 else gop
# #
# #     factorial.append(gop)
# #     idx += 1
# #
# # for fact_num in range(len(factorial)):
# #     print(str(fact_num)+'! = ', factorial[fact_num])
# # 숫자를 입력해 주세요. (1~100)5
# # 입력한 숫자 : 5
# # ----------------------------------------------------------------------------------------------------
# # 5까지의 팩토리얼 테이블 구하기!!
# # ----------------------------------------------------------------------------------------------------
# # 0! =  1
# # 1! =  1
# # 2! =  2
# # 3! =  6
# # 4! =  24
# # 5! =  120
#
#
# 팩토리얼 표: 0~100 까지의 Factorial Table
# # 팩토리얼 표: 0~100 까지의 Factorial Table
# idx, gop, sum  = 0, 0, 0
# factorial = [ ]
# total_sum = [ ]
#
# # 입력값 확인
# # num_check = list(range(10))
# num_chk_list = list('0123456789')
# # print(num_chk_list)
#
# while True:
#     key_in = input('숫자를 입력해 주세요.[1~100] => ')
#     chk_num = True
#     for char in key_in:
#         is_num = char in num_chk_list
#         chk_num *= is_num
#         if not is_num:
#             break
#         # print(char, is_num, chk_num)
#
#     if chk_num:
#         last_num = int(key_in)
#         print('입력한 숫자 :', last_num)
#         break
#     else:
#         print('입력한 값이 숫자가 아닙니다.')
#
# # print('숫자확인 완료!')
# # last_num = 10
#
# # 입력값이 숫자인 경우, 미션 수행
# title =  str(last_num) + ' 까지의 합계 및 팩토리얼 테이블 구하기!!'
# print('-'*50)
# print(title)
# print('-'*50)
#
# numbers = list(range(last_num+1))
# # print('numbers :', numbers)
#
# while idx < len(numbers):
#     num = numbers[idx]
#     sum += num
#     gop *= num
#
#     gop = 1 if gop<1 else gop
#     # if gop < 1:
#     #     gop = 1
#
#     total_sum.append(sum)
#     factorial.append(gop)
#     idx += 1
#
# print(last_num, '까지의 합계는', total_sum[-1], '입니다.')
# print('아래는 팩토리얼 테이블입니다.')
# for fact_num in range(len(factorial)):
#     print(str(fact_num)+'!\t= ', factorial[fact_num])