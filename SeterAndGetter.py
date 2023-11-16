# setter dan getter adalah cara mengunci dan membuka suatu atribut dalam class
class Mikroskil:
    def __init__(self,nim,nama,jenisKelamin):
        self.__nim = nim
        self.__nama = nama
        self.__jenisKelamin = jenisKelamin

    @property
    def nim(self):
        return self.__nim
    @nim.setter
    def nim(self,nimBaru):
        return nimBaru

    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self,namaBaru):
        return namaBaru


    @property
    def jkelamin(self):
        return self.__jenisKelamin
    @jkelamin.setter
    def jkelamin(self,jkelaminBru):
        return jkelaminBru


    def cetak(self):
        print(f"Nim : {self.__nim} \nNama : {self.__nama} \nJenis Kelamin : {self.__jenisKelamin}")


mhs = Mikroskil("221112920","mikael","laki")
mhs.nim= "2"
mhs.nama = "Michael Sitanggang"
mhs.jkelamin = "Laki - Laki"
print(f"Nim : {mhs.nim}")
print(f"Nim : {mhs.nama}")
print(f"Nim : {mhs.jkelamin}")