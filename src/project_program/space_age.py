# Given an age in seconds, calculate how old someone would be on a planet in our Solar System.

from typing import Any, overload


class SpaceAge:
    PLANETS = {
        "earth": 1.0,
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds: int):
        self.__seconds__ = seconds
        self.__init_planets__()

    def __init_planets__(self) -> None:
        for planet, orbital_period in self.PLANETS.items():
            setattr(
                self,
                f"on_{planet.lower()}",
                lambda orbital_period=orbital_period: round(
                    self.__seconds__ / 31_557_600 / orbital_period, 2
                ),
            )


"""
# that was my old code

class SpaceAge:

    def __init__(self, seconds: int):
        self.__seconds__ = seconds

    def on_earth(self):
        return round(self.__seconds__ / 31_557_600, 2)

    def on_mercury(self):
        return round(self.__seconds__ / 0.2408467, 2)

    def on_venus(self):
        return round(self.__seconds__ / 0.61519726, 2)

    def on_mars(self):
        return round(self.__seconds__ / 1.8808158, 2)

    def on_jupiter(self):
        return round(self.__seconds__ / 11.862615, 2)

    def on_saturn(self):
        return round(self.__seconds__ / 29.447498, 2)

    def on_uranus(self):
        return round(self.__seconds__ / 84.016846, 2)

    def on_neptune(self):
        return round(self.__seconds__ / 164.79132, 2)


# Um bilhão de segundos:
print("Earth:", SpaceAge(1_000_000_000).on_earth(), "years")
print("Mercury:", SpaceAge(1_000_000_000).on_mercury(), "years")
print("Venus:", SpaceAge(1_000_000_000).on_venus(), "years")
print("Mars:", SpaceAge(1_000_000_000).on_mars(), "years")
print("Jupiter:", SpaceAge(1_000_000_000).on_jupiter(), "years")
print("Saturn:", SpaceAge(1_000_000_000).on_saturn(), "years")
print("Uranus:", SpaceAge(1_000_000_000).on_uranus(), "years")
print("Neptune:", SpaceAge(1_000_000_000).on_neptune(), "years")
"""
