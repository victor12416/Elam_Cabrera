#This program is for Review


#Lists
media_list = ['books,magazines,newspapers,television,movies,video games,music']
Genre_list = ['Movies/,Horror, Romantic comedy,Science fiction,/Music/,HipHop,Jazz,rock,Folk,Classical,Country,Electronic']

#This has all the inputs
print ('There are many types of forms of Media here are some examples')
print (media_list)
print('    ')
Media = input('What type of media do you use: ')

#askses for the title
print('    ')
Title = input('What is the Titles that you enjoy on/in ' + Media + ':')
print('    ')

#askes for the description of your Title
print ('What is ' + Title + ' about?: ')
Description = input()
print('    ')   

#Year that it was created 
print ('*tip-If you dont know the date then, plesase enter (N/A)')
Year = input('What Year was it created: ')
print('    ')   

#This part askes for the Genrea
print ('*tip-if help needed with the genre selection  enter (help)')
Genre = input('What type of genre is ' + Title + ':')
if Genre == 'help':
    print (Genre_list)
    Genre = input('What type of genre is ' + Title + ':')
#/////////////////////////////////////////////////////////////////////////////
print('    ')     

#Rating 
Rating = float(input('How would you rate ' + str(Title) + ' in a scale of 1-10: '))
print (Rating)

#Review lsit/print out
Review_list = [Media,Title,Description,Year,Genre,Rating]
print('    ')     
print ('   //////Review//////   ')

print ('Media Type---' + Review_list[0])
print ('Title---' + Review_list[1])
print ('Description---' + Review_list[2])
print ('Year Created---' + Review_list[3])
print ('Genre---' + Review_list[4])
print ('Rating---' + str(Review_list[5] ))

print ('   //////Review//////   ')







