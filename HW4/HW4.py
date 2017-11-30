


def multiplication_table(m, n):
    for i in range(1,10):
        print()
        for ix in range(m,n+1):
            print("%d x %d = %2d" % (ix,i,ix*i),end="     ")
    print()



def pyramid(n):
    for i in range(n):         
        for j in range(n - i - 1): 
                 print(" ", end = "")
        for k in range(i + 1):                
                print("\ ", end = "" )
        print()     

        