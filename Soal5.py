word = "naiplovyu"
result = set() ## buat naro data nanti

def recursion(sisa, path):
    for i in range(len(sisa)):
        kombinasi = path + sisa[:i] ## knp pakai [:1] = karena buat nampung semua angka sisa sebelum i. 
        
        if 1 <= len(kombinasi) <= 6:
            result.add(kombinasi)
        recursion(sisa[:i] + sisa[i+1:], kombinasi)
    
# Memanggil buat_permutasi dan langsung menampilkan hasil total
recursion(word, "")
print("Total kemungkinan username:", len(result))

## print usernamenya : 
# for username in sorted(result):
#     print(username)
##misal "abc", ambil a . maka sisa jadi "bc", path jadi "a". 

## jadi path disini buat temporary nampung, jadi awalnya path "", lalu nanti jika loop proses maka path bisa jadi akan "i", "n" 