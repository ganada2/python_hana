import turtle as t
import math

print('다각형을 그리는 예제입니다.')

var1 = 4
var2 = 150
num_of_side = int(var1)
len_of_side = int(var2)

angle = 360.0 / num_of_side
c_mod = num_of_side % 3
color = 'red' \
    if c_mod==0 else 'green' if c_mod==1 else 'blue'

#t.begin_fill()
t.color(color)
t.pensize(5)

for i in range(num_of_side):
    t.forward(len_of_side)
    t.left(angle)

#t.end_fill()


t.right(180+135)
t.forward(math.sqrt(var2**2 + var2**2) )
t.left(90)
t.forward(math.sqrt(var2**2 + var2**2 )/2)

t.left(90)
t.forward(math.sqrt(var2**2 + var2**2 )/2)

t.left(90)
t.forward(math.sqrt(var2**2 + var2**2 ))




t.done()
