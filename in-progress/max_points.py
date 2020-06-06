from typing import List

def maxPoints(points: List[List[int]]):
    maxIntercept = 0
    error_tolerance = 0.0000000001
    points = [tuple(point) for point in points]
    unique_points = {}
    for point in points:
        if unique_points.get(point) is not None:
            unique_points[point] += 1
        else:
            unique_points[point] = 1
    points = list(unique_points.keys())
    N = len(unique_points)
    if N == 0:
        return 0
    elif N == 1:
        return unique_points[points[0]]
    for i in range(N):
        for j in range(i+1,N):
            two_pair = [points[i],points[j]]
            count = 0
            y_2, y_1, x_2, x_1 = two_pair[1][1], two_pair[0][1], two_pair[1][0], two_pair[0][0]
            delta_y,delta_x = y_2-y_1, x_2-x_1
            for point in points:
                check_x,check_y = point
                # When the two points using to make the line are the exact same points
                if delta_y==0 and delta_x==0:
                    if point == two_pair[0]:
                        count += unique_points[point]
                elif delta_y==0 and delta_x!=0:
                    if check_y == y_1:
                        count += unique_points[point]
                elif delta_y!=0 and delta_x==0:
                    if check_x == x_1:
                        count += unique_points[point]
                else:
                    slope = (delta_y)/(delta_x)
                    b = y_1 - (slope*x_1)
                    error = abs(check_y - (slope*check_x) - b)
                    if error < error_tolerance:
                        count += unique_points[point]
            if count > maxIntercept:
                maxIntercept = count
    return maxIntercept

if __name__ == '__main__':
    set_of_points = [
        [[0,0],[94911151,94911150],[94911152,94911151]],
        [[0,0],[0,0]],
        [[0,0]],
        []
    ]
    for points in set_of_points:
        print(maxPoints(points))

#[[3,1],[12,3],[3,1],[-6,-1]]                                  4
#[[1,1],[1,1],[0,0],[3,4],[4,5],[5,6],[7,8],[8,9]]             5
#[[0,0],[0,0]]                                                 2
#[[0,0]]                                                       1
#[]                                                            0