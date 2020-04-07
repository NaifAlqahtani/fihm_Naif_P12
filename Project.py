# Fihm project by Naif Alqahtani P12
# My favorite football team that I support is Barcelona so I chose them
# I could not get opencv to work at all on my PC so I went with the next best alternative; face_recognition
# there are 11 player faces in the picture but I only taught the algorithm about 10 faces only.
# I will explain the code via comments and through a video that I will upload privately on my channel
#please copy this link to youtube to see the video:    https://youtu.be/SSrc3ysLCrc
import face_recognition #face recognition library
from PIL import Image, ImageDraw



#----------------------------------------------------------
#teaching the algorithm about the TEN (10) player faces by giving them a sample
frenkie = face_recognition.load_image_file('frenkie.jpg') #loads the image file
frenkie_face = face_recognition.face_encodings(frenkie)[0] #saves the face features to "frenkie_face"

pique = face_recognition.load_image_file('pique.jpg')
pique_face = face_recognition.face_encodings(pique)[0]


rakitic = face_recognition.load_image_file('rakitic.jpg')
rakitic_face = face_recognition.face_encodings(rakitic)[0]

stegen = face_recognition.load_image_file('Ter stegen.jpg')
stegen_face = face_recognition.face_encodings(stegen)[0]

messi = face_recognition.load_image_file('messi.jpg')
messi_face = face_recognition.face_encodings(messi)[0]

alba = face_recognition.load_image_file('alba.jpg')
alba_face = face_recognition.face_encodings(alba)[0]

griezmann = face_recognition.load_image_file('griezmann.jpg')
griezmann_face = face_recognition.face_encodings(griezmann)[0]

lenglet = face_recognition.load_image_file('lenglet.jpg')
lenglet_face = face_recognition.face_encodings(lenglet)[0]

busquets = face_recognition.load_image_file('busquets.jpg')
busquets_face = face_recognition.face_encodings(busquets)[0]

semedo = face_recognition.load_image_file('semedo.jpg')
semedo_face = face_recognition.face_encodings(semedo)[0]
#-------------------------------------------------------------
#making an array of the faces that the algorithm as been taught
known_faces = [
    frenkie_face,
    rakitic_face,
    pique_face,
    stegen_face,
    messi_face,
    alba_face,
    griezmann_face,
    lenglet_face,
    busquets_face,
    semedo_face
]
#Giving a name to those faces so that it can be displayed later
kown_names = [
    "De jong",
    "Rakitic",
    "Pique",
    "Stegen",
    "Messi",
    "Alba",
    "Griezmann",
    "lenglet",
    "Busquets",
    "Semedo"
]
#-------------------------------------------------------------------
target_image = face_recognition.load_image_file('team.jpg')#loads the entire team image
face_locations = face_recognition.face_locations(target_image)#find faces in target image
face_encodings = face_recognition.face_encodings(target_image, face_locations) #makes face features for faces

#-------------------------------------------------------------------
pil_image = Image.fromarray(target_image) #convert to pil format to enable drawing
draw = ImageDraw.Draw(pil_image) #creat image layer
#-------------------------------------------------------------------

#MAIN LOOP-----------------------------------------------------------
#loop through faces in target image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_faces, face_encoding) #save every face that has been found in image

    name = "Unknown" #set the default name of faces to unknown. this will be used for demonstration

    if True in matches: #if face has been found AND it matches one of the known faces
        first_match_index = matches.index(True) 
        name = kown_names[first_match_index] #change face name from "unkown" to player name from previously mention array

    #---------------------------------------------------------------
    # start drawing boxes and lables
    draw.rectangle(((left-3, top-5),(right+5, bottom+5)), outline=(0,255,0)) #draws green face box
    text_w, text_h = draw.textsize(name) #sets text demensions
    draw.rectangle(((left-3, bottom + 2), (right+5, bottom + text_h)), fill=(0,255,0), outline=(0,255,0)) #draws green filled text box
    draw.text((left, bottom - text_h + 12), name, fill=(0,0,0,255)) #draws text
#END MAIN LOOP
#------------------------------------------------------------------------------------


del draw #it is adviced to delete draw instance once done
pil_image.show() #show final image



