def get_area(point1, point2, point3):
    x1, y1, x2, y2, x3, y3 = point1[0], point1[1], point2[0], point2[1], point3[0], point3[1]
    return 0.5 * (((x2 - x1) * (y3 - y1)) - ((x3 - x1) * (y2 - y1)))


def get_vertex(query):
    x = (query[1] - query[0]) / 2
    print('x', x)
    y = (((query[0] - query[1]) ** 2 - (x - query[0]) ** 2 - (x - query[1]) ** 2) / 2) ** 0.5
    return [x, y]


for t in range(int(input())):
    n, q = map(int, input().split())
    points = [[int(i) for i in input().split()] for j in range(n)]
    queries = [[int(i) for i in input().split()] for j in range(q)]
    for query in queries:
        count = 0
        ver = get_vertex(query)
        print(ver)
        for point in points:
            if get_area(ver, [query[0], 0], [query[1], 0]) == get_area([query[0], 0], [query[1], 0], point) + get_area(
                    ver, [query[1], 0], point) + get_area([query[0], 0], ver, point):
                count += 1
        print(count)
