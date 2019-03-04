#No1
def cetakSiku(x):
    for j in range (1, x+1):
       print (j * "@")

cetakSiku(5)

#No2
def persegi(x,y):
    for i in range(x):
        if i == 0 or i == x-1:
            print("@"*x)
        else:
            j = x - y
            print ("@"+" "*(x-2)+"@")
persegi(4,5)

#No3 A
def jumlahHurufVokal(x):
    jumlah = 0
    vokal = "aiueoAIUEO"
    for i in x:
        if i.lower() in vokal:
            jumlah += 1
    return (len(x), jumlah)
print (jumlahHurufVokal('Surakarta'))

#No3 B
def jumlahHurufKonsonan(y):
    jumlah = 0
    vokal = "aiueoAIUEO"
    for i in y:
        if i.lower() not in vokal:
            jumlah += 1
    return (len(y), jumlah)
print (jumlahHurufKonsonan ('Surakarta'))

#No4
def rerata(x):
	"""Menghitung rerata bilangan"""
	jml = 0
	for i in x:
	    jml += i
	return jml/len(x)
print(rerata([1,2,3,4,5]))
g = [3,4,5,4,3,5,2,2,10,11,23]
print (rerata(g))

#No5
from math import sqrt as sq
def apakahPrima(n):
	n=int(n)
	assert n>=0
	primaKecil=[2,3,5,7,11]
	bukanPrKecil=[0,1,4,6,8,9,10]
	if n in primaKecil:
		return True
	elif n in bukanPrKecil:
		return False
	else:
		hasil=[]
		for i in range(2,int(sq(n))+1):
			if i in primaKecil:
				hasil.append(True) 
			elif i in bukanPrKecil:
				hasil.append(False) 
		return hasil
print(apakahPrima(20))

#No6
def bilanganprima():
    prima=list()
    for i in range(2,1000):
        x = True
        for iter in prima:
            if(i%iter==0):
                x=False
                break
        if(x):
            print(i)
            prima.append(i)
bilanganprima()

#No7
def faktorprima(n):
    p = list()
    for i in range(2,n):
        x = True
        for iter in p:
            if(i%iter==0):
                x=False
                break
        if x and n%i==0:
            p.append(i)
    return p
print(faktorprima(120))

#No8
def apakahTerkandung(a,b):
    return a in b
print(apakahTerkandung("indonesia","indonesia tanah air beta"))
print(apakahTerkandung("do","pusaka"))

#No9
for x in range (1, 100) :
    if (x%3 == 0 and x%5 == 0) :
        print ("Python UMS")
    elif x%5 == 0 :
        print ('UMS')
    elif x%3 == 0 :
        print ("Python")
    else :
        print (x)

#No10
from math import sqrt as akar
def selesaikanABC (x, y, z):
    x = float(x)
    y = float(y)
    z = float(z)
    n = y**2 - 4*x*z
    if (n < 0):
        print("Determinannya negatif. Persamaan tidak mempunyai akar real.")
    else:
        a1 = (-y + akar(n))/(2*x)
        a2 = (-y + akar(n))/(2*x)
        hasil = (a1, a2)
        return hasil

#No11
tahun = int (input("Masukkan angka tahun: "))
kabisat = False
if (tahun % 400 == 0) :
    kabisat = True
elif tahun % 100 == 0 :
    kabisat = False
elif tahun % 4 == 0 :
    kabisat = True
    print("tahun kabisat") if kabisat else print("bukan tahun kabisat")

#No12
import random
s = random.randint(1, 100)
print("""Permainan tebak angka.\nSaya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.""")
b = "Masukkan tebakan ke-"
f = ":> "
c = 1
d = str(c)
for i in range (1, 100):
    n = (b+d+f)
    a = int(input(n))
    c+=1
    d = str(c)
    if (a < s):
        print("Itu terlalu kecil. Coba lagi.")
    elif (a > s):
        print("Itu terlalu besar. Coba lagi.")
    elif (a == s):
        print("Ya. Anda benar")
        break

#No13
def katakan(a):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"puluh ",-3:"ratus ",-4:"ribu ",-5:"puluh ",6:"ratus ",7:"juta ",8:"puluhjuta "}
    b=str(a)
    c=""
    i=-1
    while i>= -len(b):
        c=x[b[i]]+y[i]+c
        i-=1
    return c
print(katakan(9936))

#No14
def formatRp(n):
    i = str(n)
    if len(i) <= 3:
        return "Rp " + i
    else:
        x = i[-3:]
        y = i[:-3]
        return formatRp(y) + "." + x
        print ("Rp " + formatRp(y) + "." + x)
