class A:
    def meth1(self):
        print("Hello from A class")

class B(A):
    def meth2(self):
        print("Hello from B class")

class C(A):
    def meth3(self):
        print("Hello from C class")

class D(B, C):
    def meth4(self):
        print("Hello from D class")

pet = D()
pet.meth1()
pet.meth2()
pet.meth3()
pet.meth4()
