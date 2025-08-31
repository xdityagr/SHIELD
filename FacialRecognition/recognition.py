import face_recognition,cv2,os,pickle
import numpy as np
import pyttsx3
import json
from sckt_send import send_until_recv


known_face_encodings=[]
known_face_names=[]

video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)


photo_folder = "known face photos\\"
facial_encodings_folder = "known face encodings\\"

def load_facial_encodings_and_names_from_memory():
    for filename in os.listdir(facial_encodings_folder):
        known_face_names.append(filename[:-4])
        with open (facial_encodings_folder+filename, 'rb') as fp:
            known_face_encodings.append(pickle.load(fp)[0])

            
def run_recognition():
     face_locations = []
     face_encodings = []
     face_names = []
     process_this_frame = False

     while True:
    # Grab a single frame of video
          ret, frame = video_capture.read()
     # Resize frame of video to 1/4 size for faster face recognition processing
          small_frame = cv2.resize(frame, dsize=(128,128))     # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
          
          rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

     
          process_this_frame = not process_this_frame
          if process_this_frame:
          # Find all the faces and face encodings in the current frame of video
               face_locations = face_recognition.face_locations(rgb_small_frame)
               face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
               face_names = []
               for face_encoding in face_encodings:
               # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"


                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                         name = known_face_names[best_match_index]

                    face_names.append(name)
                    print(face_names)

               if len(face_names) != 0:
                    if face_names[0] != "Unknown":
                         
                         if face_names[0] == "Aadya":
                              # send_until_recv("0")
                              pass
                         elif face_names[0] == "Aditya":
                              # send_until_recv("1")
                              pass
                         else:
                              pass
                              # send_until_recv("")    
                         
                         for (top, right, bottom, left), name in zip(face_locations, face_names):
                         # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                              top *= 4
                              right *= 4
                              bottom *= 4
                              left *= 4

                    # # Draw a box around the face
                              # cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    # # Draw a label with a name below the face
                              cv2.rectangle(frame, (left, bottom), (right, bottom), (0, 255, 0), cv2.FILLED)
                              font = cv2.FONT_HERSHEY_DUPLEX
                              cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

               cv2.imshow('Video', frame)    
               flag=-1
                    
               
               if cv2.waitKey(1) & 0xFF==ord('q') or flag==0:
                    break
     video_capture.release()

     cv2.destroyAllWindows()
