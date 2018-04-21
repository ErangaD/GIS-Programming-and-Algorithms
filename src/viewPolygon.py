
import shapefile as shp
import matplotlib.pyplot as plt

sf = shp.Reader("/home/eranga/PycharmProjects/Graphs/data/LKA_adm/LKA_adm1.shp")
plt.figure()
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.fill(x,y);
    plt.plot(x,y)
plt.show()
