from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import json
# from .models import RecognizeHistory
# import cv2
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
tf.get_logger().setLevel('ERROR')
from PIL import Image
import uuid

def load_file(path):
    file = open(path, 'r')
    content = file.read()
    file.close()
    return content

model = load_model('leafrecog/model.h5')
class_file_path = 'leafrecog/class_list.txt'
content = load_file(class_file_path)

def load_and_preprocess_image(pathToImage):
    if pathToImage.split('.')[-1] != 'png':
        image = Image.open(pathToImage)
        image = np.array(image).reshape((image.size[0], image.size[1], 3))
    else:
        image = tf.io.read_file(pathToImage)
    image = tf.image.decode_png(image, channels=3)
    image = tf.image.resize(image, (300, 300))
    return image

def load_image(image):
    image = image.astype('float32')
    image = tf.image.decode_png(image, channels=3)
    image = tf.image.resize(image, (300, 300))
    return image

# Create your views here.
def recognizeLeaf(request):
    # print(request.POST)
    print(f' Request.FILES: {request.FILES["imagerecog"]}')
    response = {}

    # if (request.method == 'POST' and request.FILES.get('imagerecog') is not None):
    #   random_uuid = str(uuid.uuid1()).replace('-', '_')
    #   image = request.FILES.get('imagerecog')
    #   recognize_history = RecognizeHistory.objects.create(recognize_uuid = random_uuid, recognize_image = image)
    #   recognize_history.save()
    #   return
    # else:
    #   return render(request, 'error.html')

    if request.method == 'POST':
        print('Got the recognize route.')
        data = request.FILES["imagerecog"]
        random_image_id = str(uuid.uuid1()).replace('-', '_')
        path = default_storage.save(f'images/{random_image_id}.png', ContentFile(data.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        print(f'Temp file: {tmp_file}')

        # Recognize part
        try:
            # Current error part
            # image_id = str(uuid.uuid1()).replace('-', '_')
            # image_path = './' + image_id + '.png'
            # cv2.imwrite(image_path, image)
            # End of current error part

            # image = [load_and_preprocess_image(image_path)]
            image = [load_and_preprocess_image(tmp_file)]
            # image = [load_image(image)]
            DS_test = tf.data.Dataset.from_tensor_slices(image)
            DS_batch_test = DS_test.batch(batch_size=1, drop_remainder=False)
            # model = load_model('leafrecog/model.h5')
            result = model.predict(DS_batch_test, batch_size=1, verbose=2, max_queue_size=1)[0]
            result = np.array(result)
            print(f'Result: {result}')
            # class_file_path = 'leafrecog/class_list.txt'
            # content = load_file(class_file_path)
            class_list = content.split(' ')
            predicted_class = class_list[np.argmax(result)]
            print(f'Predicted: {predicted_class}')
            # Return result
            response['id'] = random_image_id
            response['name'] = predicted_class
            response['accuracy'] = str(round(result[np.argmax(result)] * 100, 2))
            print(f'Response: {response}')

        except Exception as e:
            print(f'Error: {e}')
            response['error'] = e.__str__()
            print(f'Response: {response}')
            pass

        return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        return render(request, 'error.html')


def getRecogLeaf(request):
    return render(request, 'recogLeafForm.html')
