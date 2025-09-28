from facial_emotion_recognition import EmotionRecognition
import torch
import cv2

import torch
print(torch.cuda.is_available())   # True
print(torch.cuda.get_device_name(0))

er = EmotionRecognition(device='gpu')

cam = cv2.VideoCapture(0)

while True:
	success, frame = cam.read()
	frame = er.recognise_emotion(frame, return_type='BGR')
	cv2.imshow('frame', frame)
	key = cv2.waitKey(1)
	if key == 27:
		break

cam.release()
cv2.destroyAllWindows()