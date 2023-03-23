class Guitar():
    GUITAR_TYPES = ("Stratocaster", "Telecaster", "Les Paul", "SG", "V")

    @classmethod
    def getShape(cls):
        return cls.GUITAR_TYPES

    def __init__(self, shape, colour, price):
        if (not shape in Guitar.GUITAR_TYPES):
            raise ValueError("Guitar shape not real")
        else:
            self.shape = shape
        self.colour = colour
        self.price = price

    def shapeGetter(self):
        return self.shape

    def discount(self, discount):
        return (self.price * discount)


myGuitar1 = Guitar("Les Paul", "Goldburst", 2000)

print(myGuitar1.shapeGetter())
print(myGuitar1.discount(0.7))
print("Shapes: ", Guitar.getShape())
