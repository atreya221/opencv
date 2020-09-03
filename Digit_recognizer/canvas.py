# Left click and drag to draw on the canvas
# Right click and drag to erase drawing
# Press 'c' to clear the canvas
# Press 's' to save the drawing
# Press 'q' to quit the application

import numpy as np
import cv2

img = np.zeros([200, 200], dtype = 'uint8')
wname = 'Background'

cv2.namedWindow(wname)
draw_state = False
erase_state = False

def shape(event, x, y, flags, param):  # Function to be defined for mouse event
    
    global draw_state
    global erase_state
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 8, (255,255), -1, cv2.LINE_AA)
        draw_state = True
        
    if event == cv2.EVENT_LBUTTONUP:
        draw_state = False

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (0,0), -1, cv2.LINE_AA)
        erase_state = True

    if event == cv2.EVENT_RBUTTONUP:
        erase_state = False
        
    if draw_state == True and event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img, (x, y), 8, (255,255), -1, cv2.LINE_AA)
        
    if erase_state == True and event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img, (x, y), 20, (0,0), -1, cv2.LINE_AA)




while True:
    cv2.setMouseCallback(wname, shape)  #  Window Name, Function to be defined for mouse event
    cv2.imshow(wname, img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        def returnfn():
            global img
            img = cv2.resize(img, (28,28))
            return img
        break
    elif key == ord('c'):
        img[:,:] = 0
    elif key == ord('s'):
        out = cv2.resize(img, (28,28))
        #print(out.shape)
        cv2.imwrite('test.jpg', out)
cv2.destroyAllWindows()
