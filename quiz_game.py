print("Welcome to chintapak-dumdum Quiz!")
playing = input("Do you Want to play? ")

if playing != "yes":
    quit()
else:
  print("Okay, let's play :)")
  score = 0

answer = input("chintapak-dumdum dialouge is from which series? ")
if answer == "Chota Bheem":
    print('7 Crore!!!')
    score += 1
else:
   print("nikal yahan se!!")    

answer = input("Chota Bheem had a crush on? ")
if answer == "Tun Tun Mausi":
    print('7 Crore!!!')
    score += 1
else:
   print("nikal yahan se!!")  

answer = input("how many hairs did Raju have? ")
if answer == "two":
    print('7 Crore!!!')
    score += 1
else:
   print("nikal yahan se!!")  

answer = input("what was Shin-Chan fav snack to eat? ")
if answer == "Chocochip":
    print('7 Crore!!!')
    score += 1
else:
   print("nikal yahan se!!")   

print("you got "+ str(score) +" questions correct!!")
print("you got" + str((score/4)*100) + "%.")           