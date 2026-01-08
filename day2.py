# Tugas 1 : Menentukan Bilangan Genap atau Ganjil

# n = int(input("Masukkan Angka : "))

# if n % 2 == 0:
#     print("Angka", n, "adalah bilangan Genap")
# else:
#     print(f"Angka {n} adalah bilangan Ganjil")


# Tugas 2 : Diskon Belanja

# total_belanja = int(input("Masukkan total belanjaan Anda: "))
# if total_belanja >= 500_000:
#     print("Selamat! Anda mendapatkan diskon 20%")
#     diskon = int(total_belanja * 0.2)
# elif total_belanja >= 250_000:
#     print("Selamat! Anda mendapatkan diskon 10%")
#     diskon = int(total_belanja * 0.1)
# elif total_belanja >= 100_000:
#     print ("Selamat! Anda mendapatkan diskon 5%")
#     diskon = int(total_belanja * 0.05)
# else:
#     print("Maaf, Anda tidak mendapatkan diskon")
#     diskon = 0

# print("Total Awal Belanjaan Anda: Rp", total_belanja)
# print("Total Diskon Anda: Rp", diskon)
# print("Total yang harus Anda bayar: Rp", total_belanja - diskon)

# Tugas 3 : Membuat form Login

username = "user123"
password= "pass123"

attempts = 3

while attempts > 0:
    input_username = input("Masukkan username: ")
    input_password = input("Masukkan password: ")

    if input_username == username and input_password == password:
        print(f"Login berhasil! Selamat datang, {input_username}")
        break
    else:
        attempts -= 1

        if input_username == username and input_password != password:
            print("Login gagal! Password salah.")
        elif input_username != username and input_password == password:
            print("Login gagal! Username salah.")
        else:
            print("Login gagal! Username dan password salah.")

        if attempts > 0:
            print(f"Sisa percobaan: {attempts}\n")
        else:
            print("Akses diblokir! Anda telah gagal login 3 kali.")

