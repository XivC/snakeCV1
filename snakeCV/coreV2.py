'''
import cognitive_face as CF

KEY = '4aafb44ca79a4eac8b423f9bd6d018f4'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img_url = 'test2.jpg'#'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
faces = CF.face.detect(img_url)
print(faces)
'''


import cognitive_face as CF

key = '4aafb44ca79a4eac8b423f9bd6d018f4'  # Replace with a valid Subscription Key here.
CF.Key.set(key)

base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(base_url)

img_urls = [
    'temp.jpg',
    'test2.jpg' ]

faces = [CF.face.detect(img_url) for img_url in img_urls]

# Assume that each URL has at least one face, and that you're comparing the first face in each URL
# If not, adjust the indices accordingly.
similarity = CF.face.verify(faces[0][0]['faceId'], faces[1][0]['faceId'])
print (similarity)