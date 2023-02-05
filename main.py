import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
a=int(input("What do u choose, type 0 for rock 1 for paper,2 for scissors"))
lis=[rock,paper,scissors]
print(lis[a])
r=random.randint(0,2)
print("computer chose:"+ lis[r])
if((a==0 and r==0) or (a==1 and r==1) or (a==2 and r==2)):
  print("it's a draw")
elif((a==0 and r==1) or (a==1 and r==2) or (a==2 and r==0)):
  print("you lose")
else:
  print("you win")



  


