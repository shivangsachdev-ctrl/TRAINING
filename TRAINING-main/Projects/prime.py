
for n in range(2025,2075):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'is a product of', x, '*', n//x)
            break
    else:
        print (n, 'is a product of itself')




    
