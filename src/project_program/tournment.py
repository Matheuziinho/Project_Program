# Tournament


class Tournament:
    RESULT = {
        "win": 3,
        "loss": 0,
        "draw": 1,
    }

    TEAMS = {
        "Devastating Donkeys",
        "Allegoric Alaskans",
        "Blithering Badgers",
        "Courageous Californians",
    }

    def __init__(self, team1: str, team2: str, result: str):
        self.team1 = team1
        self.team2 = team2
        self.result = result

    def __repr__(self) -> str:
        return f"Tournament({self.team1} vs {self.team2}: {self.result})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tournament):
            return False
        return (
            self.team1 == other.team1
            and self.team2 == other.team2
            and self.result == other.result
        )

    def validate(self) -> None:
        if self.team1 not in self.TEAMS:
            raise ValueError(f"Team '{self.team1}' not recognized.")
        if self.team2 not in self.TEAMS:
            raise ValueError(f"Team '{self.team2}' not recognized.")
        if self.result not in self.RESULT:
            raise ValueError(f"Result '{self.result}' not recognized.")

    def points(self, team: str) -> int:
        if self.result == "draw":
            return 1
        if (self.result == "win" and team == self.team1) or (
            self.result == "loss" and team == self.team2
        ):
            return 3
        return 0
