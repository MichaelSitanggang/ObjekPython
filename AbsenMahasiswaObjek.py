class Person:
    def __init__(self,nomor_induk,nama,jenis_kelamin,noHp):
        self.nomor_induk = nomor_induk
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.noHp = noHp

class Mahasiswa(Person):
    def __init__(self,nomor_induk,nama,jenis_kelamin,noHp,jurusan,angkatan):
        super().__init__(nomor_induk,nama,jenis_kelamin,noHp)
        self.jurusan = jurusan
        self.angkatan = angkatan

    def Absensi(self):
        print(f"Mahasiswa {self.nama} dengan nomor induk {self.nomor_induk} telah melakukan absensi")

class Dosen(Person):
    def __init__(self,nomor_induk,nama,jenis_kelamin,noHp,bidang):
        super().__init__(nomor_induk,nama,jenis_kelamin,noHp)
        self.bidang = bidang

    def perkenalan(self):
        print(f"Saya adalah dosen {self.nama} dengan bidang {self.bidang} No Hp : {self.noHp}")

mahasiswa = Mahasiswa('221112920' , 'Michael Sitanggang' , 'Pria' ,'081378945826' , 'Teknik Informatika' , 2022)
dosen = Dosen('19718080','Gunawan' , 'Pria', '089977990934', 'Basis Data')

mahasiswa.Absensi()
dosen.perkenalan()

    
        