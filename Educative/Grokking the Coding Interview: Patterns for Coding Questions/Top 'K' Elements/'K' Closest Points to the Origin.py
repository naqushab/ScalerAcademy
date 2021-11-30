"""
Problem Statement#
Given an array of points in a 2D2D plane, find ‘K’ closest points to the origin.
"""

from heapq import heappop, heappush

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __lt__(self, other):
    return self.dis_from_origin() > other.dis_from_origin()

  def dis_from_origin(self):
    return (self.x * self.x) + (self.y + self.y)

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

def find_closest_points(points, k):
  result = []
  # TODO: Write your code here
  for p in points[:k]:
    heappush(result, p)

  for p in points[k:]:
    if p.dis_from_origin() < result[0].dis_from_origin():
      heappop(result)
      heappush(result, p)
  return result


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()


