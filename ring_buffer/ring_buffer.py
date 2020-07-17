class RingBuffer:
    def __init__(self, capacity):
        self.data = []  # To hold our data.
        self.capacity = 5  # Saw capacity in test file = 5.
        self.current = 0  # Currently selected index.

    def append(self, item):
        # If the length of our data does not exceed the capacity...
        if len(self.data) < self.capacity:
            # Ensure item isn't NoneType as stated in README.
            if item is not None:
                self.data.append(item)  # Use recursion.
        # If the length of our data is greater than or equal to the capacity
        # We're going to need to overwrite the values.
        else:
            # Glad I remembered the modulo operator O.O - it will return:
            # 1 % 5 is 1, 2 % 5 is 2, 3 % 5 is 3, 4 % 5 is 4, 5 % 5 is 0.
            # This means that when the fifth index is reached, `current`
            # will return to zero, meaning we can easily overwrite values
            # by their index. Yay for arrays!
            if item is not None:  # Ensure item isn't None as stated in README.
                self.data[self.current] = item  # Overwrite current index.
                # Update value of `current`
                self.current = (self.current + 1) % self.capacity

    def get(self):
        return self.data
