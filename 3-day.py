# Treasure Island Game
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
cross_road = input("You're at a cross road.Where do you want to go? Type 'left' or 'right'").lower()

if cross_road == 'left':
    cross_left = input("Do you want to swim or wait for a boat?").lower()
    if cross_left == 'swim':
        print(" You lost the mission.Game Over")
    elif cross_left == 'wait':
        cross_wait = input("Choose the entry door color there is red, yellow and blue ")
        if (cross_wait == 'red') and (cross_wait == 'blue'):
            print("Sorry you lost the mission halfway. Game Over")
        elif cross_wait == 'yellow':
            print("Congratulation you won the Game")      
else:  
    print("You've lost the mission.Game over") 