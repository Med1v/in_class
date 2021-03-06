import cv2
import numpy as np
# import win32gui

show_colours = False
draw = False
brush_colour = (255, 204, 153)
screen_size = (640, 640, 3)
brush_size = 30


img = np.zeros(screen_size, np.uint8)


def draw_circle(event, x, y, flags, param):
    global draw, brush_colour
    step_len = 20
    # print(x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        cv2.circle(img, (x, y), brush_size, brush_colour, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            # blue, green, red
            cv2.circle(show_img, (x, y), brush_size, brush_colour, -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cc = y / step_len * (255 / (screen_size[1] / step_len))
        brush_colour = (cc, cc, cc)
        print("colour change")


def gen_colours(img):
    arr = np.zeros((screen_size[1], 50, 3), dtype='uint8')
    step_len = 20
    print(len(arr), len(arr[0]))
    b, g, r, tmp = 0, 0, 0, 0
    for y in range(1, len(arr)):
        if y % step_len == 0:
            tmp = y / step_len * (255 / (len(arr) / step_len))
            b = tmp
            g = tmp
            r = tmp
            # if y<len(arr)/3:
            #     b = round(tmp)
            #     g = 0
            #     r = 0
            # if y<len(arr)/3*2:
            #     b = 0
            #     g = round(tmp)
            #     r = 0
            # if y>len(arr)/3*2:
            #     b = 0
            #     g = 0
            #     r = round(tmp)
        for x in range(len(arr[0])):
            arr[y][x] = [b, g, r]
    return np.append(img, arr, axis=1)


img.fill(255)
show_img = img
colours = gen_colours(img)
# print(colours)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

# cv2.namedWindow('colour')

while(1):
    cv2.imshow('image', show_img)
    k = cv2.waitKey(1) & 0xFF
    # print(k)

    if show_colours:
        show_img = colours
    else:
        show_img = img
    if k == ord('c'):
        img.fill(255)
    elif k == ord('m'):
        # print("switch colour")
        show_colours = not show_colours
    elif k == 46:
        brush_size += 5
    elif k == 44:
        brush_size -= 5
    elif k == 27:
        break
cv2.destroyAllWindows()
