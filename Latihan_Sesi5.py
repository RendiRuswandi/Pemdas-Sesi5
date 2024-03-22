#Latihan Looping & While

# 1)
print ("No 1")
for i in range(1,6, 2):
    print(f"{i}.Aku Cinta Indonesia")
    
# 2)
print ("No 2")
a = 2
b = 2
max = 6
for i in range(max):
    print(a, end="")
    a += b
    b += 1
    
# 3)
print (" ")
print ("No 3")
for i in range(1,4):
    print(f"{i} X 1 = {1*1}")
    
# 4)
print ("No 4")
a = 7
b = 6
c = 42
for i in range (5):
    print(a, end=" ")
    a += b
    b += 1
    c += 7
    
# 5)
print (" ")
print ("No 5")
a = " * * * * "
b = 1
for i in range (3):
    print (a, end=" \n")
    b += 1

# 6)
print ("No 6")
a = 3
b = 4
for i in range (1, a +1):
    for j in range ( b):
        print (i, end="")
    print ( )
    
# 7)
print ("No 7")
a = 1
b = 1
c = b
for i in range (10):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# 8)
print (" ")
print ("No 8")
a = 1
b = 2
c = 3
print(a, end=" ")
print(b, end=" ")
print(c, end=" ")
for i in range(7) :
    d = a + b + c
    print(d, end=" ")
    a = b
    b = c
    c = d
    
# 9)
print (" ")
print ("No 9")
a = 4
for i in range(a, 0, -1):
    for j in range(i):
        print("1", end=" ")
    print( )

# 10)
print (" ")
print ("No 10")
for i in range(5):
    print()
    for j in range(5, i, -1):
        if i % 2 == 0:
            if j % 2 == 0:
                print(3, end=" ")
            else :
                print(2, end=" ")
        else :
            if j & 2 != 0:
                print(3, end=" ")
            else :
                print(2, end=" ")