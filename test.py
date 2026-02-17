import cv2
import numpy as np
from math import sin, cos, pi

def shuffle(a_list):
        if len(a_list) % 2 == 1:
            print("Odd list length")
            return a_list
        n = int(len(a_list) / 2)
        b_list = []
        for i in range(n):
            b_list.append(a_list[i])
            b_list.append(a_list[i + n])
        return b_list


N = 52

l = list(range(1, N + 1))

count = 1
l_s = shuffle(l)

while l_s != l:
    l_s = shuffle(l_s)
    count += 1

l_s = shuffle(l)
map = []

for item in l:
    map.append(l_s.index(item)) # honnan hova kerül


print(N, " : ", count)

CANVAS_WIDTH = 800
CANVAS_HEIGHT = CANVAS_WIDTH

canvas = np.zeros((CANVAS_WIDTH, CANVAS_HEIGHT, 3), dtype="uint8")

nodes = [(round(cos(angle*2*pi/N - pi / 2) * CANVAS_WIDTH / 3 + CANVAS_WIDTH / 2), round(sin(angle*2*pi/N - pi / 2) * CANVAS_HEIGHT / 3 + CANVAS_HEIGHT / 2)) for angle in range(N)]

for i, node in enumerate(nodes):
     cv2.circle(canvas, node, 2, (255, 255, 255), -1)
     #cv2.putText(canvas, str(i + 1), (np.array(node)).astype(np.int32).tolist(), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

for node_from, node_to in enumerate(map):
     #cv2.arrowedLine(canvas, nodes[node_from], nodes[node_to], (155, 155, 155), 2)
     cv2.line(canvas, nodes[node_from], nodes[node_to], (215, 155, 155), 1)


cv2.imshow("Test", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


