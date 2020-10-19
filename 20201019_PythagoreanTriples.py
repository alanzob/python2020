# Recreated a program I made to help find Pythagorean Triples for 9th grade Geometry class
# for extra credit in 1999
a=1
b=1
c=1

while a<100:
    b=1
    while b<100:
        c=1
        while c<100:
            if ((a*a)+(b*b))==(c*c) and b>a:
                print (str(a)+","+str(b)+","+str(c))
            c=c+1
            pass 
        b=b+1
        pass 
    a=a+1
    pass

