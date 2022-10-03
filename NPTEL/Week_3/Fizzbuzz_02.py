def fizzBuzz(rnge):
    for i in range(1,rnge):
        if(i%3==0 and i%5==0):
            print(f"X={str(i)} --> FIZZ-BUZZ")
        else:    
            if (i%3==0):
                print(f"X={str(i)} --> FIZZ")
            else:
                if (i%5==0):
                    print(f"X={str(i)} --> BUZZ")
                else:
                    print(str(i))
i=int(input("Enter The Range for Fizzbuzz: "))
fizzBuzz(i+1)