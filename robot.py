class Robot(object):
    def __init__(self, table, dirs, x=0, y=0):
        self.directions = dirs
        self.direction = self.directions.index('NORTH')
        self.x = x
        self.y = y
        self.coordinates = self.x, self.y
        self.table = table

    def place(self, coordinates: tuple, orientation: str) -> object:
        """Places the robot inside the table"""
        if not coordinates[0] < 0 and coordinates[0] <= self.table[0]:
            if not coordinates[1] < 0 and coordinates[1] <= self.table[1]:
                self.x = coordinates[0]
                self.y = coordinates[1]
                self.coordinates = self.x, self.y
                self.direction = self.directions.index(orientation)
                return self

    def move(self):
        """Moves the Robot in the facing direction, but ignoring the command if
        moving would result in the robot going off the table.
        """
        if self.direction == 0 and self.x + 1 <= self.table[0]:
            self.x += 1
        if self.direction == 1 and self.y + 1 <= self.table[1]:
            self.y += 1
        if self.direction == 2 and self.x - 1 >= 0:
            self.x += -1
        if self.direction == 3 and self.y - 1 >= 0:
            self.y += -1
        self.coordinates = self.x, self.y
        return self

    def right(self):
        """Turns the robot to the right of the given facing."""
        self.direction = (self.direction - 1) % 4
        return self

    def left(self):
        """Turns the robot to the left of the given facing."""
        self.direction = (self.direction + 1) % 4
        return self

    def report(self):
        """Writes the coordinates and facing direction of the robot to the log console."""
        print(f"{self.x},{self.y},{self.directions[self.direction]}")
        return self
