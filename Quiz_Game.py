print("Welcome to my quiz game! ")
playing = input("Do you want to play my game? ")

if playing.lower() != "yes":
    quit()

print("okay let's play")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() in ("cpu", "central processing unit"):
    print('correct!')
    score += 1
else:
    print("incorrect!")
    print("The correct answer is Central processing unit")

answer = input("what does GPU stand for? ")
if answer.lower() in ("gpu", "graphics processing unit"):
    score += 1
    print('correct!')
else:
    print("incorrect!")
    print("The correct answer is Graphics processing unit")

answer = input("What does RAM stand for? ")
if answer.lower() in ("ram", "random access memory"):
    score += 1
    print('correct!')
else:
    print("incorrect!")
    print("The correct answer is Random access memory")

answer = input("what does PSU? ")
if answer.lower() in ("psu", "power supply unit"):
    score += 1
    print('correct!')
else:
    print("incorrect!")

print("you got " + str(score) + " questions correct ")

    
    
    