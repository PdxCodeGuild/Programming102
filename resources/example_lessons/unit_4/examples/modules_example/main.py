# MAIN module
import helpers

# define main function to add two numbers using function in helpers module
def main():
    number1 = float(input('Enter the first number: '))
    number2 = float(input('Enter the second number: '))

    print(helpers.add(number1, number2))

main()