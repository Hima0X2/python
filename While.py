secret_number=9
i=1
while i<=secret_number:
    number = int(input("Guess the number?"))
    i=i+1
    if number==secret_number:
     print("You Win!")
     break
else:
    print("Sorry")
