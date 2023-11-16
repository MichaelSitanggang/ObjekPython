import os 
class Mahasiswa:
    def __init__(self, nim, nama, hp):
        self.nim = nim
        self.nama = nama
        self.hp = hp
class Michael:
    def __init__(self):
        self.dt = []
        self.dt.append(Mahasiswa("221119995", "Ani", "081399889988"))
        self.dt.append(Mahasiswa("221119992", "Budi", "081399779977"))
    def tambah(self, mhs):
        for d in self.dt:
            if(d.nim == mhs.nim):
                print("Mahasiswa dengan NIM:", mhs.nim, "sudah ada !")
                return
        self.dt.append(mhs)
        print(mhs.nama, "Berhasil ditambahkan !")
    # def urut(self):
    #     self.dt = sorted(self.dt, key=lambda x:int(x.nim))
    def BubleSort(self):
        n = len(self.dt)
        for i in range(n):
            hasil = False
            for j in range(0, n-i-1):
                if self.dt[j].nim > self.dt[j+1].nim:
                    self.dt[j], self.dt[j+1]= self.dt[j+1], self.dt[j]
                    hasil = True

            if not hasil :
                break
    
    def absen(self, nim):
        for m in self.dt:
            if(nim == m.nim):
                print("Mahasiswa dengan nama", m.nama, "("+ m.nim+") Hadir")
                break
            elif(m.nim == self.dt[len(self.dt)-1].nim):
                print("Mahasiswa dengan NIM", "("+nim+") Tidak Hadir")
    def cetak(self):
        self.BubleSort()
        print("\nDaftar Seluruh Siswa")
        print("=====================")
        for mhs in self.dt:
            print(mhs.nim, mhs.nama, mhs.hp)

def menu():
    st=True
    while(st):
        os.system('cls')
        print("Menu:\n1. Tambah Data\n2. Absensi\n3. Cetak Daftar\n0. Keluar")
        mn =0
        mn = input("Pilihan : ")
        if(mn=="1"):
            d1 = input("NIM\t: ") 
            d2 = input("Nama\t: ")
            d3 = input("HP\t: ")
            mTmp = Mahasiswa(d1,d2,d3)
            mhs.tambah(mTmp)
            mhs.BubleSort()
            input("Tekan Enter untuk lanjut !")
        elif(mn=="2"):
            e1 = input("NIM\t: ")
            mhs.absen(e1)
            input("Tekan Enter untuk lanjut !")
        elif(mn=="3"):
            mhs.cetak()
            input("Tekan Enter untuk lanjut !")
        elif(mn=="0"):
            st=False
        else:
            print("Pilihan Tidak Tersedia !")
            input("Tekan Enter untuk lanjut !")

mhs = Michael()
menu()
