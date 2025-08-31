""" 
SHIELD Facial Recognition Module - Main Source 
Developed by Aditya Gaur
Github : @xdityagr 
Email  : adityagaur.home@gmail.com 

"""
import enroll,recognition,cv2
print(cv2.__version__)
recognition.load_facial_encodings_and_names_from_memory()
recognition.run_recognition()
# name=input("Name:")
#enroll.enroll_via_camera(name)
#enroll.encoding_of_enrolled_person("Name","Path")




