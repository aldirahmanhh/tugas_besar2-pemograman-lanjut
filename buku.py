class Buku:
    def __init__(self, judul, penulis, penerbit, tahun_terbit, konten, iktisar):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.konten = konten
        self.iktisar = iktisar

    def read(self, halaman):
        try:
            print(f"Konten dari halaman 1 sampai {halaman}:")
            for i in range(halaman):
                print(self.konten[i])
        except IndexError:
            print("Halaman melebihi batas konten buku.")

    def __str__(self):
        return f"{self.judul} by {self.penulis}"
