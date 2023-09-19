#1
hours= int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

salary1 = hours * rate

print("Salary: ", salary1)


#2 
celsius1 = int(input("Enter Celsius Temperature: "))

print("Fahrenheit Temperature :", celsius1 * 9 / 5 + 32)

#3
sec_input1 = int(input('Enter seconds: '))

hour = sec_input1 // 3600 
minute = (sec_input1 % 3600) // 60
second = (sec_input1 % 3600) % 60

print( sec_input1, "second(s) is", hour , "hour(s)", minute, "minute(s)",second, "second(s)\n" )
