# Verilen sayıyı kendi basamakları ile çarp: 29 2 * 9 = 18, 1 * 8 = 8
# Eğer çıkan sonuç tek basamaksa direk döndür

def persistence(n):
    counter = 0
    mylist = []

    while len(str(n)) != 1:             # n'in uzunluğu 1 olunca dur
        for i in str(n):                # Bütün haneleri bir listeye koy
            mylist.append(i)
    
        #print(n)
        result = 1
        for x in mylist:                # Bütün haneleri birbiri ile çarp
            result *= int(x)
            n = result
            mylist = []
            #print(result)
    
        counter += 1
    
    return counter
