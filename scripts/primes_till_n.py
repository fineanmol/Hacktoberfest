N = int(input("Enter the value of N :"))
print("Prime numbers between", 1, "and", N, "are:")
for num in range(1, N + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end=" ")
