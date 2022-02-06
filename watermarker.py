import cv2

def add_watermark(img_path, watermark_text='Jules Hizon', text_color=(255,255,255), pos=(100,100), font=cv2.FONT_HERSHEY_SIMPLEX,):

    img_to_watermark = cv2.imread(img_path)
    wm_img = cv2.putText(img=img_to_watermark, text=watermark_text, org=pos, fontFace=font, fontScale=1, color=text_color, thickness=2)

    return wm_img