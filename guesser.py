import random


def computer(i, lst):
    answer = random.choice(lst)
    print(lst)
    choose = input(f"I choose number: {answer}, if it's your number press 'W', \nif it's too small press 'A', too big- press 'D' :")
    i += 1
    if choose.upper() == "W":
        print(f"guessed your number in {i} rounds!\n")
    elif choose.upper() == "A":
        computer(i, lst[lst.index(answer)+1:len(lst)])
    else: computer(i, lst[0:lst.index(answer)])

def main():
    while True:
        cyst = [i for i in range(0,int(input("enter the range which the computer must guess the number 0:"))+1)]
        computer(0, cyst)
        if input("do you want to play again, Yes or No?").upper() == "N": break


if __name__ == "__main__":
    main()