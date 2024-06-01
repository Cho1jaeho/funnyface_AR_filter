import cv2

dog_filter_img = cv2.imread('sample/dog.png', cv2.IMREAD_UNCHANGED)

def apply_dog_face_fileter(frame, gray, faces, predictor):
    for face in faces:
        landmarks = predictor(gray, face)
        
        # 강아지 필터 크기 및 위치 조정
        nose = landmarks.part(33)  # 코의 중심 위치
        eye_left = landmarks.part(36)  # 왼쪽 눈
        eye_right = landmarks.part(45)  # 오른쪽 눈
        
        # 필터 크기 조정
        scale_factor = 1.6
        dog_filter_width = int((eye_right.x - eye_left.x) * scale_factor)
        dog_filter_height = int(dog_filter_width * dog_filter_img.shape[0] / dog_filter_img.shape[1])
        resized_dog_filter = cv2.resize(dog_filter_img, (dog_filter_width, dog_filter_height))
        
        # 필터의 코 위치를 사용자의 코 위치에 맞춤
        # 예를 들어, 필터 이미지의 코가 이미지 높이의 60% 위치에 있다고 가정
        filter_nose_offset_y = int(resized_dog_filter.shape[0] * 0.60)
        
        # 코 위치를 중심으로 필터를 배치
        top_left_x = nose.x - resized_dog_filter.shape[1] // 2
        top_left_y = nose.y - filter_nose_offset_y
        
        # 이미지 합성
        for i in range(3):  # RGB 채널
            alpha_dog = resized_dog_filter[:, :, 3] / 255.0
            alpha_frame = 1.0 - alpha_dog
            frame[top_left_y:top_left_y + resized_dog_filter.shape[0], top_left_x:top_left_x + resized_dog_filter.shape[1], i] = (
                alpha_dog * resized_dog_filter[:, :, i] +
                alpha_frame * frame[top_left_y:top_left_y + resized_dog_filter.shape[0], top_left_x:top_left_x + resized_dog_filter.shape[1], i]
            )
    return frame