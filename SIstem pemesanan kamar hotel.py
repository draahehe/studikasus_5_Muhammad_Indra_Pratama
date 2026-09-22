def hitung_biaya(harga, lama_menginap):
    total = harga * lama_menginap
    return total

while True:
    print("====== Selamat Datang Di ======")
    print("=== Sistem Pemesanan Hotel ===\n")
    print("Daftar menu yang tersedia")
    print("1. Kamar Standard (Rp200.000/malam)")
    print("2. Kamar Deluxe   (Rp350.000/malam)")
    print("3. Keluar")

    pilihan = int(input("Pilih jenis kamar (1/2), Pilih 3 jika ingin keluar dari sistem : "))

    if pilihan == 1:
        nama_kamar = "Standard"
        harga = 200000
    elif pilihan == 2:
        nama_kamar = "Deluxe"
        harga = 350000
    elif pilihan == 3:
        print("Terima kasih telah menggunakan sistem ini.")
        break
    else:
        print("Pilihan tidak tersedia, coba lagi.")
        continue

    lama_menginap = int(input("Masukkan lama menginap (malam): "))
    total_biaya = hitung_biaya(harga, lama_menginap)

    print("\n===== Detail Pemesanan Kamar =====")
    print(f"Jenis Kamar   : {nama_kamar}")
    print(f"Lama Menginap : {lama_menginap} malam")
    print(f"Total Biaya   : Rp{total_biaya:,}")