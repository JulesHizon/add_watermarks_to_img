import cv2

def transparent_overlay(src, overlay, pos=(0, 0), scale=1):

    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image

    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src


def add_watermark(LogoImage,MainImage,opacity,pos=(10,100),):
    opacity = opacity / 100

    OriImg = cv2.imread(MainImage, -1)
    waterImg = cv2.imread(LogoImage, -1)

    tempImg = OriImg.copy()

    overlay = transparent_overlay(tempImg, waterImg, pos)
    output = OriImg.copy()

    watermarked_img = cv2.addWeighted(overlay, opacity, output, 1 - opacity, 0, output)

    return watermarked_img

