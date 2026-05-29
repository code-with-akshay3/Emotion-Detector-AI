import streamlit as st
from deepface import DeepFace
from camera import capture_photo
import cv2

st.set_page_config(page_title="Face Emotion AI", layout="centered")

st.title("📷 Face Emotion Detection AI")
st.write("Click button → capture photo → detect emotion")

if st.button("📸 Open Camera & Capture Face"):

    img_path = capture_photo()

    # ✅ SAFE CHECK (IMPORTANT FIX)
    if img_path is None:
        st.warning("⚠️ No image captured. Please try again.")
        st.stop()

    st.success("Photo Captured Successfully!")

    # Show image
    image = cv2.imread(img_path)

    if image is None:
        st.error("❌ Could not read image file.")
        st.stop()

    st.image(image, channels="BGR", caption="Captured Image")

    # Emotion Detection
    st.write("🧠 Analyzing Emotion...")

    try:
        result = DeepFace.analyze(
            img_path=img_path,
            actions=['emotion'],
            enforce_detection=False  # ✅ prevents crash if face not detected
        )

        emotion = result[0]['dominant_emotion']

        st.subheader("Detected Emotion:")
        st.success(emotion.upper())

        # UI messages
        if emotion == "happy":
            st.write("😄 Person looks Happy")
        elif emotion == "sad":
            st.write("😢 Person looks Sad")
        elif emotion == "angry":
            st.write("😡 Person looks Angry")
        else:
            st.write("😐 Neutral expression")

    except Exception as e:
        st.error(f"❌ Emotion detection failed: {str(e)}")

        