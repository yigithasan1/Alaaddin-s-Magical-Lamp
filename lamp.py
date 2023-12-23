import random 
counter = 0 
lamp = [False,False,False,False,False,False]
average = []
game_counter = 100000
# print(r)
for item in range(game_counter) :
    while lamp[0] == False or lamp[1] == False or lamp[2] == False or lamp[3] == False or lamp[4] == False or lamp[5] == False :
        r = random.randint(0,5)
        if r == 0 :
            lamp[r] = not lamp[r]
        elif r == 1 : 
            lamp[r] = not lamp[r]
        elif r == 2 : 
            lamp[r] = not lamp[r]
        elif r == 3 :
            lamp[r] = not lamp[r]
        elif r == 4 : 
            lamp[r] = not lamp[r]
        elif r == 5 : 
            lamp[r] = not lamp[r]
        counter = counter + 1
    average.append(counter)
    lamp = [False,False,False,False,False,False]
    counter = 0 
    
result = sum(average)/game_counter
print(result)





    






    
 



