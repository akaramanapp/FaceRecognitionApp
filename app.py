import face_recognition
from flask import Flask, jsonify, json
from flask import make_response
from flask import request

import os

UPLOAD_FOLDER = 'UPLOAD_FOLDER'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']

    myStr = file.stream.read()

    # load your image
    image_to_be_matched = face_recognition.load_image_file(file)

    # encoded the loaded image into a feature vector
    image_to_be_matched_encoded = face_recognition.face_encodings(
        image_to_be_matched)[0]

    # load the image
    current_image = face_recognition.load_image_file("images/kerim.jpg")
    # encode the loaded image into a feature vector
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    # math your image with the image and check if it matches
    result = face_recognition.compare_faces(
        [image_to_be_matched_encoded], current_image_encoded, tolerance=0.2)
    # check if it was a match
    if result[0] == True:
        return json.dumps(True)
    else:
        return json.dumps(False)
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    #file.save(f)


    return jsonify(3)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')