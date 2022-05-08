from robot import Robot
from table import Table
from re import compile, X

if __name__ == '__main__':
    dirs = ["EAST", "NORTH", "WEST", "SOUTH"]
    table = Table(5, 5)
    robot = Robot(table.range, dirs)
    pattern = compile(r"""(?<=^)                                    # start
                              (?P<cmd>MOVE$|LEFT$|RIGHT$|REPORT$|PLACE  # command
                              (?=\s?                                    # space
                              (?P<x>\d+),                               # x co-ord
                              (?P<y>\d+),                               # y co-ord
                              (?P<dir>EAST|NORTH|WEST|SOUTH)            # direction
                              $))                                       # EOL
                              """, X)
    with open('example/move_robot_1.txt') as f:
        for line in f:
            m = pattern.match(line.rstrip('\n'))
            if m is not None and m.group("cmd") == "PLACE":
                robot = robot.place((int(m.group("x")), int(m.group("y"))),
                                    m.group("dir"))
            elif hasattr(robot, m.group("cmd").lower()):
                robot = getattr(robot, m.group("cmd").lower())()
