from Lin_regr import regr
m = regr()

for i in range(0,4):
   s = int(input('input x'))
   m.x.append(s)
   n = int(input('input y'))
   1m.y.append(n)



print(len(m.x), len(m.y))

print(m.x, m.y)
    

a = m.avg_x()
b = m.avg_y()

g = m.sum_x()

h = m.sum_y()

j = m.slope()

d = m.intercept_()

r = m.pred()
