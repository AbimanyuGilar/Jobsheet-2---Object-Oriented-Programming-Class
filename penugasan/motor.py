import parkir

class Motor:
  def __init__(self, plat, merk, tipe, pemilik):
    self.plat = plat
    self.merk = merk
    self.tipe = tipe
    self.pemilik = pemilik
    self.lama_parkir = 0
  
  def parkir(self):
    parkir.registrasi(self)

  def keluar_parkir(self):
    parkir.keluar_parkir(self)

  def desc(self):
    hasil = f'''
      Plat Nomor: {self.plat}
      Merk: {self.merk}
      Tipe: {self.tipe}
      Pemilik: {self.pemilik}
    '''
    print(hasil)

  def lihat_pemilik(self):
    return f'Pemilik dari motor ini adalah {self.pemilik}'

  
    