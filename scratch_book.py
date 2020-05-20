from typing import List


def maxPoints(points: List[List[int]]) -> int:
        # y = mx + b
        #Construct power set of points List.
        #Construct set of lines from these set of two points
            #For each line count which points lie on that line
        if len(points) == 0:
            return 0
        elif len(points) == 1:
            return 1
        combination_of_pairs = []
        maxIntercept = 0
        N = len(points)
        for i in range(N):
            for j in range(i+1,N):
                combination_of_pairs.append([points[i], points[j]])
        while combination_of_pairs:
            pair = combination_of_pairs.pop()
            count = 0
            y_2, y_1, x_2, x_1 = pair[1][1], pair[0][1], pair[1][0], pair[0][0]
            delta_y,delta_x = y_2-y_1, x_2-x_1
            print('{} {}'.format(pair[0],pair[1]))
            for point in points:
                check_x,check_y = point
                print('({},{})'.format(check_x,check_y))
                if delta_y==0 and delta_x==0:
                    if check_x == x_1 and check_y == y_1:
                        print('count0')
                        count = count + 1
                elif delta_y==0 and delta_x!=0:
                    if check_y == y_1:
                        count = count + 1
                        print('count1')
                elif delta_y!=0 and delta_x==0:
                    if check_x == x_1:
                        count = count + 1
                        print('count2')
                else:
                    slope = (delta_y)/(delta_x)
                    b = y_1 - (slope*x_1)
                    if check_y == (slope*check_x) + b:
                        count = count + 1
                        print('count3 {} {} {}'.format(check_y,(slope*check_x) + b,check_y == (slope*check_x) + b))
            if count > maxIntercept:
                maxIntercept = count
            print(count)
            print('\n')
        return maxIntercept


if __name__ == '__main__':
    points = [[3,1],[12,3],[3,1],[-6,-1]]
    maxPoints(points)