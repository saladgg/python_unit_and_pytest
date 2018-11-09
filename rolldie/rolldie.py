from random import randint

def run():
    while True:
        num = integer_input("Enter an number to roll: ")
 
        if terminate(num):
            return print("Game terminated")
 
        roll = randint(1,6)
        print(format_result(roll))
 
def integer_input(message):
    while True:
        try:
            x = int(input(message))
            return x
        except ValueError:
            print("\nInvalid value, please enter an integer.")
 
def terminate(num):
    return num == 0
 
def format_result(num):
    return f"Result {num}"

#run()
