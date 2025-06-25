def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num >= 1:
                return num
            else:
                print ("Please enter a number 1 or greater.")
        except ValueError:
            print ("Invalid input. Please enter a number.")

def sing(starting_number):
    for bottles in range (starting_number, 0, -1):
        if bottles > 1:
            print (f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            next_bottles = bottles - 1
            if next_bottles == 1:
                print(f"Take one down, pass it around, 1 bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {next_bottles} bottles of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")   






