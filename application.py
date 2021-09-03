
from classes import Department, Person, Student, Faculty, University, \
    Catalog, Course
from DataSetUp import DataSetUp
import os

GMU, F2020 = DataSetUp( )
depts = GMU.listDepts()       # store the list of Departments for appl use

# Application code follows ----------------------------------------------

Menu = """

        1. Create Course
        2. Add Students to Course
        3. Print Students in Course
        4. Print Courses in Catalog
        Q. Quit

"""
              
while True:
    os.system('cls')
    print (Menu)
    menu_pic = input('Select one of the above and hit "Enter": ')     
    if menu_pic == '1':
        d_code = input('\nEnter "ENGR", "CHHS", or "ARTS": ')
        number = input ('Enter course number, 000 to 999: ')
        title = input ('Enter course title: ')
        print('\nSelect one of the following instructors: \n')
        if d_code == 'ENGR':
            depts[0].listFaculty()
        elif d_code == 'ARTS':
            depts[1].listFaculty()
        else:
            depts[2].listFaculty()
        instructor = input('\nInstructor name (from above): ')
        x = Course(d_code, number, title, instructor)        
        if x not in F2020:
            F2020.addCourse(x)
            input('\n' + d_code + number + ' added to ' + F2020.getName( ) +
                  '"Enter" to continue') 
        else:
            print('Course already in catalog ', F2020.getName( ))
    if menu_pic == '2':
        F2020.printCatalog()
        course = input('\nEnter course as name+number, e.g. "ENGR-101": ')
        course_list = F2020.listCourses()
        found = False
        for c in course_list:
            if course == c.getNameNumber():
                found = True
                stud_list = GMU.listStudents()
                n = 0
                for s in stud_list:
                    print(n+1, ' ', s.g_num, ' ', s.name)
                    n += 1
                pic = int(input('Select one of the above: '))
                if 1 <= pic <= len(stud_list):
                    c.addStudent(stud_list[pic - 1])
                    print(stud_list[pic - 1].name, ' added to course ', course)
                else:
                    print('Invalid student selected')
                break
        if not found:        
            print(course, ' not found in catalog for Fall 2020') 
    if menu_pic == '3':
        F2020.printCatalog( )
        course = input('\nEnter course as name+number, e.g. "ENGR-101": ')
        course_list = F2020.listCourses()
        for c in course_list:
            if course == c.getNameNumber():
                c.printStudents()
                break
            print(course, ' not found in catalog for Fall 2020')
        input('\nHit "Enter" to continue ')
    if menu_pic == '4':
        F2020.printCatalog()
        input ('\nHit "Enter" to continue ')
    if menu_pic in 'Qq': break                     
                     

    
