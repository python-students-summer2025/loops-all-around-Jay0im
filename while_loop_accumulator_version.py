
def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num >= 1:
                return num
            else:
                print("Please enter a number 1 or greater.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def sing(starting_number):
    bottles = starting_number
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            bottles -= 1
            if bottles == 1:
                print(f"Take one down, pass it around, 1 bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {bottles} bottles of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
            bottles -= 1
