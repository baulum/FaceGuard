from FaceGuard.recognition import FaceRecognition
from FaceGuard.faces import FaceManager

def main():
    # Gesicht-Manager initialisieren
    face_manager = FaceManager(faces_dir="faces")
    
    # Vorhandene Gesichter anzeigen
    print("Vorhandene Gesichter:", face_manager.list_faces())
    
    # Neues Gesicht hinzufügen
    new_name = input("Namen für neues Gesicht eingeben: ")
    if face_manager.add_face(new_name):
        print(f"{new_name} erfolgreich hinzugefügt.")
    
    # Gesicht löschen
    del_name = input("Namen für zu löschendes Gesicht eingeben: ")
    if face_manager.delete_face(del_name):
        print(f"{del_name} erfolgreich gelöscht.")
    
    # Gesichtserkennung und Login
    fr = FaceRecognition(faces_dir="faces")
    login_success, user_name = fr.login(required_confidence=85.0)
    if login_success:
        print(f"Willkommen, {user_name}!")
    else:
        print("Login fehlgeschlagen.")

if __name__ == "__main__":
    main()