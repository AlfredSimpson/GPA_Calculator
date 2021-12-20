'''
This is a simple program to calculate your GPA.
'''
courses = []
grades = []
qPoints = []
courseCredit = {}
GPV = {'A' : 4.0,'B+' : 3.5,'B' : 3.0,'C+' : 2.5,'C' : 2.0,'D' : 1.0,'F' : 0.0}
    


def GPValue():
    print('Some universities follow a different grading format.\n')
    print('This program uses the following grading scale, based upon NJIT\'s calculation of Grade Point Average: ')
    for grade in GPV:
        print(grade +' : '+str(GPV[grade]), end = '\n')
    print('This program does not currently accept alternate grading formulas. ')
    #edit GPV to reflect the ability to .updateGPV with their own eventually
    

def coursesTaken():
    while True:
        try:
            numCourses = int(input('How many courses did you take? '))
            break
        except ValueError:
            print('We need whole numbers only!')
    for i in range(numCourses):
        numClass = i+1
        className = input('What is the name of course #'+str(numClass)+'? ')
        className = className.capitalize()
        if className in courses:
            print('This course is already added!')
        elif className not in courses:
            courses.append(className)

def addCredits():
	for course in courses:
		while True:
			try:
				credits = int(input('How many credits was '+course+' worth? '))
				if course not in courseCredit:
					courseCredit[course] = credits
					break
				elif course in courseCredit:
					print('Course already added, with a grade of: '+str(credits[courseCredit]))
					break
			except ValueError:
				print('Courses are only worth whole credits and must be written as a digit.')
def qualityPoints():
    for course in courseCredit:
        finalGrade = input('What letter grade did you earn for your final grade in '+course+'? ')
        finalGrade = finalGrade.upper()
        while True:
            if finalGrade in GPV:
                qPoints.append(GPV[finalGrade])
                print('Grade added.')
            else:
                print('Grade cannot be added. Please try again, using the following as a format: ')
                for grade in GPV:
