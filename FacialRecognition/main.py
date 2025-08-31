
import enroll,recognition,cv2
print(cv2.__version__)
recognition.load_facial_encodings_and_names_from_memory()
#spreadsheet.mark_all_absent()
recognition.run_recognition()
# name=input("Name:")
#enroll.enroll_via_camera(name)
#enroll.encoding_of_enrolled_person("Kayaan","C:\Users\VBPS_ATL\Desktop\Advanced Facial Recognition By Aditya\source\known face photos\Kayaan.jpg")


