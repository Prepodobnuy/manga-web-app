from PIL import Image
import io
import os

import db.db as DataBase


def save_user_pfp(user_id: int, image_data: bytes):
    user = DataBase.user_read(id=user_id)

    if user is None: return

    path = get_user_pfp_path(user_id)
    image = Image.open(io.BytesIO(image_data))

    w, h = image.size

    if w < h:
        image = image.crop((0, 0, w, w))
    elif h < w:
        image = image.crop((0, 0, h, h))

    image = image.resize((300, 300))
    image.save(path)
    DataBase.user_edit(user_id, {"pfp_path": path})
    return 1

def get_user_pfp_path(user_id: int) -> str:
    return f'assets/pfp/{user_id}_pfp.png'

def get_user_pfp_bytes(user_id: int) -> bytes:
    if os.path.exists(get_user_pfp_path(user_id)):
        path = get_user_pfp_path(user_id)
    else:
        path = 'assets/default/default_pfp.png'

    with open(path, 'rb') as raw:
        data = raw.read()
    return data


def get_title_preview_path(title_id: int) -> str:
    return f'assets/preview/{title_id}_preview.png'

def get_title_preview_bytes(title_id: int) -> bytes:
    if os.path.exists(get_title_preview_path(title_id)):
        path = get_title_preview_path(title_id)
    else:
        path = 'assets/default/default_preview.png'

    with open(path, 'rb') as raw:
        data = raw.read()
    return data

if __name__ == '__main__':
    with open('/home/prepodobnuy/Documents/Wallpapers/MAKIMA.png', 'rb') as raw:
        image_data = raw.read()
    save_user_pfp(0, image_data)