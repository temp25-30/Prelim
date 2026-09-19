def main():
    print("Enter number that is the multiple of 5 between 1 and 100")
    try:
        uInput = int(input())
        if uInput > 100:
            print("Value is greater than 100!")
            raise ValueError()
        elif uInput < 1:
            print("Value is less than 1!")
            raise ValueError()

        if uInput%5 == 0:
            print("The number is valid!")
        else:
            print("The number is not valid! Try again!")
            main()
    except ValueError:
        print("Invalid input! Try again!")
        main()

if __name__ == "__main__":
    main()
