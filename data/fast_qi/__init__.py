from pathlib import Path
from typing import List

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def fast_qi(images: List[BuildImage], texts, args):
    self_loc = (120, 15)
    user_loc = (45, 80)

    self_head = (
        images[0]
        .convert("RGBA")
        .resize((70, 70), keep_ratio=True)
        .circle()
        .rotate(0)
    )
    user_head = (
        images[1]
        .convert("RGBA")
        .resize((70, 70), keep_ratio=True)
        .circle()
        .rotate(15)
    )

    frames: List[IMG] = []
    for i in range(3):
        frame = BuildImage.open(img_dir / f"{i}.png")
        frame.paste(user_head, user_loc, alpha=True)
        frame.paste(self_head, self_loc, alpha=True)
        frames.append(frame.image)

    return save_gif(frames, 0.02)


add_meme("fast_qi", fast_qi, min_images=2, max_images=2, keywords=["狠骑"])