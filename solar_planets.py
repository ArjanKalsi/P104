import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (20, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Mercury", (110, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Venus", (190, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Earth", (290, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Mars", (382, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Jupiter", (550, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Saturn", (775, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Uranus", (970, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Neptune", (1117, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Pluto", (1227, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))

cv2.imshow("output", img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)