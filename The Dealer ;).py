Inventory_list = ['Infiniti, Subaru, Lexus, GMC, Toyota, BMW, Honda, Lincoln' ]

#individual list of cars 
Infiniti = ['Q50,QX80,QX30']
Subaru= ['Impreza,Legacy,Forester']
Lexus = ['Rx,IS,Ls']
GMC = ['Acadia,Yukon,Canyon']
Toyota = ['Corolla,Land Crusier,C-HR'] 
BMW = ['3 Series,X5,5 Series']
Honda = ['Accord,Civic,CR-V']
Lincoln = ['Continential,Navigator,MKZ']

#Dialoge
print('Hi welcome to elam autoshop,')
print('if your new i got just the thing for you.')
print('Just pick one of your favorite car brands and well start from there.')
print('Here are some of the top leading Brands')
print('~~>If the Brand is not listed amagon the intial inventory')
print('please enter (N/A)')
print('')
#user Input
print(Inventory_list)
UI = input()
print('')



#adds Brands and 3 cars into it 
if UI == 'N/A':
    print('Please Enter the name of the brand you')
    print('want to add to the selection')
    
    new_brand = input()
    
    print('Now we need to add three cars to add to the suggested Brand')
    
    new_car1 = input("1. ")
    new_car2 = input("2. ")
    new_car3 = input("3. ")
    
    new_brand_car_list = [new_car1, new_car2, new_car3]

    Inventory_list.append(new_brand)
    
    
    print("You added a new " + new_brand + " list to the database " + "with these models " + str(new_brand_car_list))
    print('')
    
    
    NUI = input('Do you want to go ahead and pick the brand you suggested(Y/N)')
    
    if NUI == 'Y':
        print('')
        print('Here are the cars you picked from ' + new_brand)
        print(new_brand_car_list)
        print('')
        
        import random    
        car_price = (random.randint(40,100))
        
        User_car_selection = input('What car are you going to go for:')
        if User_car_selection == new_car1:
            print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
        if User_car_selection == new_car2:
            print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
        if User_car_selection == new_car3:
            print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    
        
        
    else:
        print('')
        print(Inventory_list)
        print('What brand are you going to go for')
        UI = input()

    
    
#Randomiser
import random    
car_price = (random.randint(50,100))      

#scans for UI input and prints accordingly
if UI == 'Infiniti':
    print('Here are the top cars from ' + UI)
    print(Infiniti)
    
    User_car_selection = input('What car are you going to go for:')
    if User_car_selection == 'Q50':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'QX80':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'QX30':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    

if UI == 'Subaru':
    print('Here are the top cars from ' + UI)
    print(Subaru)
    
    User_car_selection = input('What car are you going to go for:')
    if User_car_selection == 'Impreza':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'Legacy':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'Forester':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    

if UI == 'Lexus':
    print('Here are the top cars from ' + UI)
    print(Lexus)
    
    User_car_selection = input('What car are you going to go for:')
    if User_car_selection == 'Rx':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'IS':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'Ls':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')

if UI == 'GMC':
    print('Here are the top cars from ' + UI)
    print(GMC)
    
    User_car_selection = input('What car are you going to go for:')
    if User_car_selection == 'Acadia':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'Yukon':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'Canyon':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')


if UI == 'Toyota':
    print('Here are the top cars from ' + UI)
    print(Toyota)
    
    User_car_selection = input('What car are you going to go for:')
    if User_car_selection == 'Corolla':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'Land Crusier':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'C-HR':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')

if UI == 'BMW':
    print('Here are the top cars from ' + UI)
    print(BMW)
    
    User_car_selection = input('What car are you going to go for:')
    if User_car_selection == '3 Series':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'X5':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == '5 Series':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')

if UI == 'Honda':
    print('Here are the top cars from ' + UI)
    print(Honda)
    
    User_car_selection = input('What car are you going to go for:')
    if User_car_selection == 'Accord':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'Civic':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'CR-V':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')

if UI == 'Lincoln':
    print('Here are the top cars from' + UI)
    print(Lincoln)
    
    User_car_selection = input('What car are you going to go for:')
    if User_car_selection == 'Continential':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'Navigator':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')
    if User_car_selection == 'MKZ':
        print('The cuurent going price for ' + User_car_selection + ' is ' + str(car_price) + ',000')






