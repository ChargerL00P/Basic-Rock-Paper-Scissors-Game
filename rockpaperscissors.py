import random
user_wins, cpu_wins = 0, 0
user, cpu = 0, 0
username = input("What's your name? ")
options = ["rock", "paper", "scissors"]
while True:
    user = input("Choose Rock / Paper / Scissors / q to quit: ").lower()
    cpu = random.choice(options)
    if user == "q":
        break
    if user not in options:
        continue
    if user == "rock" and cpu == "scissors" or \
       user == "paper" and cpu == "rock" or \
       user == "scissors" and cpu == "paper":
        print(f"CPU used {cpu}. You won!")
        user_wins += 1
    elif user == "rock" and cpu == "paper" or \
         user == "paper" and cpu == "scissors" or \
         user == "scissors" and cpu == "rock":
        print(f"CPU used {cpu}. You lost!")
        cpu_wins += 1
    elif user == cpu:
        print(f"CPU used {cpu}. It's a tie!")
print(f"CPU has {cpu_wins} scores. {username} has {user_wins} scores.")
if cpu_wins > user_wins:
    print("CPU won!")
if cpu_wins < user_wins:
    print(f"{username} won!")
else:
    print("It's a tie!")