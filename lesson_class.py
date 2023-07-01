import abc

class Poultry(abc.ABC):
    def __init__(self, color, sound, species) -> None:
        self.color = color
        self.sound = sound
        self.species = species

    def make_some_noise(self):
        print(f"{self.species} is making some noise !! {self.sound * 3}")    

    def move(self):
        print(f"{self.species} move.")

    @abc.abstractmethod
    def eat(self):
        pass

    def hatch(self):
        print(f"{self.species} hatch zzz.")

    def fly(self):
        print(f"papapa")

class Duck(Poultry):
    def __init__(self, color, sound) -> None:
        super().__init__(color, sound, "Duck")

    def eat(self):
        print(f"{self.species} eat vegitable.")
    
    def swim(self):
        print(f"{self.species} swim ~")


class Chicken(Poultry):
    def __init__(self, color, sound) -> None:
        super().__init__(color, sound, "Chicken")

    def eat(self):
        print(f"{self.species} eat bug.")

    def morning_call(self, time):
        print(f"{self.sound * 3}, it's {time} a.m. now")


if __name__ == '__main__':
    duck_1 = Duck('yellow', 'ba')
    duck_2 = Duck('black', 'ga')
    duck_3 = Duck('white', 'gua')

    duck_2.make_some_noise()
    print(duck_2.sound)
    duck_2.eat()

    chicken_1 = Chicken("Brown", 'gu')
    chicken_1.make_some_noise()
    print(chicken_1.sound)
    chicken_1.eat()
    chicken_1.morning_call(6)