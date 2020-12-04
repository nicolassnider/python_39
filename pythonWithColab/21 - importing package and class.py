import math as m

print(m.factorial(5))
print(m.sqrt(4))


class myClass(object):
    """
    docstring
    """
    def add(self,a,b):
        """
        docstring
        """
        return a+b
        pass
    pass

objMyClass = myClass()

print(objMyClass.add(2,5))
