import cv2
import overlay_transparent as tp
# 선글라스 이미지 로드 (투명 배경 PNG)
sunglasses_img = cv2.imread('sample/sunglass.png', cv2.IMREAD_UNCHANGED)

def apply_sunglasses_filter(frame, gray, faces, predictor):
    for face in faces:
        landmarks = predictor(gray, face)
        # 눈 위치 찾기 (왼쪽 눈: 36~41, 오른쪽 눈: 42~47)
        left_eye = landmarks.part(36)
        right_eye = landmarks.part(45)
        eye_center = ((left_eye.x + right_eye.x) // 2, (left_eye.y + right_eye.y) // 2)
        
        scale_factor = 1.2
        # 선글라스의 크기 조정
        sunglass_width = int(1.5 * (right_eye.x - left_eye.x) * scale_factor)
        sunglass_height = int(sunglass_width * sunglasses_img.shape[0] / sunglasses_img.shape[1])
        resized_sunglass = cv2.resize(sunglasses_img, (sunglass_width, sunglass_height), interpolation=cv2.INTER_AREA)
        
        # 선글라스의 위치 결정
        top_left = (int(eye_center[0] - sunglass_width / 2), int(eye_center[1] - sunglass_height / 2) + 15)
        bottom_right = (int(eye_center[0] + sunglass_width / 2), int(eye_center[1] + sunglass_height / 2))
        
        # 선글라스 합성
        tp.overlay_transparent(frame, resized_sunglass, top_left[0], top_left[1])
    return frame