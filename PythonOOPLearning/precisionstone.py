"""Write an object oriented program to create a precious stone. Not more than 5 precious stones can be held in
possession at a given point of time. If there are more than 5 precious stones, delete the first stone and store the
new one. """


class PrecisionStone(object):
    stones = []

    def __init__(self, name):
        self.insert_stone(name)


    def __repr__(self):
        return repr(self.stones)

    def yield_first(iterable):
        for item in iterable or []:
            yield item.name
            return


    def has_more_than_five_stones(self):
        if len(self.stones) >= 5:
            return True
        else:
            return False


    def insert_stone(self, name):
        if self.has_more_than_five_stones():
            self.stones.remove(self.stones[0])
            #print(self.yield_first())
            #del self.stones[0]
        self.stones.append(name)

    def __str__(self):
        # return " ".join([str(element) for element in self.stones])
        return " ".join(map(str, self.stones))


preciousStoneOne = PrecisionStone("Ruby")
preciousStoneTwo = PrecisionStone("Emerald")
preciousStoneThree = PrecisionStone("Sapphire")
preciousStoneFour = PrecisionStone("Diamond")
preciousStoneFive = PrecisionStone("Amber")
print(preciousStoneFive)

preciousStoneSix = PrecisionStone("Onyx")
print(preciousStoneSix)