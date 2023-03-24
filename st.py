from tkinter import *
from random import*
#окно, 3 случайных точки, потом строим любую точку, случайным образом выбираем точку и смещаем к выбранной вершине на половину расстояния до нее

root=Tk()
canvas=Canvas(width=900,height=900,bg="white")

# x1=randint(0,850)
# y1=randint(0,850)
# x2=randint(0,850)
# y2=randint(0,850)
# x3=randint(0,850)ток
# y3=randint(0,850)
# canvas.create_rectangle([x1,y1],[x1+8,y1+8],fill="red")
# canvas.create_rectangle([x2,y2],[x2+8,y2+8],fill="red")
# canvas.create_rectangle([x3,y3],[x3+8,y3+8],fill="red")

x1=450
y1=50
x2=100
y2=750
x3=800
y3=750
canvas.create_rectangle([x1,y1],[x1+8,y1+8],fill="red")
canvas.create_rectangle([x2,y2],[x2+8,y2+8],fill="red")
canvas.create_rectangle([x3,y3],[x3+8,y3+8],fill="red")
am=0
flag=True
while flag:
	x0 = randint(0, 850)
	y0 = randint(0, 850)
	a1=(x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)
	a2=(x2-x0)*(y3-y2)-(x3-x2)*(y2-y0)
	a3=(x3-x0)*(y1-y3)-(x1-x3)*(y3-y0)
	if (a1 <= 0 and a2 <= 0 and a3 <= 0) or (a1 >= 0 and a2 >= 0 and a3 >= 0):
		flag=False
canvas.create_rectangle([x0,y0],[x0+3,y0+3],fill="blue",outline="blue")
canvas.pack()

while am<=1000000:
	point=randint(1,4)
	if point==1:
		x0=(x1+x0)//2
		y0=(y1+y0)//2
		canvas.create_rectangle([x0, y0], [x0 + 3, y0 + 3], fill="blue",outline="blue")
		canvas.update()
	elif point==2:
		x0=(x2+x0)//2
		y0=(y2+y0)//2
		canvas.create_rectangle([x0, y0], [x0 + 3, y0 + 3], fill="blue",outline="blue")
		canvas.update()
	elif point == 3:
		x0 = (x3 + x0) // 2
		y0 = (y3 + y0) // 2
		canvas.create_rectangle([x0, y0], [x0 + 3, y0 + 3], fill="blue",outline="blue")
		canvas.update()

root.mainloop()