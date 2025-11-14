# Hamming


class HammingTest(object):
    def __init__(self, dna_code: str):
        self.dna_code = dna_code

    def __repr__(self) -> str:
        return self.dna_code

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HammingTest):
            raise ValueError("Other must be instance of HammingTest.")
        return self.dna_code == other.dna_code

    def distance(self, other: str) -> int:
        if len(self.dna_code) != len(other):
            raise ValueError("Strands must be of equal length.")
        if not all(i in "ATCG" for i in self.dna_code + other):
            raise ValueError("Strands must contain only A, T, C, and G.")

        count = 0
        for index in range(len(self.dna_code)):
            if self.dna_code[index] != other[index]:
                count += 1
        return count
