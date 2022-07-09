class vector:
    def __init__(self,vec):
        self.ve=vec 
    def __str__(self):
        str1=""
        index=0
        for i in self.ve:
            str1=str1+f"{i}A{index} + "
            index+=1
        return str1[:-2]
    def __add__(self,vec1):
        new=[]
        for i in range(len(self.ve)):
            new.append(self.ve[i]+vec1.ve[i])
        return vector(new)
    def __mul__(self,vec2):
        new=[]
        for i in range(len(self.ve)):
            new.append(self.ve[i]*vec2.ve[i])
        return vector(new)

v1=vector([1,4,6,10])
v2=vector([4,6,3,6])
print(v1+v2)
print(v1*v2)
