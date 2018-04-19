import matplotlib.pyplot as plt
import shapefile

shpFilePath = "/home/eranga/PycharmProjects/Graphs/data/LKA_adm/LKA_adm0.shp"
listx=[]
listy=[]
test = shapefile.Reader(shpFilePath)
for sr in test.shapeRecords():
    for xNew,yNew in sr.shape.points:
        listx.append(xNew)
        listy.append(yNew)
plt.plot(listx,listy)
plt.show()