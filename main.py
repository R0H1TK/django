class complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,c):
        return complex(self.real+c.real,self.imaginary+c.imaginary)
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
    def __mul__(self, c):
        multipliedReal= self.real*c.real-self.imaginary*c.imaginary
        multipiedImaginary=self.real*c.imaginary+ self.imaginary*c.real
        return complex(multipliedReal,multipiedImaginary)
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
c1= complex(2,3)
c2=complex(4,5)
print(c1+c2)
print(c1*c2)