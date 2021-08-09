# Verilen kelimede her geçen harfi tara
# Eğer harf kelimede bir kez geçiyorsa yeni kelimeye "(" ekle
# Eğer harf kelimede birden fazla kez geçiyorsa yeni kelimeye ")" ekle

def duplicate_encode(word):
    
    lower_word = word.lower()
    newstr = ""

    for i in lower_word:                                    # Her harf için dönen döngü
        counter = 0                                         # Her harften kelimede kaç tane var sayacı
        stradded = ""
        for x in lower_word:                                # Her harf için her harfi tarayan ve sayan döngü
            if i == x:
                counter += 1

        if counter > 1:
            stradded = ")"
            newstr += stradded
        else:
            stradded = "("
            newstr += stradded

        print("Harf: " + str(i) + ", Counter: " + str(counter) + ", Encode: " + stradded)
    print("")
    print("Output: " + newstr)

duplicate_encode("Merhaba")