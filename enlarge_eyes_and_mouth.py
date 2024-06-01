import cv2

def apply_enlarge(frame, gray, faces, predictor):
    for face in faces:
        landmarks = predictor(gray, face)
        # 눈 확대
        for i in [36, 45]:
            eye_center = landmarks.part(i)
            eye_left = (eye_center.x - 25, eye_center.y - 25)
            eye_right = (eye_center.x + 25, eye_center.y + 25)
            eye_area = frame[eye_left[1]:eye_right[1], eye_left[0]:eye_right[0]]
            if eye_area.size > 0:
                enlarged_eye = cv2.resize(eye_area, (0, 0), fx=2, fy=2)
                frame[eye_left[1]:eye_left[1] + enlarged_eye.shape[0], eye_left[0]:eye_left[0] + enlarged_eye.shape[1]] = enlarged_eye
        # 입 확대
        mouth_center = landmarks.part(62)
        mouth_left = (mouth_center.x - 50, mouth_center.y - 30)
        mouth_right = (mouth_center.x + 50, mouth_center.y + 30)
        mouth_area = frame[mouth_left[1]:mouth_right[1], mouth_left[0]:mouth_right[0]]
        if mouth_area.size > 0:
            enlarged_mouth = cv2.resize(mouth_area, (0, 0), fx=2, fy=2)
            frame[mouth_left[1]:mouth_left[1] + enlarged_mouth.shape[0], mouth_left[0]:mouth_left[0] + enlarged_mouth.shape[1]] = enlarged_mouth
    return frame