def find_duplicat(arr):
    angka_set = set()
    
    for num in arr:
        if num in angka_set:
            return True
        else:
            angka_set.add(num)
            
    return False ##  there's no duplicate 
    

angka = [20, 1, 3, 2, 4, 6, 8, 5, 7, 9, 11, 13, 15, 10,  12, 14, 16, 18, 20, 17, 19]
print(find_duplicat(angka))