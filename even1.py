#Print the even numbers in the given N
N = int(input(" Enter the Number N : "))
count = 1
while count <= N:
    if count % 2 == 0:
        print(count , end ="  " )
    count += 1
