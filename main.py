import cv2
import dlib
import enlarge_eyes_and_mouth
import hat_filter
import bulge_effect
import concave_effect
import sunglasses_filter
import hamster_filter
import dog_filter

# Dlib의 얼굴 검출기와 랜드마크 검출기 초기화
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('sample/shape_predictor_68_face_landmarks.dat')

# 웹캠 캡처 초기화
cap = cv2.VideoCapture(0)

# 필터 리스트
filters = ['original', 'enlarge_eyes_and_mouth', 'hat_filter', 'bulge_effect', 'concave_effect', 'sunglasses_filter', 'hamster_filter', 'dog_filter', 'color_invert']

# 현재 선택된 필터 인덱스
current_filter_index = 0

def apply_filter(frame, filter_type):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    if filter_type == 'original':
        pass
    elif filter_type == 'enlarge_eyes_and_mouth':
        frame = enlarge_eyes_and_mouth.apply_enlarge(frame, gray, faces, predictor)
    elif filter_type == 'hat_filter':
        frame = hat_filter.apply_hat_filter(frame, gray, faces, predictor)
    elif filter_type == 'bulge_effect':
        frame = bulge_effect.apply_bulge_effect(frame, faces)
    elif filter_type == 'concave_effect':
        frame = concave_effect.apply_concave_effect(frame, faces)
    elif filter_type == 'sunglasses_filter':
            frame = sunglasses_filter.apply_sunglasses_filter(frame, gray, faces, predictor)
    elif filter_type == 'hamster_filter':
        frame = hamster_filter.apply_hamster_filter(frame)
    elif filter_type == 'dog_filter':
        frame = dog_filter.apply_dog_face_fileter(frame, gray, faces, predictor)
    elif filter_type == 'color_invert':
        frame = cv2.bitwise_not(frame)
    return frame

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 현재 필터 적용
    frame = apply_filter(frame, filters[current_filter_index])

    # 화면에 결과 표시
    cv2.imshow('Funny Face Effects', frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == 9:  # Tab 키
        current_filter_index = (current_filter_index + 1) % len(filters)

cap.release()
cv2.destroyAllWindows()