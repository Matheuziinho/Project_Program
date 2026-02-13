# Two Buckets

class TwoBucket:

    def__init__(sel, size1:float, size2:float, desired:float, bucket:int) -> None
        self.size1 = size1
        self.size2 = size2
        self.desired = desired
        self.bucket = bucket

    def repr(self):
        if self.bucket == 1:
            self.bucket = "one"
        elif self.bucket == 2:
            self.bucket = "two"
        else:
            raise ValueError("Invalid bucket number")
        return f"TwoBucket({self.size1}, {self.size2}, {self.desired}, {self.bucket})."

    def measure(self) -> float:
        if self.size1 == self.desired or
        self.size2 == self.desired

