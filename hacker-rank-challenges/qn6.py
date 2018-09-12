if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = (sum(student_marks[query_name])/3)
    print('%.2f' % (avg))

marks = {}
for _ in range(int(input())):
    line = input().split()
    marks[line[0]] = list(map(float, line[1:]))
print('%.2f' % (sum(marks[input()])/3))
