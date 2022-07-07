class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """

class Solution:
  def cleanRoom(self, robot: Robot):
    def backtrace(pos, dir):
      # dir: up - 0, right - 1, down - 2, left - 3
      visited.add(pos)
      robot.clean()

      for idx in range(4):
        next_dir = (dir + idx) % 4
        next_cell = (pos[0] + directions[next_dir][0], pos[1] + directions[next_dir][1])

        if next_cell not in visited and robot.move():
          backtrace(next_cell, next_dir)
          robot.turnRight()
          robot.turnRight()
          robot.move()
          robot.turnRight()
          robot.turnRight()

        robot.turnRight()

    visited = set()
    # up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    backtrace((0, 0), 0)

