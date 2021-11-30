class Base:
    message = "I am in base class"

    @classmethod
    def multiply(cls, num1, num2):
        print("Multiplication is: ",(num1 * num2))
        print("class method Message", cls.message)

    @staticmethod
    def add(num1, num2):
        total = num1 + num2
        print("The sum of two numbers", total)
        print("The static method Message",Base.message)

class Derived(Base):
    message = "hello I am derived"
    def dislay(self):
        print("message", self.message)


c1 = Base()
c1.add(5,3)
c1.multiply(5, 5)
c2 = Derived()
c2.dislay()
c2.add(1, 10)
c2.multiply(2, 7)
