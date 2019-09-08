# if __name__ == '__main__':
#     n = int(input())
#     points = []
#     all_points = set()
#     for i in range(n):
#         point = list(map(int, input().split(' ')))
#         points.append(point)

#     for item in points:
#         start = [item[0], item[1]]
#         end = [item[2], item[3]]

#         # 说明是列
#         if start[0] != end[0] and start[1] == end[1]:
#             start_x = None
#             if start[0] <= end[0]:
#                 start_x = start[0]
#             else:
#                 start_x = end[0]

#             # 本身的点放进去
#             all_points.add((start_x, start[1]))
#             for i in range(abs(start[0]-end[0])):
#                 all_points.add((start_x + i + 1, start[1]))

#         # 说明是行
#         if start[1] != end[1] and start[0] == end[0]:
#             start_y = None
#             if start[1] <= end[1]:
#                 start_y = start[1]
#             else:
#                 start_y = end[1]

#             # 本身的点放进去
#             all_points.add((start[0], start_y))
#             for i in range(abs(start[1]-end[1])):
#                 all_points.add((start[0], start_y + i + 1))



#     print(len(all_points))

if __name__ == '__main__':
    n = int(input())
    points = {
        'row': [],
        'col': []
    }


    all_points_num = 0
    for i in range(n):
        point = list(map(int, input().split(' ')))

        start = [point[0], point[1]]
        end = [point[2], point[3]]

        # 说明是列
        if start[0] != end[0] and start[1] == end[1]:
            points['col'].append(point)
            all_points_num += (abs(start[0] - end[0]) + 1)

        # 说明是行
        if start[1] != end[1] and start[0] == end[0]:
            points['row'].append(point)
            all_points_num += (abs(start[1] - end[1]) + 1)

    for row in points['row']:
        for col in points['col']:
            start = None
            end = None
            if col[1] <= col[3]:
                start = col[1]
                end = col[3]

            else:
                start = col[3]
                end = col[1]

            if start <= row[1] and row[1] <= end:
                print('aaa')
                all_points_num =- 1
    print(all_points_num)
            





































