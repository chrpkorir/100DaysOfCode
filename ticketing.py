print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age?\n"))

    if age < 12:
        bill = 5
        print("Children tickets are $5.")

    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")

    else:
        bill = 12
        print("Adult tickets are $12.")

    want_photo = input("Do you want a photo taken? Y or N\n")
    # Add $3 for a photo
    if want_photo == "Y" or "y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")