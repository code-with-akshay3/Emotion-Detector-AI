import cv2

def capture_photo():
    cam = cv2.VideoCapture(0)
    img_name = None  # ✅ default value

    while True:
        ret, frame = cam.read()

        if not ret:
            print("Camera not working properly")
            break

        cv2.imshow("Press SPACE to Capture | ESC to Exit", frame)

        key = cv2.waitKey(1)

        # SPACE = capture
        if key == 32:
            img_name = "captured_face.jpg"
            cv2.imwrite(img_name, frame)
            print("Photo captured!")
            break

        # ESC = exit without capture
        elif key == 27:
            print("Exit without capturing photo")
            break

    cam.release()
    cv2.destroyAllWindows()

    # ✅ safe return
    return img_name