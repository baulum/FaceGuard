from FaceGuard.faces import FaceManager

face_manager = FaceManager(faces_dir="faces")

# Neues Gesicht hinzufügen
name = input("Namen für das neue Gesicht eingeben: ")
face_manager.add_face(name)

# Gesicht löschen
name = input("Namen für zu löschendes Gesicht eingeben: ")
face_manager.delete_face(name)

# Liste der vorhandenen Gesichter anzeigen
print("Vorhandene Gesichter:", face_manager.list_faces())