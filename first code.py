name = input("What is your name?").capitalize()
print("Hi", name, ", how are you doing today?")
num = int(input("Enter a number: "))
dur = int(input("Till which number?"))
for i in range(1, dur+1):
    print(f"{num} x {i} = {num*i}")