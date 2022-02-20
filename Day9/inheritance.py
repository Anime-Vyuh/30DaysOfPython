class Kurama:
    def powers(self):
        return "Nine Tails Chakra"

class Naruto(Kurama):
    def battle(self):
        return "Sage Mode"
    def superpowers(self):
        return "I will just Talk"

war = Naruto()
print(war.battle())
print(war.powers())
print(war.superpowers())

"""
class SliceOfLife:
    def inside(self):
        return "Inside Slice of Anime"

class Romance(SliceOfLife):
    def inside(self):
        return "Inside Romance"

class Comedy(Romance):
    def inside(self):
        return "Inside Comedy"

genre = Comedy()
print(genre.inside())
genre1 = Romance()
print(genre1.inside())
genre2 = SliceOfLife()
print(genre2.inside())

"""