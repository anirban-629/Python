while(True):
    print("q to quit or Enter a number: ")
    a=input("Enter: ")
    if a=="q":
        break
    try:
        a=int(a)
        if a>0:
            print("Greater than 0")
        else:
            print("Less than 0")
    except Exception as e:
        print(f"Invalid..Error!! : {e}")

print("Thankyou..!!")

