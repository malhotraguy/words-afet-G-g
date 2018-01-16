phrase_inp=input("enter your phrase: ")
work=""
for word in phrase_inp:
    if word.isalpha():
        work=work+word
        
        
    else:
        
        if work.lower()>="h":
            print(work.upper())
            work=""
        else:
            work=""
            
