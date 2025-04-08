def calculation(Num_list):
    Num_min = min(Num_list)
    Num_max = max(Num_list)
    average = sum(Num_list) / len(Num_list)
    
  
    ## return[min, max, average]
    
    def removal_decimal(value):
        return int(value) if value.is_integer() else round(value, 1)
    
    return[removal_decimal(Num_min), removal_decimal(Num_max), removal_decimal(average)]
    

# input1 = input("Masukan angka : ")
# Num_list = list(map(int, input1.split()))

## or 
# Num_list = list(map(int, input("Masukan angka : ").split()))

Num_list = [4.5, 2.0, 1.5, 3.0, 2.5, 4.0, 5.0, 3.5, 2.0, 1.0]

result = calculation(Num_list)
print(result)
    