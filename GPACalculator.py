#Ryan Tolentino
#TolentinoDev
#15 January 2017
#GPA Calculator


print('Welcome to the GPA Calculator.')
print('Please enter all your letter grades, one per line.')
print('Enter a blank line to terminate the program.')
points = {'A+':4.0,'A':4.0,'A-':3.67,'B+':3.33,'B':3.0,
          'B-':2.67,'C+':2.33,'C':2.0,'C-':1.67,'D+':1.33,
          'D':1.0,'F':0.0}
number_courses = 0
total_pnts = 0
done = False

while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print("Unknown grade '{0}' being ignored".format(grade))
    else:
        number_courses +=1
        total_pnts += points[grade]
if number_courses > 0:
    print('Your GPA is {0:.3}'.format(total_pnts/number_courses))
