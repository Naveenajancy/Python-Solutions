class Animal:
    @classmethod
    def description(cls):
        return "An animal"

class Bird(Animal):
    @classmethod
    def description(cls):
        s = super()
        print("hello", s)
        print("elcom")
        return super().description() + "with wings"
class Flamingo(Bird):
    @classmethod
    def description(cls):
        s= super()
        print(s)

        return super().description() + "With fabulous Pink."
