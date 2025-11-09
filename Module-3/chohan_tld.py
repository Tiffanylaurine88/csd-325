"""
chohan_tld.py
Modified from: "Cho-Han" by Al Sweigart
Changes by TLD (Tiffany L. Davidson) for CSD-325 Module 3:
- Changed all input prompts to "tld:"
- House fee set to 12% (was 10%)
- Added notice: rolling a total of 2 or 7 awards a 10 mon bonus
- Implemented bonus: if dice total is 2 or 7, announce and add +10 mon to purse
"""
import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

intro = ("Cho-Han (TLD edition)\n\n""In this traditional Japanese dice game, two dice are rolled in a bamboo\n""cup by the dealer sitting on the floor. The player must guess if the\n""dice total to an even (cho) or odd (han) number.\n""Special rule: If your roll totals 2 or 7, you get a 10 mon bonus!\n")
print(intro)

purse = 5000
HOUSE_FEE_PERCENT = 12  # changed from 10

while True:  # Main game loop.
    print("You have", purse, "mon. How much do you bet? (or QUIT)")
    while True:
        pot = input("tld: ")
        if pot.upper() == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        elif not pot.isdecimal():
            print("Please enter a number.")
        elif int(pot) > purse:
            print("You do not have enough to make that bet.")
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("The dealer swirls the cup and you hear the rattle of dice.")
    print("The dealer slams the cup on the floor, still covering the")
    print("dice and asks for your bet.")
    print()
    print("    CHO (even) or HAN (odd)?")

    while True:
        bet = input("tld: ").upper()
        if bet != "CHO" and bet != "HAN":
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    print("The dealer lifts the cup to reveal:")
    print("   ", JAPANESE_NUMBERS[dice1], "-", JAPANESE_NUMBERS[dice2])
    print("     ", dice1, "-", dice2)

    total = dice1 + dice2
    rollIsEven = (total % 2) == 0
    correctBet = "CHO" if rollIsEven else "HAN"
    playerWon = (bet == correctBet)

    if playerWon:
        print("You won! You take", pot, "mon.")
        purse = purse + pot
        house_fee = (pot * HOUSE_FEE_PERCENT) // 100
        print(f"The house collects a {house_fee} mon fee ({HOUSE_FEE_PERCENT}%).")
        purse = purse - house_fee
    else:
        purse = purse - pot
        print("You lost!")

    if total in (2, 7):
        print(f"Bonus! Your total was {total}. You receive +10 mon.")
        purse += 10

    if purse <= 0:
        print("You have run out of money!")
        print("Thanks for playing!")
        sys.exit()