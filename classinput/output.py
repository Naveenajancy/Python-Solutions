class InputOutputString:
    def getstring(self):
        self.s  = input("Please enter your input\n")

    def toUpper(self):
        print(self.s.upper())

str_obj = InputOutputString()
str_obj.getstring()
str_obj.toUpper()