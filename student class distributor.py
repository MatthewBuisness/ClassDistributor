ClassesTuples=[("mathSix",6),("mathSeven",7),("mathEight",8),("EnglishSix",6),("EnglishSeven",7),("EnglishEight",8)]
StudentTuples=[("greg",8),("lakisha",6),("Laquan",8),("emily",6),("Jamal",8),("James",6),("Peyton",7),("Steven",7),("Grace",7),("Denise",7)]    
StudentTuples8=[]
StudentTuples7=[]  
StudentTuples6=[] 
ClassesSix=[]
ClassesSeven=[]
ClassesEight=[]
SudentOverflow=[] 
def ClassDistribution(StudentList,Classes):
    x=" "
    howmanyStudents=len(StudentList)
    for Student in StudentList:
        if "8" in Student[1]:
            Student.append(StudentTuples8)
        elif "7" in Student[1]:                   
            Student.append(StudentTuples7)
        elif "6" in Student[1]: 
            Student.append(StudentTuples6)
        else:
            x="student did no enter grade properly" 
    for SingleClass in Classes:
        if "6" in SingleClass[1]:
            SingleClass.append(ClassesSix)
        elif "7" in SingleClass[1]:
            SingleClass.append(ClassesSeven)
        elif "8" in SingleClass[1]:
            SingleClass.append(ClassesEight)
    def ClassSize(Classes,Students):
        if len(Classes)%len(Students)==0:
            classSize=Classes//Students 
            return classSize 
        else:
            Remainder=len(Classes)%len(Students)
            count=len(Classes)-Remainder
            while count!=0:
                TransfersTemp=[]
                TransfersTemp.append(Students[1])
                Students.pop(1)
        classSize=Classes//Students
        classSizeFinal=(classSize,Remainder)
        return classSizeFinal
            
                