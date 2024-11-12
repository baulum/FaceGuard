from FaceGuard.recognition import FaceRecognition

fr = FaceRecognition(faces_dir="faces")
login_success, user_name = fr.login(required_confidence=85.0)
if login_success:
    print(f"Willkommen, {user_name}!")
else:
    print("Login fehlgeschlagen.")