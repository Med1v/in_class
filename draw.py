import cv2
import numpy as np
import win32gui

draw = False
brush_colour = (255, 204, 153)
screen_size = (640, 640, 3)
colour_screen_size = (200, 200, 3)
brush_size = 30
enable_colour_win = False


img = np.zeros(screen_size, np.uint8)
colour_img = np.zeros(colour_screen_size, np.uint8)

def nothing(x):
    pass


# mouse callback function
def get_pixel_colour(event,x,y,flags,param):
    global colour_img
    print("test")


def draw_circle(event,x,y,flags,param):
    global draw
    # print(x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        cv2.circle(img, (x,y), brush_size, brush_colour, -1)
    if event == cv2.EVENT_LBUTTONUP:
        draw = False
    if event == cv2.EVENT_MOUSEMOVE:
        if draw:
            # blue, green, red
            cv2.circle(img, (x,y), brush_size, brush_colour, -1)


for i in range(colour_screen_size[0]):
    for j in range(colour_screen_size[1]):
        b = round(j/20)*20
        g = round(i/20)*20
        r = round((i+j)/20)*20
        colour_img[i][j] = [b, g, r]


img.fill(255)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

cv2.namedWindow('colour')

while(1):
    cv2.imshow('image', img)
    if enable_colour_win:
        cv2.imshow('colour', colour_img)
        cv2.moveWindow('colour', 810, 150)
    else:
        cv2.destroyWindow('colour')
    k = cv2.waitKey(1) & 0xFF
    # print(k)
    if k == ord('c'):
        img.fill(255)
    elif k == ord('m'):
        enable_colour_win = not enable_colour_win
    elif k == 46:
        brush_size += 5
    elif k == 44:
        brush_size -= 5
    elif k == 27:
        break
cv2.destroyAllWindows()