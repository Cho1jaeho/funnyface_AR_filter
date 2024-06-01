import cv2
import overlay_transparent as tp

# 모자 이미지 로드 (투명 배경 PNG)
hat_image = cv2.imread('sample/hat.png', -1)

def apply_hat_filter(frame, gray, faces, predictor):
    for face in faces:
        landmarks = predictor(gray, face)
        forehead = landmarks.part(27)
        face_width = face.right() - face.left()
        # 모자의 너비와 높이 조절
        hat_width = int(face_width * 1.5)
        hat_height = int(hat_width * hat_image.shape[0] / hat_image.shape[1])
        # 모자 리사이징
        hat_resized = cv2.resize(hat_image, (hat_width, hat_height), interpolation=cv2.INTER_CUBIC)
        # 모자 위치 설정
        x = forehead.x - hat_width // 2 - 30
        y = forehead.y - hat_height + 70 # 이마 위치에서 모자가 머리 위로 올라가도록 조정
        frame = tp.overlay_transparent(frame, hat_resized, x, y)
    return frame
