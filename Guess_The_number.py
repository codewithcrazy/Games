import random
randNum = random.randint(1,10)
count=0
userName=input("Enter Your Name :  ").capitalize()
while True:
    userGuess = int(input("Enter Your Guess : "))
    count+=1
    if(userGuess == randNum):
        break
    elif(userGuess > randNum):
        print("Oops ! Wrong Answer . Guess a low value")
    elif(userGuess < randNum):
        print("Oops ! Wrong Answer . Guess a high value")
print(f"Congratulation {userName} ! You have Used {count} guess to guess the number {randNum}")

with open("guess-the-num-score.txt",'r') as f:
    scoresData=f.read()
with open("guess-the-num-score.txt",'a') as f:
    f.write(f"{userName} has scored {count}\n")
