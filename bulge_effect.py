import cv2
import numpy as np

def apply_bulge_effect(frame, faces, strength=0.01, radius_scale=1.5):
    if faces:
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            center_x, center_y = x + w // 2, y + h // 2
            radius = int(min(w, h) * radius_scale / 2)
            map_x, map_y = np.indices((frame.shape[0], frame.shape[1]), dtype=np.float32)
            dx = map_x - center_y
            dy = map_y - center_x
            distance = np.sqrt(dx**2 + dy**2)
            valid = distance < radius
            scale = 1 + np.exp(-distance[valid] * strength) - np.exp(-radius * strength)
            map_x[valid] = center_y + dx[valid] * scale
            map_y[valid] = center_x + dy[valid] * scale
            frame = cv2.remap(frame, map_y, map_x, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)
    return frame