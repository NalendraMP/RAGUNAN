pembatas = "-----------------------------------------------"
print(pembatas)
nama_ragunan = "RAGUNAN PUTRA JAYA"
print(nama_ragunan)
ucapan = "Selamat datang di Ragunan Putra Jaya"
print(ucapan)
while True:
    try:
        umur = int(input("Silahkan Masukkan umur anda (atau 0 untuk keluar): "))
        
        if umur == 0:
            print("Terima kasih! Silahkan datang lagi.")
            break
        elif umur <= 2:
            harga = 0
        elif 3 <= umur <= 12:
            harga = 14
        elif umur >= 65:
            harga = 18
        else:
            harga = 23

        print(f"Harga tiket untuk umur {umur} adalah ${harga}")

        uang_dibayarkan = float(input("Masukkan jumlah uang yang dibayarkan: "))
        kembalian = uang_dibayarkan - harga

        if kembalian >= 0:
            print(f"Kembalian Anda adalah ${kembalian:.2f}")
        else:
            print(f"Uang yang Anda bayarkan tidak cukup. Anda kekurangan ${abs(kembalian):.2f}")

    except ValueError:
        print("Masukan tidak valid. Harap masukkan angka umur atau 0 untuk keluar.")
 
    
 