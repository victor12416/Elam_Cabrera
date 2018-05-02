# GPS to hannas house
"""
all the hardwired settings that will take place in the program
is here
"""
def next_step():
    print('     ||||||||||||||||||||NEXT_STEP|||||||||||||||||||||')
def final_destination():
    print('     |||||||||||Arived at Final Destination||||||||||||')
#Location_1 = ('Elam(s) house')
#Location_2 = ('Hanna(s) house')


"""
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
print('What Location are you starting from' + '\n')
print('Before entering location Note that the program only apccets' + '\n' + '2 choices, Location_1 = Elam(s) house and Location_2 = Hanna(s) house' + '\n' + 'The locations have to be written as illistrated.' + '\n')
Location = input('Location:\n')

def give_direction(Location):
    if Location == 'Location_1' or 'location_1':
        print('The Program needs to have the car start from the exit of vehicle parking spot.')
        next_step()
        print('At the exit of the drive way take a left and go forward, stop at the connor.')
        next_step()
        print('Turn left at and go forward until stop.')
        next_step()
        print('Thank you for using our Application now leave, its my lunch break.')
        final_destination()
    elif Location == 'Location_2' or 'location_2':
        print('The Program needs to have the car start from the exit of vehicle parking spot.')
        next_step()
        print('At the exit of the drive way take a right and go forward, stop at the connor.')
        next_step()
        print('Turn right at and go forward until stop.')
        next_step()
        print('GET OUT AND DONT COME BACK, LEAVE YOURS KEYS')
        final_destination()
    else:
        print('Your current location is not recorded ' + '\n' + 'in our current DATABASE')
    return give_direction
    


User_location = give_direction(Location)
print(User_location)


"""
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""



"""
this is all the logic that figures out the
path it needs to run depending on the location

Drive_way = input('Is the vehivcle in a drive way')
Positon = input('What position is the vehicle in, Forward or Backwards' + '\n')


if Drive_way == 'yes' or 'Yes':
    
if Position == 'Backwards' or 'backwards':
    print('The car needs to go into reverse and change positions') 
"""

    








