def deskripsi_sederhana(pesan_terenkripsi):
    hasil = ""
    
    for karakter in pesan_terenkripsi:
        ## jika karakter adalah spasi atau tanda baca, biarkan sama (continue)
        if karakter == "" or not karakter.isalpha():
            hasil += karakter
            continue
        
        kode_ascii = ord(karakter)
        
        if 97 <= kode_ascii <= 122:
            # mundur 5 langkah, sesuai dgn soal 
            kode_baru = kode_ascii - 5 
            
            if kode_baru < 97:
                #jadi biar dia bisa mundur lgi ke z, jika uhd nyampe a
                kode_baru = kode_baru + 26
                
            hasil += chr(kode_baru)
            
        else:
            hasil += karakter
            
    return hasil

# Pesan yang terenkripsi
pesan1 = "xfqfr bfmdz"
pesan2 = "gjxtp lzj rfz ifkyfw jxi snm"
pesan3 = "gwt, gjxtp qz rfz rfpfs in bfwlty lfp?"
pesan4 = "fpz xfdfsl pfrz, rfz lfp ofin ufhfwpz"
pesan5 = "dfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu"


print("Hasil Transkripsi:")
print("1.", pesan1, "=", deskripsi_sederhana(pesan1))
print("2.", pesan2, "=", deskripsi_sederhana(pesan2))
print("3.", pesan3, "=", deskripsi_sederhana(pesan3))
print("4.", pesan4, "=", deskripsi_sederhana(pesan4))
print("5.", pesan5, "=", deskripsi_sederhana(pesan5))

# ord() = mengubah karakter menjadi kode ASCII 
# chr() = mengubah kode ASCII menjadi karakter