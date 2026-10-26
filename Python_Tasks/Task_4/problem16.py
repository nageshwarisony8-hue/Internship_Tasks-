# Problem: Nested Lists
# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem

students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(set(score for name, score in students))
second_lowest = scores[1]

for name, score in sorted(students):
    if score == second_lowest:
        print(name)
