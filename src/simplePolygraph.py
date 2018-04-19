from matplotlib import pyplot as p  #contains both numpy and pyplot
x1 = [-1,-1,10,10,-1];
y1 = [-1,10,10,-1,-1];
x2 = [21,21,29,29,21];
y2 = [21,29,29,21,21];
shapes = [[x1,y1],[x2,y2]]
for shape in shapes:
  x,y = shape
  p.plot(x,y)
p.show()