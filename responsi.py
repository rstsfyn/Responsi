#RESTU SOFYAN MAARIF

beli = []
barang =[]
diskon=a=total=diskon_tambah=jmlh_brg = 0 
def convert_int(text):
    try:
        var = int(input(text))
    except:
        print("Hanya Masukan Angka Saja")
    return var

#Bagian Admin
def bagianAdmin():
    global diskon
    global diskon
    while True:
        print("="*30)
        print("==========MENU ADMIN==========")
        print("""
            1. Input Data Barang
            2. Input Diskon Barang
            3. Exit
            """)
        print("="*30)
        pilihan = int(input("Masukan Pilihan Menu: "))
        if pilihan == 1:
            inputKodeBarang = input("Masukan Kode Barang: ")
            inputNamaBarang = input("Masukan Nama Barang: ")
            inputHargaBarang = int(input("Masukan Harga Barang: "))
            dataBaru = []
            dataBaru.append(inputKodeBarang)
            dataBaru.append(inputNamaBarang)
            dataBaru.append(inputHargaBarang)
            barang.append(dataBaru)
        elif pilihan == 2:
            diskon = convert_int("Masukan diskon barang: ")
        else:
            print("Tidak Ada Pilihan")
            break
        
#Bagian Pelanggan
def bagianPelanggan():
    while True:
        print("="*30)
        print("========MENU PELANGGAN========")
        print("""
            1. Lihat Data Barang
            2. Input Barang Berdasarkan Nama Barang
            3. Menu Bayar
            4. Exit
            """)
        print("="*30)
        pilihan = int(input("Masukan Piliahan menu: "))
        if barang != []:
            if pilihan == 1:
                for i in barang:
                    print("Kode Barang  : ",i[0])
                    print("Nama Barang  : ",i[1])
                    print("Harga Barang : ",i[2])
            elif pilihan == 2:
                ulang = True
                while ulang:
                    namaBarang = str(input("Masukan Nama Barang yang ingin di Input: "))
                    for i in barang:
                        if i[1] == namaBarang:
                            qty = convert_int("Masukan Jumlah barang yang dibeli :")
                            tmp = i.copy()
                            tmp.append(qty)
                            beli.append(tmp)
                            lagi = input("Apakah ingin membeli lagi ? [y/t]")
                            if lagi == 'y':
                                break
                            elif lagi == 't':
                                ulang = False
                                break
                    else:
                        print("Maaf Barang yang Anda Cari tidak ditemukan")
                        break
            elif pilihan == 3:
                global a,total,diskon_tambah,jmlh_brg
                print("="*30)
                print("=========SRUK BELANJA=========")
                print("Barang Yang Anda Beli :")
                for i in beli:
                    a+=1
                    print(a," Kode Barang   : ",i[0])
                    print("   Nama Barang   : ",i[1])
                    print("   Harga Barang  : ",i[2])
                    print("   Qty Barang    : ",i[3])
                    total += i[2] * i[3]
                    jmlh_brg += i[3]
                if jmlh_brg > 10:
                    diskon_tambah = 20000
                elif jmlh_brg > 5:
                    diskon_tambah = 10000
                print("Harga total      :",total)
                print("Diskon           :",diskon)
                print("Diskon tambahan  :",diskon_tambah)
                print("Total Bayar      :",total - diskon - diskon_tambah)
                print("="*30)
                break 
        else:
            print("Tidak Ada Piliha Menu")
            break
        
#Bagian Menu UTAMA
while True:
    print("="*30)
    print("==========MENU UTAMA==========")
    print("""
        1. Menu Admin
        2. Menu Pelanggan
        3. Exit
        """)
    print("="*30)
    pilihanmenu = int(input("Pilih Menu: "))
    if pilihanmenu == 1:
        bagianAdmin()
    elif pilihanmenu == 2:
        bagianPelanggan()
    else:
        print("Terimaksih Telah Menggunakan Menu ini")
        break
        
  #MENUJU TAK TERBATAS MELAMPAUINNYA
