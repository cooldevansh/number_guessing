import random

number_random=random.randint(3, 9)
print("number genetaed at", number_random)
user=int(input("enter any number"))
if(user==number_random):
    print("you win")
    
else: 
        print("you lose")
        print("the number genrated was ", number_random)




     