lower_limit = int(input("Enter Lower limit: "))

Upper_limit = int(input("Enter Upper limit: "))

sum=0

for i in range(lower_limit,Upper_limit+1):
    sum=sum+i

print("Addition of numbers = ",sum)
