# TUGAS BESAR KELOMPOK 5
# ~PROGRAM VENDING MACHINE~
 
# Import
import os
from time import sleep

'''INISIALISASI'''
# KAMUS
# produk = arr of string 
# stok_barang, pemesanan, list_of_pecahan = arr of int
# kode, harga_total, uang, kembalian = int
# idx, i = int
# pecahan = dictionary of (string: int)
# cancel_atau_lanjut, metode = string
# kode_rahasia = string


# Inisialisasi Array Nama Produk dan Harga Produk
produk = ["Chitatho", "Yakul", "Akua", "The pucuk", "Nescafo", "Poup mie", "Cola", "No Green Tea",
          "Hypermilk", "Pocahri", "Pocki", "Silverking"]

harga = [2000, 3000, 4000, 5000, 6000, 6000, 7000, 7000, 7000, 8000, 11000, 14000]

pemesanan = [0 for i in range(len(produk))]

# Membuat File Text yang Berisi Daftar Stok Barang Jika Belum Ada
if not os.path.exists("vend_mach_data.txt"):
    file = open("vend_mach_data.txt", "x")
    file = open("vend_mach_data.txt", "a")
    for i in range(12):
        file.write("10\n")

# Read Text File Stok Barang
file = open("vend_mach_data.txt", "r")
stok_barang = file.readlines()
file.close()

# Membenarkan Element Stok Barang Menjadi Integer
for i in range(len(stok_barang)):
    stok_barang[i] = int(stok_barang[i].strip())

'''FUNGSI'''

# Formatting
def justify(seperator, number, word1, word2, word3):

# Kamus = semuanya parameter berupa string
    seperator = str(seperator)
    number = str(number) 
    word1 = str(word1)
    word2 = str(word2)
    word3 = str(word3)

    print(number, word1, end = "")
    for i in range(40 - len(number) - len(word1) - len(word2)):
        print(seperator, end = "")
    print(word2, word3)

# Tampilkan qr code
def draw_qr():                           
    print("▄▄▄▄▄▄▄ ▄▄         ▄▄ ▄▄▄▄▄▄▄  ")
    print("█ ▄▄▄ █ ▄  ▄▄▄▀ █▀ ▄▄ █ ▄▄▄ █  ")
    print("█ ███ █ ██▄█▀███▄▀▀▄▀ █ ███ █  ")
    print("█▄▄▄▄▄█ ▄▀▄ ▄▀█ █ █▀▄ █▄▄▄▄▄█  ")
    print("▄▄▄▄  ▄ ▄▀ ▄▀ ████ ▄▀▄  ▄▄▄ ▄  ")
    print("▄▄▀ ▀▄▄▄▄▀ █▄   ▀▄▀▀ █▀█▀█▄█▀  ")
    print(" ▀ █▀ ▄█▄▄ ▀▀██▀ ▄ ▀█▀   ▄▄    ")
    print("█▀▄█ ▄▄▀█▀█ █▄▄▀▀▄▄█▄ ▀█ ▄███  ")
    print("▀█▄ █ ▄ ██▀▀ ▄▄▄▀ ███▄ ▄█  ▄   ")
    print("▄  █▀ ▄ ▄▄█▀█▀ █▄   █▀ ▀ ▀     ")
    print(" ▄█ ▀▀▄█▄▄ ▀▀ █▀███ █▄█▄███▄▀  ")
    print("▄▄▄▄▄▄▄ ▀█▀█ ▀█ ▀ ▄██ ▄ ██ █   ")
    print("█ ▄▄▄ █  █▀ ▄██▄▀▄  █▄▄▄█ ▄█▀  ")
    print("█ ███ █ █▀  ▄▀█▀▄▀▄▄▀▀ █▀▀▄▀█  ")
    print("█▄▄▄▄▄█ █ █▄▄▄▀ ▄ ▄ █▄  ▄▀ █   ")
    print()

# Tampilan Vending Machine
def draw_vending_machine():
    justify(" ", "No.", "Produk", "Harga", "Stok")
    for idx in range(12):
        justify("-", idx+1, produk[idx], harga[idx], stok_barang[idx])
    print()

