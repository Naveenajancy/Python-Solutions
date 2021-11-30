class ShippingContainer:
    next_serial = 321

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = self.next_serial + 1

c1 = ShippingContainer("SJE", ["clothes", "snacks"])
print("The owner code is ", c1.owner_code)
print("The contents are ", c1.contents)
print ( "the serail number ", c1.serial )
c2 = ShippingContainer("EJD", ["shoes","leather"])
print("The owner code is ", c2.owner_code)
print("The contents are ", c2.contents)
print ( "the serail number ", c2.serial )