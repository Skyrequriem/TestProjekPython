print("=== Kalkulator Sederhana ===")

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
operasi = input("Masukkan operasi : ")

if operasi == "+":
    hasil = angka1 + angka2
elif operasi == "-":
    hasil = angka1 - angka2
elif operasi == "*":
    hasil = angka1 * angka2
elif operasi == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error: Tidak bisa membagi dengan 0!"
else:
    hasil = "Operasi tidak valid."

print("Hasil:", hasil)
