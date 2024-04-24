courses_classes = {'CS101':'CS101', 'CS102':'CS102', 'CS103':'CS103', 'NT110':'NT110', 'CM241':'CM241' }

courses_rooms = {'CS101':3004, 'CS102':4501, 'CS103':6755, 'NT110':1244, 'CM241':1411 }

courses_instructors = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee' }

courses_times = { 'CS101':'8:00am', 'CS102':'9:00am', 'CS103':'10:00am', 'NT110':'11:00am', 'CM241':'1:00pm' }



course = input('Enter a class name:')



if course in courses_rooms:
    print('Class:', courses_classes[course])
    print('Room:', courses_rooms[course])
    print('Instructor:', courses_instructors[course])
    print('Time:', courses_times[course])
else:
    print('Invalid course number.')
