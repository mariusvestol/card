import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)


def countPix(mask):
	return cv.countNonZero(mask)
#denne kan jeg ikke

newVal = 0
val = 0 

""" Directonarys in python:
Each key must be unique, and it is associated with a value """

color_ranges = {
    "red": ([0, 120, 70], [10, 255, 255]),  # Red (hue wraps around at 0 and 180)
    "green": ([36, 50, 50], [70, 255, 255]),  # Green
}

pixel_counts = {}


while True:
	isTrue, frame = capture.read()

#denne lager grayscale
	#gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	
	#denne lager HSV 
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

	for color, (lower, upper) in color_ranges.items():
		lowerBound = np.array(lower)
		upperBound = np.array(upper)

		mask = cv.inRange(hsv, lowerBound, upperBound)

		pixelCount = countPix(mask)

		pixel_counts[color] = pixelCount


	dominant = max(pixel_counts, key=pixel_counts.get)
#forstår ikke denne men tror max gir den med mest

	newVal = dominant
	if newVal == val:
		print(newVal)
	val = newVal

	cv.imshow('Video', hsv)

	if not capture.isOpened():
		print("test")



	if cv.waitKey(20) & 0xFF==ord('d'):
		break


capture.release()
cv.destroyAllWindows()