# Mode Refill
def mode_refill():
    draw_vending_machine()
    print("Selamat datang di mode refill!")

    while True:
        kode = int(input("Pilih kode produk mana yang ingin di refill (0 untuk keluar, 13 untuk refill semuanya): ")) - 1
        if kode == -1:
            break

        elif kode == 12:
            for i in range(12):
                stok_barang[i] = 10
            print("Berhasil! Semua produk sudah di refill.")
            print()
            break

        elif 0<=kode<=11:
            stok_barang[kode] = 10
            print(f"Berhasil! {produk[kode]} sudah di refill.")
            print()

        else:
            kode = int(input("Error, masukkan kode 0-13: "))
    
    # Update Stok Barang
    file = open("vend_mach_data.txt", "w")
    file.write("")
    file.close()

    file = open("vend_mach_data.txt", "a")
    for i in range(12):
        file.write(f"{stok_barang[i]}\n")
    file.close()

    # Selesai
    draw_vending_machine()
    print("Telah keluar mode refill, stok barang sudah ter-update.")
    
# Hitung Kembalian
def hitung_kembalian(kembalian):

    # Dictionary kembalian
    pecahan = {"pecahan_50": 0, "pecahan_20": 0, "pecahan_10": 0, "pecahan_5": 0,
               "pecahan_2": 0, "pecahan_1": 0}
    
    # Hitung masing-masing pecahan
    pecahan["pecahan_50"] = kembalian // 50_000
    kembalian %= 50_000

    pecahan["pecahan_20"] = kembalian // 20_000
    kembalian %= 20_000

    pecahan["pecahan_10"] = kembalian // 10_000
    kembalian %= 10_000

    pecahan["pecahan_5"] = kembalian // 5_000
    kembalian %= 5_000

    pecahan["pecahan_2"] = kembalian // 2_000
    kembalian %= 2_000

    pecahan["pecahan_1"] = kembalian // 1_000

    return list(pecahan.values())

'''ALGORITMA INTI'''

# Print UI
os.system("CLS")
draw_vending_machine()
print("Selamat datang di Vending Machine Kelompok 5!")
print("Mau beli apa?")
print("Masukkan 0 untuk selesai dan lanjut ke pembayaran")

# Inisialisasi harga awal
harga_total = 0

# Inisialisasi kode rahasia
kode_rahasia = "12345"
# Sebenearnya kodenya 12345, tetapi harus dikurangi 1 karena input kode dikurangi 1

# Input terus
while True:

    # Input kode
    kode = input("Masukkan kode barang yang ingin dibeli (0 untuk selesai dan lanjut ke pembayaran): ")

    # Jika Kode rahasia untuk mode refill
    if kode == kode_rahasia:
        os.system("CLS")
        mode_refill()
        exit()

    # Jika kode salah
    if kode not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
        print()
        print(f"Error, kode tidak terbaca!")
        print()
    
    else:
        # kode nya dijadiin integer
        kode = int(kode) - 1

        # Jika customer memasukkan 0 tetapi belum membeli apa-apa
        if kode == -1 and harga_total == 0:
            print("Anda belum beli apa-apa... ")
            kode = int(input("Apakah tetap ingin quit? Masukkan 0 kembali untuk keluar: "))
            if kode == 0:
                print("Terima kasih telah menggunakan vending machine ini!")
                print("Selamat datang kembali")
                exit()
            else:
                pass

        # Customer sudah selesai, lanjut bayar
        elif kode == -1:
            print()
            break
        
        # Pemesanan benar
        elif 0 <= kode <= 11:
            
            # Jika stoknya gaada
            if stok_barang[kode] == 0:
                print(f"Mohon maaf, stok {produk[kode]} sedang habis, silakan beli produk lain.")

            # Input jumlah yang ingin dibeli hingga benar
            else:
                jumlah = int(input(f"Masukkan jumlah dari {produk[kode]} yang ingin dibeli: "))

                # Jika stok memenuhi
                if stok_barang[kode] >= jumlah:
                    
                    # Tambah ke harga total
                    harga_total += jumlah * harga[kode]

                    # Kurangi stok dengan jumlah yang dibeli
                    stok_barang[kode] -= jumlah

                    # Tambahkan ke array pemesanan
                    pemesanan[kode] += jumlah

                    # Print harga total
                    print(f"Harga total = {harga_total}")

                # jika stok tidak cukup
                else:
                    print(f"Mohon maaf, stok {produk[kode]} tidak mencukupi, silakan beli produk lain.")
        
        # Kode tidak sesuai
        else:
            print("Error, kode yang Anda masukkan tidak sesuai. Silakan memasukkan input kembali.")
            sleep(0.5)

        print()


