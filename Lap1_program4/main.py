n = 1
sum=0
time=0
while n != 0:
 n=int(input('Enter numbers to calculate their sum and average. Enter 0 to exit: '))
 if n==0:
     break
 sum=sum+n
 time+=1
 print('Sum = ', sum ,' Average = ', sum/time)