print("==== welcome to JMC ( jomok Fried Chicken) ===== \n")
# Tampilkan menu
print("Menu:")

# Menu dan jenis
menu = {
    '1': ('Ayam Goreng Kripsi', 'makanan', 15000),
    '2': ('Ayam Puk Puk', 'makanan', 13000),
    '3': ('Ayam Bakar', 'makanan', 20000),
    '4': ('Es Teh', 'minuman', 5000),
    '5': ('Es Jeruk', 'minuman', 7000)
}

for kode, (nama_item, jenis, harga) in menu.items():
    print(f"{kode}. {nama_item} ({jenis}) - Rp{harga:,}")

# Ambil nama orang
customer_name  = input("\nMasukkan nama pelanggan: ")
pesanan = {}

# Input pesanan
while True:
    kode = input("\n Masukkan kode menu (1-5), atau 'done' jika selesai: ").strip()
    if kode == 'done':
        break
    if kode in menu:
        jumlah = int(input("Berapa banyak? "))
        item = menu[kode][0]  # Mendapatkan nama item dari menu
        pesanan[item] = pesanan.get(item, 0) + jumlah
    else:
        print("Kode tidak ditemukan. Coba lagi.")


subtotal = 0
pajak_total = 0

for item, jumlah in pesanan.items():
    # cari data dari menu
    for kode, (nama_item, jenis, harga) in menu.items():
        if nama_item == item:
            total_item = harga * jumlah
            if jenis == 'makanan':
                pajak = total_item *  0.05 ## buat yg 5 %
            else:
                pajak = total_item * 0.03 ## buat yg 3%
            
            subtotal += total_item
            pajak_total += pajak
                    
## total + pajak lgi 
pajak_transaksi = (subtotal + pajak_total) * 0.15
total = subtotal + pajak_total + pajak_transaksi

## tampilin
print(f"\n This is your order {customer_name} : ")

for item, jumlah in pesanan.items():
    print(f"- {item} :  {jumlah} pcs" )
    
print(f"\n Subtotal : Rp {subtotal:,} ")
print(f"pajak = {pajak_total:,}")
print(f"pajak Transaksi (15%) = {pajak_transaksi:,.1f}")
print(f"Total semua yg perlu dibayar = Rp.{total:,}")

## :, = dipakai hanya untuk formating angka agar ada tanda ribuan (100,000)

