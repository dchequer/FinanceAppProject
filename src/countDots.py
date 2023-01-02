import cv2
import numpy as np

# define range of black color
black = [0, 100]
lower, upper = black


def countDots(img) -> int:
    #handle img
    img = handleIncomingBytes(img)  
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    # smooth image by 7x7 pixels, may need to adjust a bit
    blur = cv2.medianBlur(grayscale, 7)
    # apply threshhold color to white (255,255, 255) and the rest to black(0,0,0)
    mask = cv2.inRange(blur,lower,upper)
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 20, param1=20, param2=8, minRadius=10, maxRadius=20)
    circleCount = 0
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")


    # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image,
            #   then draw a rectangle corresponding to the center of the circle
            cv2.circle(img, (x, y), r, (255, 0, 255), 2)
            cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (255, 0, 255), -1)

            circleCount += 1
    output_bytes = cv2.imencode('.png', img)[1].tobytes()
    return circleCount, output_bytes

def handleIncomingBytes(img_bytes):
    img_array = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)  # decode img from np array
    dsize = (768, 1024) if img.shape[0] > img.shape[1] else (1024, 768)  # if img is portrait, resize to 1280x720, else 720x1280
    img = cv2.resize(img, dsize= dsize)  # resize img to 1920x1080
    return img