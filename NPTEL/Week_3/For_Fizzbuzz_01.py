for i in range(1,100):
    if (i%3==0):
        print(f"X={str(i)} --> FIZZ")
    else:    
        if (i%5==0):
            print(f"X={str(i)} --> BUZZ")
        else:
            if(i%3==0 and i%5==0):
                print(f"X={str(i)} --> FIZZ-BUZZ")
            else:
                print(str(i))
        
