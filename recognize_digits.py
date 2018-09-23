from imutils import contours
from imutils.perspective import four_point_transform
import imutils
import cv2
from matplotlib import pyplot as plt

# define the dictionary of digit segments so we can identify
# each digit on the thermostat
DIGITS_LOOKUP = {
    (1, 1, 1, 0, 1, 1, 1): 0,
    (0, 0, 1, 0, 0, 1, 0): 1,
    (1, 0, 1, 1, 1, 1, 0): 2,
    (1, 0, 1, 1, 0, 1, 1): 3,
    (0, 1, 1, 1, 0, 1, 0): 4,
    (1, 1, 0, 1, 0, 1, 1): 5,
    (1, 1, 0, 1, 1, 1, 1): 6,
    (1, 0, 1, 0, 0, 1, 0): 7,
    (1, 1, 1, 1, 1, 1, 1): 8,
    (1, 1, 1, 1, 0, 1, 1): 9
}

# load the example image
img = cv2.imread("tower.png")

# pre-process the image by resizing it, converting it to grayscale, blurring it, and computing an edge map
image = imutils.resize(img, height=500)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)

# find contours in the edge map, then sort them by their size in descending order
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
displayCnt = None


# loop over the contours
for c in cnts:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # if the contour has four vertices, then we have found the thermostat display
    if len(approx) == 4:
        displayCnt = approx
        break

buffer = 30
x,y,w,h = cv2.boundingRect(displayCnt)
x -= buffer
y -= buffer
w += 2*buffer
h += 2*buffer
cropped_img = gray[y:y+h, x:x+h]

thresh = cv2.threshold(cropped_img, 0, 255,
    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
# thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
digitsCnts = []

for c in cnts:
    # compute the bounding box of the contour
    (x, y, h, w) = cv2.boundingRect(c)
    cv2.rectangle(thresh, (x,y), (x+w,y+h),(0.255,0),2)

plt.imshow(thresh)
plt.show()
