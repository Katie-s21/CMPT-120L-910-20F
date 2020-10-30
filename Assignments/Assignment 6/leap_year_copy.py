def leap_year(year):
    year = input("Enter year: ")
    if int(year) % 4 == 0:
        print("Is a leap year")
    if int(year) % 4 != 0:
        print("Not a leap year")
    

if __name__ == "__main__":
    years = [2000, 1994, 1912, 3002, 1700, 1400]
    answers = []
    for year in years:
        answers.append(leap_year(year))
    
    print(answers)