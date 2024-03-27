hari=(1,2,3,44,5,6,88.99)
print(hari)
#built-in functions
print(min(hari))
print(max(hari))
print(sum(hari))
print(len(hari))

print(list(hari)) 
 
#tuple operations
#1.Concatenation
h1=(4,5,6)
h2=(7,8,9)
print(h1+h2)
print((h1,h2)*10)
new=[]
for h,j in zip(h1,h2):
    new.append(h+j)
    print(tuple(new))

#2.repetition
print(h1*10)
print(h2*10)


#3.Membership
h=(23,45,6,7800,23345,677,67)
print(1 not in h)

h1=(1,2,3,4,5)
h3=(123,45667,7,7,88)
print(h1 in h3)

h3=(123,45667,7,7,88)
for i in h3:
    print(i)
    
  

#Atm
name="harikumar"
Password="144"
username=input("Enter the username:")
passwords=input("Enter the password:")
h='''
   1.credit
   2.debit
   3.mini statement
   4.exit
   '''
Amount=30000
if name==username and Password==passwords:
    while True:
        print(h)
        option=int(input("Enter your option:"))
        if option==1:
            credit_Amount=float(input("Enter the Amount:"))
            print("Amount after credited:",Amount+credit_Amount)
        elif option==2:
            debit_Amount=float(input("Enter the Amount:"))
            print("Amount after debited:",Amount-debit_Amount)
        elif option==3:
            print("Your Account is under dominant condition:",Amount)
        elif option==4: 
            break
else: 
    print("InValid")
    
hari=(1,2,3,44,5,6,88.99)
print(seq(hari))  

