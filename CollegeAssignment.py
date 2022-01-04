import cx_Oracle,sys
class College:
    def clgdet(self):
        self.clgname="INDIRA GANDHI NATIONAL TRIBAL UNIVERSITY,AMARKANTAK MADHYA PRADESH"
class InternalMarks:
    def internal(self):
        try:
            while(True):
                self.ic=int(input("Enter the Internal marks of C :"))
                if(self.ic<0 or self.ic>20):
                    print("="*50)
                    print("You entered wrong Marks.Please try again:")
                    print("="*50)
                else:
                    break
            while(True):
                self.icpp=int(input("Enter the Internal marks of C++ :"))
                if(self.icpp<0 or self.icpp>20):
                    print("="*50)
                    print("You entered wrong Marks.Please try again:")
                    print("="*50)
                else:
                    break
            while(True):
                self.ipython=int(input("Enter the Internal marks of Python :"))
                if(self.ipython<0 or self.ipython>20):
                    print("="*50)
                    print("You entered wrong Marks.Please try again:")
                    print("="*50)
                else:
                    break
            if(self.ic<14 or self.icpp<14 or self.ipython<14):
                self.iGrade="Fail"
                self.Itotm=self.ic+self.icpp+self.ipython
            else:
                self.iGrade="Pass"
                self.Itotm=self.ic+self.icpp+self.ipython
        except ValueError:
            print("="*60)
            print("Don't enter String/Spacial symbol/Alphanumeric for Internal Marks")
            print("="*60)
            sys.exit()

class ExternalMarks(InternalMarks):
    def external(self):
        try:
            while(True):
                self.ec=int(input("Enter the External marks of C :"))
                if(self.ec<0 or self.ec>80):
                    print("="*50)
                    print("You entered wrong Marks.Please try again:")
                    print("="*50)
                else:
                    self.c=self.ic+self.ec
                    break
            while(True):
                self.ecpp=int(input("Enter the External marks of C++ :"))
                if(self.ecpp<0 or self.ecpp>80):
                    print("="*50)
                    print("You entered wrong Marks.Please try again:")
                    print("="*50)
                else:
                    self.cpp=self.icpp+self.ecpp
                    break
            while(True):
                self.epython=int(input("Enter the External marks of Python :"))
                if(self.epython<0 or self.epython>80):
                    print("="*50)
                    print("You entered wrong Marks.Please try again:")
                    print("="*50)
                else:
                    self.python=self.ipython+self.epython
                    break
                
            if(self.c<40 or self.cpp<40 or self.python<40):
                self.eGrade="Fail"
                self.Etotm=self.ec+self.ecpp+self.epython
                self.totm=self.Itotm+self.Etotm
            else:
                self.Etotm=self.ec+self.ecpp+self.epython
                self.totm=self.Itotm+self.Etotm
                if(self.totm>=250 and self.totm<=300):
                    self.eGrade="Distinct"
                elif(self.totm>=200 and self.totm<=249):
                    self.eGrade="First"
                elif(self.totm>=150 and self.totm<=199):
                    self.eGrade="Second"
                elif(self.totm>=120 and self.totm<=145):
                    self.eGrade="Third"
        except ValueError:
            print("="*60)
            print("Don't enter String/Spacial symbol/Alphanumeric for Theory Marks")
            print("="*60)
            sys.exit()

class Student(College,ExternalMarks):
    def sinfo(self):
        try:
            self.sno=int(input("Enter Student Enrollment:"))
            self.sname=input("Enter the student Name:")
            self.dob=input("Enter student DOB:")
            self.fname=input("Enter the  Stusent Father's Name:")
            self.gen=input("Enter student Gender:")
            if(self.Itotm<42):
                self.eGrade="Fail"
        except ValueError:
            print("="*60)
            print("Don't enter String/Spacial symbol/Alphanumeric for Enrollment")
            print("="*60)
            sys.exit()
            
    def display(self):
        print("*"*80)
        print("\t",self.clgname)
        print("="*80)
        print("\t\t  FIRST SEMESTER MARKS - 2021")
        print("-"*80)
        print("\t\t\tPERSONAL INFORMATION")
        print("-"*80)
        print("\t   Enrollment\t:\t",self.sno)
        print("\t   Name\t\t:\t",self.sname)
        print("\t   DOB\t\t:\t",self.dob)
        print("\t   Father's Name :\t",self.fname)
        print("\t   Gender\t:\t",self.gen)
        print("-"*80)
        print("\t\t\tREPORT CARD")
        print("-"*80)
        print("  Subject\tTotal\tInternal(20)\tTheory(80)\tObtain")
        print()
        print("  C Prog\t100\t  ",self.ic,"\t\t",self.ec,"\t\t",self.c)
        print()
        print("  CPP\t\t100\t  ", self.icpp,"\t\t",self.ecpp,"\t\t",self.cpp)
        print()
        print("  PYTHON \t100\t  ",self.ipython,"\t\t",self.epython,"\t\t",self.python)
        print("-"*80)
        print("  TOTAL\t\t300\t  ",self.Itotm,"\t\t",self.Etotm,"\t \t",self.totm)
        print("="*80)
        print("  \t\t\t\t\t",self.iGrade,"\t\t",self.eGrade)
        print("*"*80)
    def insert(self):
        try:
            con=cx_Oracle.connect("Surya","AshoK1775")
            cur=con.cursor()
            iq="insert into University values('%s',%d,'%s','%s','%s','%s',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,'%s','%s')"
            cur.execute(iq %(self.clgname,self.sno,self.sname,self.dob,self.fname,self.gen,self.ic,self.icpp,self.ipython,self.ec,self.ecpp,self.epython,self.c,self.cpp,self.python,self.totm,self.iGrade,self.eGrade))
            con.commit()
            print("Data inserted Successfully---Verify")
        except cx_Oracle.DatabaseError as db:
            print("Problem in database:",db)



#main prigram
std=Student()
std.clgdet()
std.internal()
std.external()
std.sinfo()
std.display()
std.insert()

