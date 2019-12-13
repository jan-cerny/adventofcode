#!/usr/bin/python3

def count_points(instructions):
	points = [(0,0)]
	for instruction in instructions:
		direction = instruction[0]
		step = int(instruction[1:])
		for _ in range(step):
			x, y = points[-1]
			if direction == "R":
				x += 1
			elif direction == "L":
				x -= 1
			elif direction == "U":
				y += 1
			elif direction == "D":
				y -= 1
			else:
				raise ValueError(instruction)
			new_point = (x, y)
			points.append(new_point)
	return points

def find_intersections(line1, line2):
	intersection = set(line1) & set(line2)
	intersection.remove((0,0))
	return list(intersection)

def distance(point):
	x, y = point
	return abs(x) + abs(y)

def find_nearest(intersections):
	nearest_point = min(intersections, key=distance)
	return distance(nearest_point)

def combined_steps(points1, points2, intersections):
	smallest = -1
	for p in intersections:
		steps1 = points1.index(p)
		steps2 = points2.index(p)
		sum_steps = steps1 + steps2
		if smallest < 0 or sum_steps < smallest:
			smallest = sum_steps 
	return smallest

def solve(wire1, wire2):
	instructions1 = wire1.split(",")
	points1 = count_points(instructions1)
	instructions2 = wire2.split(",")
	points2 = count_points(instructions2)
	intersections = find_intersections(points1, points2)
	d = find_nearest(intersections)
	print(f"Manhattan distance from the central port to the closest intersection is {d}")
	c = combined_steps(points1, points2, intersections)
	print(f"The fewest combined steps the wires must take to reach an intersection is {c}")
	return d, c

def test_solve():
	input_str1 = "R8,U5,L5,D3"
	input_str2 = "U7,R6,D4,L4"
	assert solve(input_str1, input_str2) == (6, 30)
	input_str1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
	input_str2 = "U62,R66,U55,R34,D71,R55,D58,R83"
	assert solve(input_str1, input_str2) == (159, 610)
	input_str1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
	input_str2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
	assert solve(input_str1, input_str2) == (135, 410)

if __name__ == "__main__":
	with open("input", "r") as f:
		wire1 = f.readline().strip()
		wire2 = f.readline().strip()
		solve(wire1, wire2)
