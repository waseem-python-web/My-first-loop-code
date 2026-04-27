email = input("Enter your Gmail.com: ")

if len(email) >= 8:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:
            if email.endswith(".com"):
                
                invalid = 0
                for i in email:
                    if i.isalnum():
                        continue
                    elif i in ["@", "_", "."]:
                        continue
                    else:
                        invalid = 1
                        break

                if invalid == 0:
                    print("Valid Gmail ✅")
                else:
                    print("Invalid Character ❌")
            else:
                print("Must end with .com ❌")
        else:
            print("Invalid @ usage ❌")
    else:
        print("First letter must be alphabet ❌")
else:
    print("Too short email ❌")











"""email = input("Enter your Gmail.com :")
k = 0
j = 0
d = 0
if len(email) >= 8:
    pass

    if email[0].isalpha():
        pass
        if ("@"in email) and (email.count("@") == 1) :
            if (email[-4] == ".") ^(email[-3] == "."):
                for i in email:
                    if i==i.isalpha():
                     
                        k = 1
                    elif i.isalpha():
                        if i.upper():
                            j =1

                    elif i.isdigit(): 
                        continue
                    elif i == "_" or i =="."  or i =="@":
                        continue  
                    else:
                        d = 1    

                if k == 1 or j==1  or d ==1:
                    print("wrong mail.com")
            else:
                print("wrong gmail.com")
        else:
            print("wromg Gmail.com")   
       
    else:
        print("wrong Gmail.com") 


else:
    print("wrong Gmail")
"""