import cv2
import os

positives_folder = "positives"
annotations_file = "annotations/pos.txt"

os.makedirs("annotations", exist_ok=True)

f = open(annotations_file, "w")

for filename in os.listdir(positives_folder):
    if not filename.lower().endswith((".jpg", ".png")):
        continue

    path = os.path.join(positives_folder, filename)
    img = cv2.imread(path)
    clone = img.copy()
    rect = []  # burada list olarak tanımla

    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            rect.clear()
            rect.append((x, y))
        elif event == cv2.EVENT_LBUTTONUP:
            rect.append((x, y))
            cv2.rectangle(clone, rect[0], rect[1], (0, 255, 0), 2)
            cv2.imshow("Image", clone)
            x0, y0 = rect[0]
            x1, y1 = rect[1]
            width = x1 - x0
            height = y1 - y0
            f.write(f"{filename} 1 {x0} {y0} {width} {height}\n")

    cv2.imshow("Image", clone)
    cv2.setMouseCallback("Image", click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

f.close()
print("Annotation tamamlandı!")
