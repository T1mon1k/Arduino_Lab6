import cv2
camera = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier(
	"/usr/share/opencv4/haarcascades/"
	"haarcascade_frontalface_default.xml"
)

if not camera.isOpened():
	raise SystemExit("Camera unavailable")

if detector.empty():
	camera.release()
	raise SystemExit("Face classifier not found")

detection = False

try:
	while True:
		ok, frame = camera.read()
		if not ok:
			break

		if detection:
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces = detector.detectMultiScale(
				gray, scaleFactor=1.1,
				minNeighbors=5, minSize=(60, 60)
			)
			for x, y, w, h in faces:
				cv2.rectangle(
					frame, (x, y), (x + w, y + h),
					(0, 255, 0), 2
				)

		cv2.imshow("my_face | D: detection | Q: exit", frame)
		key = cv2.waitKey(1) & 0xFF

		if key == ord("d"):
			detection = not detection
		elif key == ord("q"):
			break
finally:
	camera.release()
	cv2.destroyAllWindows()
