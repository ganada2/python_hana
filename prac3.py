import turtle as t
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'magenta', 'violet']
for i in range(45):
    t.color( colors[i%len(colors)])
    t.forward(2+ i*5)
    t.left(45)
    t.width(i)

t.done()
