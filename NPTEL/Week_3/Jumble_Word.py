import random

def chose():
    words=["rainbow","sea","jungle","eating","name","random","funny","interesting","joking"]
    pick=random.choice(words)
    return pick

def jumble(word):
    jumble_word="".join(random.sample(word,len(word)))
    return jumble_word

def thank(p1n,p2n,p1s,p2s):
    print(p1n,"Have a nice day!..Your score is:",p1s)
    print(p2n,"Have a nice day!..Your score is:",p2s)

def play():
    p1name=input("Player 1 Name:")
    p2name=input("Player 2 Name:")
    pp1=0
    pp2=0
    turn=0
    while(1):
         #Computer's Task
        picked_Word=chose()
        #Create Question
        qn=jumble(picked_Word)
        print(qn)
        if turn%2==0:
            print(p1name,"Your Turn")
            ans=input("What is on my mind")
            if ans==picked_Word:
                pp1=pp1+1
                print("Your Score is: ",pp1)
            else:
                print("Better Luck next time!!, I thought:",picked_Word)
            c=input("Press 1 to continue or 0 to Quit")
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        else:
            print(p2name,"Your Turn")
            ans=input("What is on my mind")
            if ans==picked_Word:
                pp2=pp2+1
                print("Your Score is: ",pp2)
            else:
                print("Better Luck next time!!, I thought:",picked_Word)
            c=input("Press 1 to continue or 0 to Quit")
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn=turn+1
play()