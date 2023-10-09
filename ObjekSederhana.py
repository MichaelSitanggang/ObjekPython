from abc import ABC , abstractmethod
class les(ABC):
    @abstractmethod 
    def cetak(self):
        pass

class privateLes(les):
    def __init__(self , nama , noHp,biayaLes):
        self.nama = nama
        self.noHp = noHp
        self.biayaLes = biayaLes

class sd(privateLes):
    def __init__(self, nama, noHp, biayaLes , jenisKelamin):
        super().__init__(nama, noHp, biayaLes)
        self.jenisKelamin = jenisKelamin

    def cetak(self):
        print("Anak SD")
        print(f"Nama : {self.nama} \nnoHp : {self.noHp} \nbiaya Les : {self.biayaLes} \nJenis Kelamin : {self.jenisKelamin}")

class smp(privateLes):
    def __init__(self, nama, noHp, biayaLes, Umur):
        super().__init__(nama, noHp, biayaLes)
        self.Umur = Umur

    def cetak(self):
        print()
        print("Anak SMP")
        print(f"Nama : {self.nama} \nnoHp : {self.noHp} \nbiaya Les : {self.biayaLes} \nUmur : {self.Umur}")

class sma(privateLes):
    def __init__(self, nama, noHp, biayaLes, JenisKelas):
        super().__init__(nama, noHp, biayaLes)
        self.jenisKelas = JenisKelas

    def cetak(self):
        print()
        print("Anak SMA")
        print(f"Nama : {self.nama} \nnoHp : {self.noHp} \nbiaya Les : {self.biayaLes} \nJenis Kelas : {self.jenisKelas}")

anakSd = sd('anna','081367889013','500.000','Perempuan')
anakSmp = smp('abel','08136744013','800.000',21)
anakSma = sma('rungkit','089034567822','1.200.000','Ipa')

anakSd.cetak()
anakSmp.cetak()
anakSma.cetak()



