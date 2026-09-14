# Task - 1

class Film:
    def __init__(self,ad,il,reyting):
        self.ad = ad
        self.il = il
        self._reyting = None
        self.reyting = reyting

    @property
    def reyting(self):
        return self._reyting

    @reyting.setter
    def reyting(self,value):
        if not 0 <= value <= 10:
            raise ValueError("Reyting 0-10 aralığında olmalıdır")
        self._reyting = value

    def __str__(self):
        return f"{self.ad} ({self.il}) : {self._reyting}"

    @classmethod # Task - 2
    def from_string(cls,text):
        ad,il,reyting = text.split('|')
        return cls(ad, int(il), float(reyting))

    def __eq__(self, other): # Bonus
        if not isinstance(other, Film):
            return False
        return self.ad == other.ad and self.il == other.il

    def __hash__(self): # Bonus
        return hash((self.ad, self.il))

f1 = Film("Inception", 2010, 8.8)
f2 = Film("Inception", 2010, 9.0)
f3 = Film("Interstellar", 2014, 8.6)
 
print(f1 == f2)
 
filmler_set = {f1, f2, f3}
print(len(filmler_set))

#---------------------------------------------------------------

# Task - 3

class FilmSiyahisi:
    def __init__(self):
        self.filmler = []

    def elave_et(self,film):
        return self.filmler.append(film)

    def __len__(self):
        return len(self.filmler)

    def en_yaxsi(self):
        if not self.filmler:
            return None
        return max(self.filmler, key=lambda f: f.reyting)

s = FilmSiyahisi()

s.elave_et(Film.from_string("Inception|2010|8.8"))
s.elave_et(Film.from_string("Interstellar|2014|8.6"))

print(len(s))
print(s.en_yaxsi())

#---------------------------------------------------------------