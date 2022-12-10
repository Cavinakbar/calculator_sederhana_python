#kalkulator sederhana dari python
print(10*"-" + "SELAMAT DATANG DI KALKULATOR SEDERHANA INI"+ 10*"-")
angka1 = int(input("masukkan angka pertama:"))
angka2 = int(input("masukkan angka kedua  :"))
operator = input("""
-----keterangan-----
perkalian   = kali
perkurangan = kurang
pertambahan = tambah
pembagian   = bagi
perpangkatan= pangkat
Masukkan keterangan yang kamu mau:""")

if operator.lower()==("kali"):
    hasil = angka1 * angka2
    print(f"Hasil: {hasil}")

elif operator.lower()==("tambah"):
    hasil = angka1 + angka2
    print(f"Hasil: {hasil}")

elif operator.lower()==("bagi"):
    hasil = angka1 / angka2
    print(f"Hasil: {hasil}")

elif operator.lower()==("pangkat"):
    hasil =angka1 ** angka2
    print(f"Hasil: {hasil}")

elif operator.lower()==("kurang"):
    hasil =angka1 - angka2
    print(f"Hasil: {hasil}")
else:
    print("keterangan anda salah")
print("TERIMAKASIH TELAH MENGGUNAKAN KALKULATOR SEDERHANA INI")