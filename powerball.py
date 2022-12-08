import random
from utilts import  *

class Winning_number():

    def winning_white_ball(self):                # ##    This function contain today's 5 winning num and 1 power ball
        number = range(1,20)
        win_number = random.sample(number, k=5)
        win_number.sort()
        return win_number


class Lucky_numbers():

##   This function contain a number which is selected by customer or candidate

    def your_lucky_numbers(self):
        number = range(1,20)
        lucky_numbers = random.sample(number, k=5)
        lucky_numbers.sort()
        return lucky_numbers

class Value(Winning_number,Lucky_numbers):
    def Score(self):
        powerball_win = random.randint(1, 10)
        powerball_lucky = random.randint(1, 10)

        todays_number = Winning_number().winning_white_ball()
        lucky_number = Lucky_numbers().your_lucky_numbers()
        countd = len(set(todays_number) & set(lucky_number))

        list_number = [str(x) for x in todays_number]
        win_number = "  ".join(list_number)
        list_number = [str(x) for x in lucky_number]
        lucky_numbers = "  ".join(list_number)

        #   To know how many numbers has a customer from given today's winning number

        print(f"{blue}powerball winning Numbers", end="  ")
        print(green,win_number, yellow,powerball_win,returen)
        print(f"{blue}your lucky ball Number", end="  ")
        print(green,lucky_numbers, yellow, powerball_lucky, returen)
        print()
        print(f"{blue}The number of white balls {yellow}{countd}")
        print("___________________________________________________________")
        if powerball_win != powerball_lucky and countd == 5:
            print(f"{green}5 Correct White Balls and  the  Powerball: $1,000,000")
        elif powerball_win == powerball_lucky and countd == 4:
            print(f"{green}4 Correct White Balls, but no Powerball: $10,000")
        elif powerball_win != powerball_lucky  and countd == 4:
            print(f"{green}4 Correct White Balls, but no Powerball: $100")
        elif powerball_win == powerball_lucky  and countd == 3:
            print(f"{green}3 Correct White Balls and the Powerball: $100")
        elif powerball_win != powerball_lucky and countd == 3:
            print(f"{green}3 Correct White Balls, but no Powerball: $7")
        elif powerball_win == powerball_lucky  and countd == 2:
            print(f"{green}2 Correct White Balls, but no Powerball: $7")
        elif powerball_win!= powerball_lucky  and countd == 2:
            print(f"{red}you are not lucky\nTry agine!")
        elif powerball_win == powerball_lucky  and countd == 1:
            print(f"{green}1 Correct White Balls and the Powerball: $4")
        elif powerball_win!= powerball_lucky  and countd ==1:
            print(f"{red}you are not lucky\nTry agine!")
        elif powerball_win == powerball_lucky and countd == 0:
            print(f"{green} 0 Correct White Balls, but no Powerball: $4")
        else:
            print(f"{red}you are not lucky\nTry agine!")





