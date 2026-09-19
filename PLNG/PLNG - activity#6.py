#GRADE PROGRAM
def inputCatch(callerFunc):
        try:
            uNum = int(input())
            if uNum < 0 or uNum > 100:
                raise ValueError
            return uNum
        except ValueError:
            print("ERROR! That was not a valid number!")
            callerFunc()

def gradeCalc():
    print("Input Java score: ")
    Jscore = inputCatch(gradeCalc)
    """
        if Jscore <= 0:
        print("INVALID NUMBER!")
        gradeCalc()
    """

    print("Input C score: ")
    Cscore = inputCatch(gradeCalc)

    print("Input Database Handling score: ")
    DBscore = inputCatch(gradeCalc)

    total = Jscore + Cscore + DBscore
    average = total / 3
    letterGrade = ' '
    explanation = " "

    if average >= 90:
        letterGrade = 'A'
        explanation = "between 90 and 100"
    elif average >= 80:
        letterGrade = 'B'
        explanation = "between 80 and 89"
    elif average >= 75:
        letterGrade = 'C'
        explanation = "between 75 and 79"
    else:
        letterGrade = 'F'
        explanation = "below 75."

    print(f"Java Programming Score: {Jscore}  |  C Programming Score: {Cscore} | Database Handling Score: {DBscore}")
    print(f"Average: {average}  |   Grade: {letterGrade} because the average is {explanation}")

    print("Do you want to continue? (YES/NO):")
    contAns = input()

    if contAns.lower() == "no":
        print("Program terminated. Thank you!")
    elif contAns.lower() == "yes":
        gradeCalc()
    else:
        print("Please enter either YES or NO only.")
        print("Do you want to continue? (YES/NO):")
        contAns = input()

def main():
    gradeCalc()

if __name__ == "__main__":
    main()
