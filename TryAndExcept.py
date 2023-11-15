class Person:
    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp

    def validate_nama(self):
        if not all(char.isalpha() or char.isspace() for char in self.nama):
            raise ValueError("Nama hanya boleh terdiri dari huruf dan spasi saja.")
        return True

    def validate_no_hp(self):
        if not (self.no_hp.startswith('+') and self.no_hp[1:].isdigit() and 8 <= len(self.no_hp) <= 15):
            raise ValueError("No HP harus dimulai dengan '+' diikuti dengan angka, dan memiliki panjang 8-15 karakter.")
        return True

class Mahasiswa(Person):
    def __init__(self, nim, nama, no_hp):
        super().__init__(nama, no_hp)
        self.nim = nim

    def validate_nim(self):
        if not (self.nim.isdigit() and len(self.nim) == 9):
            raise ValueError("NIM harus terdiri dari 9 digit angka.")
        return True

class Dosen(Person):
    def __init__(self, nip, nama, no_hp):
        super().__init__(nama, no_hp)
        self.nip = nip

    def validate_nip(self):
        if not (self.nip.isdigit() and len(self.nip) == 9):
            raise ValueError("NIP harus terdiri dari 9 digit angka.")
        return True

# Contoh penggunaan:
try:
    mahasiswa = Mahasiswa('123456799', 'John Doe', '+123456789')
    mahasiswa.validate_nim()
    mahasiswa.validate_nama()
    mahasiswa.validate_no_hp()

    dosen = Dosen('987654321', 'Jane Smith', '987654321')
    dosen.validate_nip()
    dosen.validate_nama()
    dosen.validate_no_hp()

    print("Data Mahasiswa dan Dosen valid.")
except ZeroDivisionError as e:
    print(e)
    print("error")
