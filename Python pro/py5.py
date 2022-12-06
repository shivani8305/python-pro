#password generator
import random
s=""
password=[]
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
characters = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
print("Welcome to the Password Generator")
alpha = int(input("How many letters would you like to have in your password?\n"))
num = int(input("How many numbers would you like to have in your password?\n"))
char = int(input("How many characters would you like to have in your password?\n"))
for a in range(0, alpha):
    password.append(random.choice(letters))
for z in range(0, num):
    password.append(random.choice(numbers))
for y in range(0, char):
    password.append(random.choice(characters))
random.shuffle(password)

for n in range(0, len(password)):
    s+=password[n]
print(f"Your password is: {s}")    
       
          