# PEMBAYARAN
# Print Daftar harga barang (struk pembayaran)
os.system("CLS")
justify("-", "Jumlah", "Produk", "Harga", "")
for i in range(len(pemesanan)):
    if pemesanan[i] != 0:
        justify("-", str(pemesanan[i]) + " x   ", produk[i], harga[i]*pemesanan[i], "")
justify("-", "Total", "", harga_total, "")
print()

# Lanjut ke pembayaran atau tidak
cancel_atau_lanjut = input("Apakah ingin lanjut ke pembayaran atau cancel? lanjut/cancel:  ")
while cancel_atau_lanjut not in ["cancel", "lanjut"]:
    print("Error, silakan input kembali.")
    cancel_atau_lanjut = input("Apakah ingin lanjut atau cancel: ")

# Tidak
if cancel_atau_lanjut == "cancel":
    print(f"Terima kasih telah menggunakan vending machine ini!")
    print(f"Selamat datang kembali!")
    exit()

# Lanjut
elif cancel_atau_lanjut == "lanjut":

    # Pilih metode pembayaran
    metode = input("Masukkan metode pembayaran tunai/nontunai: ")
    while metode not in ["tunai", "nontunai"]:
        metode = input("Error, masukkan metode pembayaran tunai/nontunai: ")
    print()

    if metode == "tunai":

        # Input uang
        uang = int(input("Masukkan nominal uang pembayaran (hanya menerima keliapatan Rp10.000): "))
        
        # Jika uang masih salah:
        while (uang % 10_000 != 0) or (uang < harga_total):

            # Jika uang bukan keliapatan 10.000
            if uang % 10_000 != 0:
                uang = int(input("Error, masukkan nominal uang dengan kelipatan Rp10.000: "))

            # Jika uang tidak mencukupi
            else:
                uang = int(input("Waduh, uang Anda tidak cukup, silakan memasukkan kembali nominal uang: "))

        # Hitung kembalian
        kembalian = uang - harga_total
        pecahan = ["Rp50.000", "Rp20.000", "Rp10.000", "Rp5.000", "Rp2.000", "Rp1.000"]

        if kembalian != 0:
            list_pecahan = hitung_kembalian(kembalian) 

        # Ini biar keliatan keren
        print("Pembayaran sedang diproses.", end= " ")
        for i in range(3):
            print(".", end = " ")
            sleep(0.7)
        print()
        print()

        # Output pecahan uang
        if kembalian != 0:
            print(f"Kembalian Anda adalah Rp{kembalian} dengan rincian kembalian berikut: ")
            for i in range(len(pecahan)):
                if list_pecahan[i] != 0:
                    justify("", str(list_pecahan[i]) + "x", pecahan[i], "", "")
            print()
        else:
            print("Berhasil, Anda membayar dengan uang pas!")

    # Ini juga biar keliatan keren
    elif metode == "nontunai":
        draw_qr()
        print(f"Silakan menscan QR code diatas.")
        input(f"Masukkan kode pembayaran: ")

        print("Pembayaran sedang diproses.", end= " ")
        for i in range(3):
            print(".", end = " ")
            sleep(0.7)
        print()

# Output
print("Selesai! Terima kasih telah menggunakan vending machine ini!")
print("Selamat datang kembali")

# Update Stok Barang
file = open("vend_mach_data.txt", "w")
file.write("")
file.close()

file = open("vend_mach_data.txt", "a")
for i in range(12):
    file.write(f"{stok_barang[i]}\n")
file.close()