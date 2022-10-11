x = "*hilal nuran*"

type(x)		       # icine yazili degiskenin tipini döndürür.
str(6)		       # 6 number'ini stringe dönüstürür.
float("6.0")       # 6 stringini float'a döndürür.
int("6")	       # 6 stringini number'a dönüstürür.

len("enes")     # Bana enes stringinin karakter sayisini döndür.

dir(x)          # x degiskeni üzerinde uygulanabilecek metodlari listele.

x.upper()       # x stringinin harflerini büyüt.
x.lower()       # x stringinin harflerini kücült.

x.islower()     # x stringi kücük mü?
x.isupper()     # x stringi büyük mü?

x.replace("a", "e") # x stringinin a harflerini e ile degistir.

x.strip("*")    # x degiskeninin etrafindaki *'lardan kurtul, yani sil.  

x.capitalize()  # x stringinin ilk karakterini büyüt.
x.title()       # x stringinin her kelimesinin ilk harfini büyüt.

print("enes", "hilal", sep=("_"))  # "enes_hilal" seklinde cikti verir.

x=["Siegen", "München", "Berlin"]

x[0]            # x listesinin 0. elemani
x[-1]           # x listesinin sondan 1. elemani
x[0]="Solingen" # x listesinin ilk elemanini "Solingen" olarak degistirmis olduk.

x[0:3]          # x stringinin harflerini 0'dan 3'e kadar (3 dahil degil) döndür.
x[0:3:2]        # x stringinin harflerini 0'dan 3'e kadar (3 dahil degil) 1 atlayarak döndür.


x.append("Osnabrück") 	 # x listesinin sonuna "Osnabrück" eklemis olduk.
x.extend(["Paris", "Brüj", "Düsseldorf"])   # x listesinin sonuna yazili elemanlari topluca eklemis olduk. (tek tek yazmamiza gerek kalmadi)
x.remove("Siegen")    	 # x listesinden "Siegen"i siler.
x.pop(0)             	 # x listesinin 0. elemanini siler.
x.insert(0, "Bursa")     # x listsinin 0. indexine Bursa stringini ekle.

x.count("Siegen")      # x listesindeki Siegen stringinin sayisini döndürür.
x.index("Siegen")      # x listesindeki Siegen stringinin index numarasini döndürür.
x.reverse()            # x listesini cevirir.
x.sort()               # x listesi sayilardan olusan bir liste olsun. Sayilari kücükten büyüge dogru siralar.

xYedek = x.copy()      # x listesini yedekleyip yazili degiskene atar.
x.clear()              # x listesinin icini bosaltir.

del x                  # x degiskenini sil.


setOlustur = set(x)    # x listesinden bir set olustur. (setlerde her bir eleman bir kez bulunabilir.)
setOlustur.add("Antalya")   # setOlustur setine Antalya stringini ekler.
setOlustur.remove("Antalya")    # setOlustur setindeki Antalya stringini siler.
setOlustur.discard("Antalya")   # setOlustur setindeki Antalya stringini varsa siler, yoksa da problem cikarmaz.

###





set1=set([1,3,5,7])
set2=set([1,2,3,4,5,6,7])

set1.difference(set2)   # set1'in set2'den farkini döndürür. {5}

set1.symmetric_difference(set2)   # set1 ve set2'nin birbirinden farklarini döndürür. {2,5}

set1.intersection(set2) # set1 ve set2'nin ortak elemanlarini döndürür.
set1.difference(set2)   # set1'in set2'den farkini döndürür. {5}
set1.intersection_update(set2)   # set1 ve set2'nin ortak elemanlari set1'in artik yeni elemanlari olur. (günceller).
set1.union(set2)        # set1 ile set2 setlerini birlestirir.

set1.isdisjoint(set2)   # set1 ile set2 ortak elemanlar iceriyor mu?
set1.issubset(set2)     # set1 set2 nin alt kümesi midir?
set2.issuperset(set1)   # set2 set1'i kapsiyor mu?


###


def x():		    # x isminde bir fonksiyon tanimladik.
	...
    
x = lambda a,b : a+b # bu da bir baska fonksiyon tanimlama sekli.

def x(a,b=2,c):         	    # tanimlanan fonksiyonda a+b*c sonucunu döndürür.
	global sonuc        # globalden sonuc degiskenini cagirdik.
	return a+b*c/sonuc

def y():
	pass		    # "simdilik es gec" demek.


###

if (x > 2) and (y < 8 or not z == 10):
	break # if döngüsünden komple cikar.
elif x > 10:
	break # bir sey yapma, devam et.
else:
	...

###

c=[1,2,3,4,5]

for sayi in c:
	...
    
    
###


while True:		    # while döngüsü kurma
	...
    
###

class Kullanici:
    
    universityname = "Uni Köln"
    
	def __init__(self, kullaniciadi, sifre): # bu class'tan ne zaman bir obje olusturulursa, bu kisim calisir. burasi baslangic degerleridir.
		self.userid = kullaniciadi
		self.passw = sifre
		self.takenlessons = 0

	def derskaydi(self, dersadi):
		self.takenlessons += 1
		self.takenlesname = dersadi
        
class Yönetici(Kullanici): # bu class artik Kullanici classinin tüm özelliklerine sahip.
    def dersAtama(self, atananders):
        self.lesson = atananders

enes=kullanici("g05599", 164153)
print(enes.passw)                 # 164153 olarak cikti verir.
enes.derskaydi("edp")             # edp adindaki dersi aldi, takenlesname'ye atadi.
hilal = Yönetici()


###

liste1=[1,3,5,7]
liste2=[1,2,3,4]

import numpy

a = numpy.array(liste1)
b = numpy.array(liste2)

a*b # listelerin ayni indexlerini birbirleriyle carpar.

###

list(map(lambda herbireleman: herbireleman + 10, liste1) # liste1'deki her bir elemanin üzerine 10 ekle ve bunu listele.

list(filter(lambda herbireleman: herbireleman > 10, liste1) # liste1'deki her bir elemani kontrol et 10'dan büyük olanlari listele.

     
from functools import reduce
reduce(lambda a , b : a + b, liste1) # liste1'deki her bir elemani birbirleriyle toplayarak gez.

###

try:
    print(busatirikontrolet)
except NameError:
    print("NameError hatasi varsa bunu yap.")
except:
    print("Hata NameError hatasi degilse bunu yap.")
else:
    print("Hata yok, o yüzden bunu yap.")
finally:
    print("Hata olsa da olmasa da bunu yap")
