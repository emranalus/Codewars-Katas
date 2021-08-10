# Verilen sayı arrayi sayılardan birisi diğerlerinden farklıdır
# Bütün diğer sayılar 2 ile tam bölünürken 1 tanesi bölünmez veya
# Bütün diğer sayılar 2 ile tam bölünemezken 1 tanesi bölünür
# Bu sayıyı bulup arraydeki konumunu 1'den saymaya başlayarak döndür

def iq_test(numbers):
    mylist = numbers.split(' ')
    evenlist = []
    oddlist = []
    counter = 0

    for i in mylist:                                    # Verilen arrayin hepsini tara
        even = int(i) / 2

        if int(i) == int(even) * 2:                     # Bir sayının ikiye bölünebilirliğini test ediyor
            evenlist.append(i)
            print(str(i) + " is Even")                  # Eğer bölünebiliyorsa
        else:
            oddlist.append(i)
            print(str(i) + " is Odd")                   # Eğer bölünemiyorsa

    if len(oddlist) > len(evenlist):                    # Eğer Odd sayıların sayısı Even sayılardan fazla ise
        for x in mylist:                                # Girdiyi tara
            counter += 1                                # Even'ımıza ulaşa ne kadar kaç basamak geçti(1'den başla)
            if evenlist[0] == x:                        # Eğer evenlistin ilk üyesi x'e eşitse saymayı bırak
                break
    else:                                               # Eğer değilse
        for x in mylist:                                # Girdiyi tara
            counter += 1                                # Even'ımıza ulaşa ne kadar kaç basamak geçti(1'den başla)
            if oddlist[0] == x:                         # Eğer evenlistin ilk üyesi x'e eşitse saymayı bırak
                break

    return counter
