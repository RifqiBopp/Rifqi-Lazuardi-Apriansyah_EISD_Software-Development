import re 

def palindrome(text):
    clean_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower() ## (r'[^a-zA-Z0-9]') = cari yg bukan a-z , A-Z , 0-9  . # re.sub(pattern, replacement, string)
    
    if clean_text == clean_text[::-1]: ## (::-1) = (start:end:step) 
        return "eureeka!"
    else:
        return "suka blyat"
    
    

text_list = ["Angsa",
             "KataK", 
             "kasur empuk", 
             "Aku Suka Kamu", 
             "Ibu Ratna antar ubi."]


for text in text_list:
    result = palindrome(text)
    print(result)