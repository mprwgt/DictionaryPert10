daftarkontak = {"Nama":"Nomor Telepon"}
kontak = {'Ari':'081267888', 'Dina':'087677776'}

print("="*30)
print("   Nama     |    Nomor Telepon   ")
print("="*30)
print(" # Ari   |   ",kontak['Ari'])
print(" # Dina  |   ",kontak['Dina'])
print("="*30)

# Menampilkan kontak Ari
print("Menampilkan kontak Ari")
print("="*30)
print(" # Ari   |   ",kontak['Ari'])
print("="*30)

#Menambahkan kontak dengan nama Lala dan nomor 087852744
print("Menambah kontak dengan nama Lala dan Nomor Telepon 087852744")
kontak['Lala']='087852744'
print("="*30)
print("  Lala   |   ",kontak['Lala'])
print("="*30)

#Mengubah kontak Dina dengan nomor baru 081222109187
print("Mengubah kontak Dina dengan nomor baru 081222109187")
kontak['Dina']='081222109187'
print("="*30)
print(" # Dina  |   ",kontak['Dina'])
print("="*30)
#Menampilkan semua nama
print("Menampilkan semua nama")
print("="*30)
print(kontak.keys())
print("="*30)
#Menampilkan semua nomor
print("Menampilkan semua nomor")
print("="*30)
print(kontak.values())
print("="*30)
#Menampilkan semua daftar kontak beserta nama dan nomornya
print("Menampilkan daftar nama dan nomor")
print("="*30)
print(kontak.items())
print("="*30)
#Menghapus kontak Dina
print("Hapus kontak Dina")
kontak.pop('Dina')
print("="*30)
print(kontak.items())
print("="*30)