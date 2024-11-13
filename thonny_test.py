student_heights = input().split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0

for h in student_heights:
  total_height += h

print(f"Total height is {total_height}")