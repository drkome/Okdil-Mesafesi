## Öklit Fonksiyonu
def euclideanDistance(a,b):
    z=(((a[0]-b[0])**2)+((a[1]-b[1])**2))**0.5;
    return z; 

## En kücük Degeri bulan
def minvalue(liste):
    minimum=liste[0]
    for a in range(0,len(liste)):
        if(minimum>=liste[a]):
            minimum=liste[a]
    return minimum


distance=[]
points= [(4,5),(8,9),(55,125),(125,65),(3,4),(957,124),(63,75),(847,35),(34,87)]

boyut=len(points)


##Liste bütün noktalarla işlem yapan döngü
for i in range(0,boyut-1):
    for a in range(i+1,boyut):
        distance.append(euclideanDistance(points[i],points[a]))


kucuk=minvalue(distance)
print(kucuk)