inp_ph=input("enter your phrase: ")
w=0
n=0
word=" "
spac_loc=inp_ph.find(" ")
print(spac_loc)
while spac_loc!=-1:
    if inp_ph[n].isalpha():
        #print("Yes it is alpha")
        if inp_ph[n].lower()>"g":
            #print("Yes it is greater than g")
            while n!=spac_loc:
                word=word+inp_ph[n]
                n=n+1
            print(word)
            word=" "
            n=spac_loc+1
            spac_loc=inp_ph.find(" ",n+1)
        else:
            n=spac_loc+1
            spac_loc=inp_ph.find(" ",n+1)
