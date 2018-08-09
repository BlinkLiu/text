m = int(input())
matrix = list(map(int, input().strip().split(' ')))
robot1 = 0
robot2 = 0
nm = 0
while len(matrix) != 0:
    if len(matrix) == 1:
        if nm == 0:
            robot1 += matrix[0]
        if nm == 1:
            robot2 += matrix[0]
        matrix.pop(0)
    elif matrix[0] > matrix[-1]:
        if nm == 0:
            robot1 += matrix[0]
            nm = 1
        else:
            robot2 += matrix[0]
            nm = 0
        matrix.pop(0)
    else:
        if nm == 0:
            robot1 += matrix[-1]
            nm = 1
        else:
            robot2 += matrix[-1]
            nm = 0
        matrix.pop(-1)

if robot1 > robot2:
    print(1)
elif robot1 == robot2:
    print(0)
else:
    print(2)
