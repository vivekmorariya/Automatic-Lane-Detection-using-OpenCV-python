import cv2 as cv
import numpy as np


def make_coordinates(image, line_parameters):
    try:
        slope, intercept = line_parameters
        y1 = image.shape[0]
        y2 = int(y1 * (3 / 5))
        x1 = int((y1 - intercept) / slope)
        x2 = int((y2 - intercept) / slope)
        return np.array([x1, y1, x2, y2])
    except:
        np.array([0, 0, 0, 0])


def average_slope_intercept(image, lines):
    try:
        left_fit = []
        right_fit = []
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            slope = parameters[0]
            intercept = parameters[1]

            if slope < 0:
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))

        left_fit_average = np.average(left_fit, axis=0)
        right_fit_average = np.average(right_fit, axis=0)

        left_line = make_coordinates(image, left_fit_average)
        right_line = make_coordinates(image, right_fit_average)
        return np.array([left_line, right_line])
    except:
        return np.array([0,0])


def edge_detection(image):
    if (image is not None):
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (5, 5), 0)
        canny = cv.Canny(blur, 50, 150)
        return canny
    else:
        return image


def display_line(image, lines):
    try:
        line_image = np.zeros_like(image)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)
                cv.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
        return line_image
    except:
        return image


def region_of_interest(image):
    if (image is not None):
        height = image.shape[0]
        polygons = np.array([[(200, height), (1100, height), (550, 250)]])
        mask = np.zeros_like(image)
        cv.fillPoly(mask, polygons, 255)
        masked_image = cv.bitwise_and(image, mask)
        return masked_image
    else:
        return image

# image = cv.imread("test_image.jpg")
# lane_image = np.copy(image)
# canny_image = edge_detection(lane_image)
# cropped_image = region_of_interest(canny_image)
# lines = cv.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
# average_lines = average_slope_intercept(lane_image, lines)
# line_image = display_line(lane_image, average_lines)
# combo_image = cv.addWeighted(lane_image, 0.8, line_image, 1, 1)
# new_steering_angle = compute_steering_angle(image, average_lines)
# print(new_steering_angle)
# current_heading_image = display_heading_line(combo_image, new_steering_angle)
# cv.imshow("Image", current_heading_image)
# cv.waitKey(0)
# cv.destroyAllWindows()

cap = cv.VideoCapture("test2.mp4")
while (cap.isOpened()):
    _, frame = cap.read()
    canny_image = edge_detection(frame)
    cropped_image = region_of_interest(canny_image)

    lines = cv.HoughLinesP(cropped_image, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    average_lines = average_slope_intercept(frame, lines)
    line_image = display_line(frame, average_lines)
    combo_image = cv.addWeighted(frame, 0.8, line_image, 1, 1)
    try:
        cv.imshow("Image", combo_image)
    except:
        break
    if cv.waitKey(1) == ord("q"):
        break
cap.release()
cv.destroyAllWindows()
