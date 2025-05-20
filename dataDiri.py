data = ('Putuyandirah Eliqohen Duka', '71241145', 'Gondokusuman, DI Yogyakarta')

# Menampilkan NIM, NAMA, dan ALAMAT
print("NIM    :", data[1])
print("NAMA   :", data[0])
print("ALAMAT :", data[2])

# Mengubah NIM menjadi tuple karakter
nim_tuple = tuple(data[1])
print("NIM :", nim_tuple)

# Mengambil nama depan (kata pertama) dan dijadikan tuple karakter
nama_depan = tuple(data[0].split()[0])
print("NAMA DEPAN:", nama_depan)

# Membalik urutan nama (dari belakang ke depan)
nama_terbalik = tuple(reversed(data[0].split()))
print("NAMA TERBALIK:", nama_terbalik)
