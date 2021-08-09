# AAAABBBCCCAAABBB Stringini bir listeye [A, B, C, A, B] şeklinde yaz
# Her tarama için taranan harfi hafızaya al 
# Bir sonraki taramada aynı harf ile karşılaşılır ise bir sonraki harfe geç
# Eğer başka bir harf ile karşılaşılırsa önceki harfi listeye yaz ve yenisini hafızaya al

def unique_in_order(iterable):
    fmem = ""
    mylist = []

    for i in iterable:
        if i != fmem:
            fmem = i
            mylist.append(i)
    
    return mylist
        

print(unique_in_order("AAAABBBCCCAAABBB"))