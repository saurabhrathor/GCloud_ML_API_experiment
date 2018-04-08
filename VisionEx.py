import io
from google.cloud import vision
from google.cloud.vision import types

vision_client = vision.ImageAnnotatorClient()
file_name = '220px-Sachin_Tendulkar_at_MRF_Promotion_Event.jpg'

with io.open(file_name,'rb') as image_file:
        content = image_file.read()
image = types.Image(content=content)

'''
### if pic to be uploaded from any URL
image = types.Image()
image.source.image_uri = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Guido-portrait-2014.jpg/290px-Guido-portrait-2014.jpg'
'''

response = vision_client.label_detection(image=image)
labels = response.label_annotations


for label in labels:
        print(label.description,label.score)
