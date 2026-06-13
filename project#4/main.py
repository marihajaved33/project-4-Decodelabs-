import cv2
import pytesseract
import os

# =====================================
# TESSERACT PATH
# =====================================

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# =====================================
# CREATE OUTPUT FOLDER
# =====================================

if not os.path.exists("output"):
    os.makedirs("output")

# =====================================
# PROCESS ALL IMAGES
# =====================================

image_folder = "images"

for filename in os.listdir(image_folder):

    if filename.lower().endswith((".jpg", ".jpeg", ".png")):

        print("\n===================================")
        print("Processing:", filename)
        print("===================================\n")

        image_path = os.path.join(image_folder, filename)

        image = cv2.imread(image_path)

        if image is None:
            print("Could not load image.")
            continue

        # =====================================
        # PREPROCESSING
        # =====================================

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        thresh = cv2.threshold(
            blur,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        # =====================================
        # OCR ON ORIGINAL IMAGE
        # =====================================

        text = pytesseract.image_to_string(image)

        print("Recognized Text:")
        print("---------------------")
        print(text)

        # =====================================
        # SAVE TEXT FILE
        # =====================================

        txt_name = os.path.splitext(filename)[0] + ".txt"

        with open(
            os.path.join("output", txt_name),
            "w",
            encoding="utf-8"
        ) as file:

            file.write(text)

        # =====================================
        # CONFIDENCE SCORES
        # =====================================

        print("\nConfidence Scores:")
        print("---------------------")

        data = pytesseract.image_to_data(
            image,
            output_type=pytesseract.Output.DICT
        )

        for i in range(len(data["text"])):

            word = data["text"][i].strip()

            if word != "":

                try:
                    confidence = float(data["conf"][i])
                except:
                    confidence = 0

                print(
                    f"Word: {word} | Confidence: {confidence}"
                )

        # =====================================
        # DRAW BOUNDING BOXES
        # =====================================

        boxed_image = image.copy()

        for i in range(len(data["text"])):

            word = data["text"][i].strip()

            if word != "":

                x = data["left"][i]
                y = data["top"][i]
                w = data["width"][i]
                h = data["height"][i]

                cv2.rectangle(
                    boxed_image,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    boxed_image,
                    word,
                    (x, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 255),
                    1
                )

        # =====================================
        # SAVE DETECTED IMAGE
        # =====================================

        output_image = os.path.join(
            "output",
            os.path.splitext(filename)[0] + "_detected.jpg"
        )

        cv2.imwrite(output_image, boxed_image)

        print("\nSaved:")
        print(output_image)

print("\n===================================")
print("ALL IMAGES PROCESSED SUCCESSFULLY")
print("===================================")