import numpy as np
import numpy.random

print(np.array([5,75,83,95]))

my_list  = ["Bucak","Zeliha","Tolunay",15,True,98.65]

print(f"Listenin ilk tipi = {type(my_list)}")

my_arr = np.array(my_list)

print(f"Listenin son tipi = {type(my_arr)}")
print(my_list)
print("*"*50)
print(my_arr)

# Baştan sıfırdan array tanımlama

my_arr2 = np.array([56,102,65.89],dtype=int)
print(my_arr2)
print(type(my_arr2))

# Normalde python'da yerleşik olarak bulunan random isminde bir modül var.
# Numpy çok güçlü bir modül olduğu için kendi random modülünü kullanır.

# 0 ve 1 arasında 5 satır 3 sütundan rastgele değerlerle oluşan
# matris tanımlama

print(numpy.random.rand(5,3))

print("-"*50)

# int tipinde rastgele değerler ile 5 satır 3 sütundan oluşan matris
print(numpy.random.randint(5,100,(5,3)))

# float tipinde rastgele değerler ile 5 satır 3 sütundan oluşan matris

print(numpy.random.uniform(-3,10,(5,3)))

# int tipinde 4 satır 4 sütundan oluşan 10 ve 100 arasında değerler
# barındıran matris
print("-"*50)
print(numpy.random.randint(10,100,(4,4)))

# matrislerde boyut (satır ve sütun sayısı öğrenme) => shape fonksiyonu ile
print("-"*50)

my_arr4 = numpy.random.randint(10,100,(4,4))
print(my_arr4.shape)

# eleman sayısı öğrenme => size fonksiyonu ile
print(my_arr4.size)

# (Boyut) Katman sayısı öğrenme (satır, sütun, kanal sayısı)
print(my_arr4.ndim)

# Matrisi yeniden boyutlandırma => reshape fonksiyonu ile
# Yeniden boyutlandırma işlemi için satır ve sütun sayısının çarpımı
# ile yeniden boyutlandırmada verilen satır ve sütunun birbirine oranlı
# yani tam bölünebilir olması lazım

# my_arr4'ün boyutu = (4,4) => 4 * 4 = 16
# yeniden boyut için verilebilecek boyut bilgileri:
# (1,16), (2,8), (8,2), (16,1)

#my_arr5 = np.reshape(my_arr4,(1,16))
#my_arr5 = np.reshape(my_arr4,(2,8))
#my_arr5 = np.reshape(my_arr4,(8,2))
my_arr5 = np.reshape(my_arr4,(16,1))
print(my_arr5)

print("-"*50)

# Matrisler ile matematiksel işlemler

my_arr6 = numpy.random.randint(1,100,(3,3))
print(f"my_arr6 = \n{my_arr6}")
print(f"my_arr6 * 2 = \n{my_arr6 * 2}")

my_arr7 = numpy.random.randint(1,10,(2,2))
my_arr8 = numpy.random.randint(1,10,(2,2))

print("-"*50)

print(my_arr7)
print(my_arr8)
print(my_arr7 + my_arr8)

# 2x2'lik 1 ve 20 arasında değerlerden oluşan 2 matrisi önce 3 ile çarpın
# sonra bu iki matrisi birbirinden çıkarın

matris_1 = numpy.random.randint(1,20,(2,2))
matris_2 = numpy.random.randint(1,20,(2,2))

matris_1 = matris_1 * 3
matris_2 = matris_2 * 3

print(matris_1-matris_2)
