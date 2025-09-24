class Trip(object):
    def __init__(
        self,
        start,
        end,
        distance,
        duration,
        fare,
    ) -> None:
        self.start = start
        self.end = end
        self.distance = distance
        self.duration = duration
        self.fare = fare

    def __repr__(self) -> str:
        return f"Trip({self.start}, {self.end}, {self.distance}, {self.duration}, {self.fare})"

    def __add__(
        self,
        other,
    ) -> "Trip":
        if isinstance(other, Trip):
            return Trip(
                start=self.start,
                end=other.end,
                distance=self.distance + other.distance,
                duration=self.duration + other.duration,
                fare=self.fare + other.fare,
            )

        raise ValueError(f"Operation add not defined for Trip and { type(other) }")


class Transportation:
    def __init__(
        self,
    ) -> None:
        pass


class Bus(Trip, Transportation):

    def __init__(
        self,
        start,
        end,
        distance,
        duration,
        fare,
    ) -> None:
        Trip.__init__(
            self,
            start,
            end,
            distance,
            duration,
            fare,
        )


class Train(Transportation):
    def __init__(
        self,
    ) -> None:
        super().__init__()


class Car(Transportation):
    def __init__(
        self,
    ) -> None:
        super().__init__()


class Airplane(Transportation):

    def __init__(
        self,
        flight_number: str = None,
    ) -> None:
        super().__init__()
        self.flight_number = flight_number

    def needsPassport(self):
        pass

    def __repr__(self) -> str:
        return f"Airplane(flight_number={self.flight_number})"


class Azul(Trip, Airplane):

    def __init__(
        self,
        start,
        end,
        distance,
        duration,
        fare,
        flight_number: str,
    ) -> None:
        Trip.__init__(
            self,
            start,
            end,
            distance,
            duration,
            fare,
        )
        Airplane.__init__(self, flight_number)

    def needsPassport(self):
        return False

    def __repr__(self) -> str:
        return f"Azul(start={self.start}, end={self.end}, distance={self.distance}, duration={self.duration}, fare={self.fare}, flight_number={self.flight_number})"

    def __add__(
        self,
        other,
    ) -> "Trip":
        if isinstance(other, Trip):
            return Trip(
                start=self.start,
                end=other.end,
                distance=self.distance + other.distance,
                duration=self.duration + other.duration,
                fare=self.fare + other.fare,
            )

        raise ValueError(f"Operation add not defined for Azul and { type(other) }")


SantosSaoCarlos = Trip(
    start="Santos",
    end="São Carlos",
    distance=500,
    duration=5,
    fare=30,
)

SaoCarlosBH = Trip(
    start="São Carlos",
    end="Belo Horizonte",
    distance=900,
    duration=10,
    fare=150,
)

print(SantosSaoCarlos)
print(SaoCarlosBH)
print(SantosSaoCarlos + SaoCarlosBH)
# print(SantosSaoCarlos + 1)

SantosSaoPaulo = Bus(
    start="Santos",
    end="São Paulo",
    distance=500,
    duration=5,
    fare=30,
)

SaoPauloRio = Azul(
    start="São Paulo",
    end="Rio de Janeiro",
    distance=1000,
    duration=10,
    fare=100,
    flight_number="AZ123",
)

print(f"SantosSaoPaulo + SaoPauloRio = {SantosSaoPaulo + SaoPauloRio}")
print(SaoPauloRio.needsPassport())
