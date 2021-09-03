
def DataSetUp( ):
    from classes import Department, Person, Student, Faculty, University, \
         Catalog, Course
    print('\nStart of IT209 A8 Data Set-up **************')
    print('\n1. Create 10 student objects for use in the demo ')
    s1 = Student('G34568', 'David Miller', '321 Maple Lane, Vienna, VA',
          '571-285-4567', 'dmiller8@gmu.edu',
          status = 'sophomore', major = 'Hist', enrolled = 'y',
          credits = 30, qpoints = 90)           
    s2 = Student('G21345', 'Sonia Fillmore', '123 Oak Street, Potomac, MD',
          '301-285-4567', 'sfillmor8@gmu.edu',status = 'senior', major = 'Math',
          enrolled = 'y', credits = 90, qpoints = 315)
    s3 = Student('G42156', 'Chris Squire', '4567 Park Lane, London, UK',
          '425-285-4567', 'csquire8@gmu.edu',status = 'sophomore', major = 'Musc',
          enrolled = 'y', credits = 45, qpoints = 160)
    s4 = Student('G10928', 'Tal Wilkenfeld', '423 Outback Way, Sydney, AU',
          '524-485-5674', 'twilkenfeld@AU.gov',status = 'junior', major = 'Musc',
          enrolled = 'y', credits = 75, qpoints = 250)    
    s5 = Student('G22157', 'Larry Graham', '324 San Fernando Bd, Los Angeles, CA',
          '321-987-7674', 'lgraham@funktown.org',status = 'senior', major = 'Musc',
          enrolled = 'y', credits = 105, qpoints = 290)
    s6 = Student('G31345', 'John Entwistle', '6 Stable Way, London, U.K',
          '011-21-9872-7674', 'jentw@thewho.org',status = 'freshman', major = 'CSci',
          enrolled = 'y', credits = 15, qpoints = 35)  
    s7 = Student('G44568', 'Esperanza Spalding', '3512 P Street, NE, Washington, D.C.',
          '345-872-8674', 'esperanza@gmail.com',status = 'junior', major = 'ENGR',
          enrolled = 'y', credits = 65, qpoints = 250)  
    s8 = Student('G55345', 'Tim Bogert', '272 West Street, Los Angeles, CA',
          '543-278-9785', 'timbogert@gmu.edu',status = 'sophomore', major = 'Hist',
          enrolled = 'y', credits = 45, qpoints = 120)           
    s9 = Student('G66113', 'Gordon Sumner', '42 Park Lane, London, U.K.',
          '011-4352-5987', 'sting@gordomusic.com',status = 'freshman', major = 'Musc',
          enrolled = 'y', credits = 15, qpoints = 48) 
    s10 = Student('G11311', 'Paul McCartney', '312 5th Avenua, New York, N.Y.',
          '212-332-1895', 'pmccart@gmu.edu',status = 'senior', major = 'ARTS',
          enrolled = 'y', credits = 110, qpoints = 320)        
    ##s11 = Student('G22111', 'Elizabeth Smythe', status = 'junior', major = 'ENGR',
    ##      enrolled = 'y', credits = 85, qpoints = 250)
    ##s12 = Student('G31312', 'John McVie', status = 'sophomore', major = 'Hist',
    ##      enrolled = 'y', credits = 45, qpoints = 120)
    ##s13 = Student('G31312', 'Nawt Enrolled', status = 'sophomore', major = 'Hist',
    ##      enrolled = 'n', credits = 45, qpoints = 120)
    ##s14 = Student('G11112', 'Toolow G. Peyay', status = 'freshman', major = 'Undc',
    ##      enrolled = 'y', credits = 20, qpoints = 38)           
    f1 = Faculty('G98765', 'Gene Shuman', '3062 Covington Street, Fairfax, VA',
                 '571-235-2345', 'gshuman@gmu.edu', 'Assistant Professor', 'y',
                 18, 'teaching', 250000)     
    f2 = Faculty('G56789', 'Irina Hashmi', '9166 Barrick Street, Fairfax, VA',
                 '571-532-5432', 'ihashmi@gmu.edu', 'Assistant Professor', 'y',
                 18, 'teaching', 325000)     
    f3 = Faculty('G23456', 'Cody Narber', '9211 Amerleigh Way, Ashburn, VA',
                 '703-233-0681', 'cnarber@gmail.com', 'Adjunct Instructor', 'y',
                 12, 'teaching', 0)
    f4 = Faculty('G33456', 'Brady Narber', '921 Donahughe Way, Ashburn, VA',
                 '703-220-0681', 'bnarber@gmail.com', 'Instructor', 'y',
                 12, 'teaching', 0)
    f5 = Faculty('G43456', 'Jennie Biggins', '92 Downer Way, Leesburg, VA',
                 '703-092-06732', 'jbiggins@gmail.com', 'Professor', 'y',
                 12, 'teaching', 0)
    print('List of Students created-------------------------------: ')
    print('s1=  ',s1)
    print('s2=  ',s2)
    print('s3=  ',s3)
    print('s4=  ',s4)      
    print('s5=  ',s5)
    print('s6=  ',s6)      
    print('s7=  ',s7)
    print('s8=  ',s8)
    print('s9=  ', s9)
    print('s10= ',s10)
    ##print('s11= ',s11)
    ##print('s12= ',s12)      
    ##print('s13= ',s13)
    ##print('s14= ',s14)
    print('f1= ', f1)
    d1 = Department('ENGR', 'Engineering', 5, 2.75)
    d2 = Department('ARTS', 'Art and Architecture', 15, 2.0)
    d3 = Department('CHHS', 'College of Health and Human Sevrices', 10, 2.5)

    #input('\n2. Hit "Enter" to see the list of departments created ')
    print('\n\nDepartments established-------------------------:')
    print(d1)
    print(d2)
    print(d3)

    #input('\n\n\n\n3. Hit "Enter" to add s1 - s5 to ENGR Department- print Roster follows\n')
    d1.addStudent(s1)      
    d1.addStudent(s2)
    d1.addStudent(s3)
    d1.addStudent(s4)
    d1.addStudent(s5)
    d1.addStudent(s6)
    d1.addStudent(s7)
    d1.addStudent(s8)
    d2.addStudent(s9)
    d3.addStudent(s10)
    d1.addFaculty(f1)
    d1.addFaculty(f2)
    d1.addFaculty(f3)
    d2.addFaculty(f4)
    d3.addFaculty(f5)
    d1.printRoster('s')
    d1.printRoster('f')
    d2.printRoster('s')
    d3.printRoster()

    d1.printRoster()
    d2.printRoster()
    d3.printRoster()      

    GMU = University( )
    GMU.addDept(d1)
    GMU.addDept(d2)
    GMU.addDept(d3)
    GMU.addStudent(s1)
    GMU.addStudent(s2)
    GMU.addStudent(s3)
    GMU.addStudent(s4)
    GMU.addStudent(s5)
    GMU.addStudent(s6)
    GMU.addStudent(s7)
    GMU.addStudent(s8)
    GMU.addStudent(s9)
    GMU.addStudent(s10)       
    F2020 = Catalog('Fall 2020')
    GMU.addCat(F2020)
    return GMU, F2020  # Return University container and Catalog objects                


    
