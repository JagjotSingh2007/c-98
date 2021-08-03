def swap() :
    f1=input("ENTER FIRST FILE NAME")
    f2=input("ENTER SECOND FILE NAME")
    with open(f1,"r") as a :
        d1 = a.read()

    with open(f2,"r") as b :
        d2 = b.read()
    with open(f1,"w") as a :
        a.write(d2)
    with open(f2,"w") as b :
        b.write(d1)
swap()