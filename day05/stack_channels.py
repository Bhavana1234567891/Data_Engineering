
import numpy as np
from PIL import Image

SIZE = 8


# TASK 1: Create solid RGB images
def solid(rgb: tuple[int, int, int]) -> np.ndarray:
    image = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)
    image[:, :] = rgb
    return image


# Combine 3 RGB images into 9 channels
def stack_rgb(frames: list[np.ndarray]) -> np.ndarray:
    # Frames are RGB, shape (H, W, 3). Output is (9, H, W).
    channels = [
        frame[:, :, color]
        for frame in frames
        for color in range(3)
    ]
    return np.stack(channels, axis=0)


frames = [
    solid((255, 0, 0)),  # t-2 red
    solid((0, 255, 0)),  # t-1 green
    solid((0, 0, 255)),  # t blue
]

stack9 = stack_rgb(frames)

assert stack9.shape == (9, SIZE, SIZE)
assert int(stack9[0].mean()) == 255
assert int(stack9[4].mean()) == 255
assert int(stack9[8].mean()) == 255

print("9-channel stack ok", stack9.shape)


# TASK 2: Add three mask channels
mask = np.zeros((SIZE, SIZE), dtype=np.uint8)
mask[:, 4:] = 255

stack12 = np.concatenate(
    [stack9, np.stack([mask, mask, mask], axis=0)],
    axis=0
)

assert stack12.shape == (12, SIZE, SIZE)
assert int(stack12[9, 0, 0]) == 0
assert int(stack12[9, 0, 4]) == 255
assert int(stack12[11, 0, 4]) == 255

print("12-channel stack ok", stack12.shape)

print("stack12[0] :\n",stack12[0])
print("stack12[4] :\n",stack12[4])
print("stack12[8] :\n",stack12[8])

# Save all 12 channels as TIFF pages
pages = [
    Image.fromarray(stack12[index])
    for index in range(12)
]

pages[0].save(
    "sample12.tif",
    save_all=True,
    append_images=pages[1:]
)

print("wrote sample12.tif")


# TASK 2: Reload the TIFF and count its pages
with Image.open("sample12.tif") as img:
    page_count = 0

    while True:
        try:
            img.seek(page_count)
            page_count += 1
        except EOFError:
            break

print("Total TIFF pages:", page_count)

assert page_count == 12
print("TIFF page count verified!")
