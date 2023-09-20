#!/usr/bin/python3
"""
Module: CGPA Calculator
Author: Mire
Description: Calculates the Cumulative Grade Point Average using Nigerian system
TLU = Total Load Unit
TCP = Total Credit Point
"""
from functools import reduce

def main():
	grade_list, course_unit_list = GetInput()
	TLU = reduce(lambda x, y: x + y, course_unit_list)
	TCP = calculate_TCP(grade_list, course_unit_list)
	print(f"Your GPA is {(TCP/TLU):.2f}")

def GetInput():
	"""
	Gets all need input value from user
	returns: list of grades and credit unit
	"""
	while True:
		count = input("How many courses in total?: ")
		if count.isdigit():
			count = int(count)
			break
		else:
			print("Invalid Input: enter a valid number")

	grade_list = []
	unit_list = []
	for x in range(count):
		current_grade, current_unit = input(f"Grade and Credit Unit for Course {x + 1}(grade, CU): ").split(", ")
		if current_grade.upper() == 'A':
			grade_list.append(5)
		elif current_grade.upper() == 'B':
			grade_list.append(4)
		elif current_grade.upper() == 'C':
			grade_list.append(3)
		elif current_grade.upper() == 'D':
			grade_list.append(2)
		elif current_grade.upper() == 'E':
			grade_list.append(1)
		elif current_grade.upper() == 'F':
			grade_list.append(0)
		unit_list.append(int(current_unit))
	return grade_list, unit_list

def calculate_TCP(grades=[], units=[]):
	total = 0
	for x in range(len(grades)):
		total += grades[x] * units[x]
	return total

if __name__ == '__main__':
	main()