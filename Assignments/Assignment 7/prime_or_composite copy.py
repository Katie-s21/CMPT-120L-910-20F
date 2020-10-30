def prime_or_composite(number):
  number = input("Enter number: ")
  if int(number) > 1:
      for x in range(2, int(number)):
          if (int(number) % x) == 0:
            print ("Composite")
      else:
          print("prime")
  else:
      print("Composite")
        
    
if __name__ == "__main__":
    numbers = [1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201]
    # If you want to test the efficency of your algorithm add this number to the array above -7
    # If you want to test the efficency of your algorithm add this number to the array above 47055833459
    answers = []
    for number in numbers:
        answers.append(prime_or_composite(number))
    
    print(answers)