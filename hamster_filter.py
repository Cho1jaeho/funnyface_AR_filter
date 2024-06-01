import cv2
import numpy as np

def apply_hamster_filter(frame):
    
    hamster_img_path = 'sample/hamster.png'
    # 햄스터 이미지 로드 (투명 배경 PNG)
    hamster_img = cv2.imread(hamster_img_path, cv2.IMREAD_UNCHANGED)
    
    # 이미지의 크기를 조절
    scale_factor = 0.9  # 이미지 크기 조절 비율
    resized_hamster = cv2.resize(hamster_img, 
                                 (int(hamster_img.shape[1] * scale_factor), int(hamster_img.shape[0] * scale_factor)), 
                                 interpolation=cv2.INTER_AREA)
    
    # 합성할 위치 계산 (화면 중앙)
    start_y = frame.shape[0] - resized_hamster.shape[0] - 10  # 프레임 높이에서 햄스터 높이를 빼고, 10 픽셀 여유를 둠
    start_x = frame.shape[1] - resized_hamster.shape[1]  # 프레임 너비에서 햄스터 너비를 빼고, 10 픽셀 여유를 둠
    
    # 선글라스 이미지 합성을 위한 알파 값 계산
    alpha_s = resized_hamster[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s
    
    # 선글라스를 배경에 합성
    for c in range(0, 3):
        frame[start_y:start_y + resized_hamster.shape[0], start_x:start_x + resized_hamster.shape[1], c] = (
            alpha_s * resized_hamster[:, :, c] +
            alpha_l * frame[start_y:start_y + resized_hamster.shape[0], start_x:start_x + resized_hamster.shape[1], c]
        )
    
    return frame