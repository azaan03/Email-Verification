while True:
    email=input("Enter the Email to Check Email is Valid or Not :")
    if email=="exit":
        break
    k,j,c=0,0,0
    if len(email)>=6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@")==1):
                if email[-4]=="." or email[-3]==".":
                    for i in email:
                        if i==i.isspace():
                            k=1
                        elif i.isalpha():
                            if i==i.isupper():
                                j=1
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="." or i=="@":
                            continue
                        else:
                            c=1
                                
                    if k==1 or j==1 or c==1:
                        print("Email not Valid")  
                    else:
                        print("Email is Valid")      
                else:
                    print("Email not Valid")
            else:
                print("Email not Valid")
        else:
            print("Email not Valid")
    else:
        print("Email not Valid")