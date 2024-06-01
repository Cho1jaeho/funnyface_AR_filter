import numpy as np

def overlay_transparent(background, overlay, x, y):
    background_height, background_width = background.shape[:2]
    overlay_height, overlay_width = overlay.shape[:2]

    # 위치가 음수인 경우 처리
    if x < 0:
        overlay = overlay[:, -x:]
        overlay_width = overlay.shape[1]
        x = 0
    if y < 0:
        overlay = overlay[-y:, :]
        overlay_height = overlay.shape[0]
        y = 0

    # 오버레이가 배경을 벗어나는 경우 처리
    if x + overlay_width > background_width:
        overlay = overlay[:, :(background_width - x)]
        overlay_width = overlay.shape[1]
    if y + overlay_height > background_height:
        overlay = overlay[:(background_height - y), :]
        overlay_height = overlay.shape[0]

    overlay_image = overlay[..., :3]  # RGB 채널
    mask = overlay[..., 3:] / 255.0  # 알파 채널을 0-1 범위로 정규화

    # 배경 이미지에서 오버레이를 적용할 부분을 잘라냄
    background_part = background[y:y+overlay_height, x:x+overlay_width]
    # 마스크를 이용해 오버레이 이미지와 배경을 합성
    mask = np.dstack([mask] * 3)  # 마스크를 3채널로 확장
    background_part = background_part.astype('float32')  # 연산을 위해 float 타입으로 변환
    overlay_image = overlay_image.astype('float32')

    # 알파 블렌딩 수행
    foreground_part = (mask * overlay_image)
    background_part = ((1 - mask) * background_part)
    combined = foreground_part + background_part

    # 합성된 이미지를 원본 배경에 붙여넣기
    background[y:y+overlay_height, x:x+overlay_width] = combined.astype('uint8')

    return background