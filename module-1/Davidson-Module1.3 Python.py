# Author: Tiffany Davidson
# Assignment: Module 1.3 - On the Wall + Flowchart
# Description: Countdown bottles of beer and remind user to buy more

def countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
        print(f"Take one down and pass it around, {bottles} bottle(s) of beer on the wall.\n")

    if bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")

def main():
    bottles = int(input("Enter number of bottles: "))
    countdown(bottles)
    print("Time to buy more beer!")

if __name__ == "__main__":
    main()
