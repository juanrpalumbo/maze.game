import random
directions = ("N","S","E","W")
answer=("you are in a maze, choose one direction (N, S, E, or W)"+random.choice(directions))
combination=('N','S','N','E','W','N')
moves=1
lives=3

if moves ==(11,21,31):
    lives = lives-1
    print('you have just los one life, you now have'+str(lives)+'lives')

    for i in combination:
        while answer == combination[combination.index(i)]
            print ("start again")
            x=x+1
            if lives == 0:
                print('start again')
                break
            if answer == combination[i]:
                i = i+1
                if i<len(combination):
                    print('good, now where do you want to go?')
                else:
                    print('congrats you have escaped')
                    break

print('!!!!!!!!!')