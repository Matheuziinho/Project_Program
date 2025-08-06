# Given an age in seconds, calculate how old someone would be on a planet in our Solar System.

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds / 31_557_600

    def on_earth(self):
        return round(self.seconds, 2)

    def on_mercury(self):
        return round(self.seconds / 0.2408467, 2)

    def on_venus(self):
        return round(self.seconds / 0.61519726, 2)

    def on_mars(self):
        return round(self.seconds / 1.8808158, 2)

    def on_jupiter(self):
        return round(self.seconds / 11.862615, 2)

    def on_saturn(self):
        return round(self.seconds / 29.447498, 2)

    def on_uranus(self):
        return round(self.seconds / 84.016846, 2)

    def on_neptune(self):
        return round(self.seconds / 164.79132, 2)

# Um bilhão de segundos:
print('Earth:', SpaceAge(1_000_000_000).on_earth(), 'years')
print('Mercury:', SpaceAge(1_000_000_000).on_mercury(), 'years')
print('Venus:', SpaceAge(1_000_000_000).on_venus(), 'years')
print('Mars:', SpaceAge(1_000_000_000).on_mars(), 'years')
print('Jupiter:', SpaceAge(1_000_000_000).on_jupiter(), 'years')
print('Saturn:', SpaceAge(1_000_000_000).on_saturn(), 'years')
print('Uranus:', SpaceAge(1_000_000_000).on_uranus(), 'years')
print('Neptune:', SpaceAge(1_000_000_000).on_neptune(), 'years')
