#install version 2.8 of tensorflow
#pip install tensorflow==2.8 tensorflow==2.8 opencv-python matplotlib protobuf==3.19.1
import tensorflow as tf
import numpy as np
import cv2
from tensorflow.python.keras.models import load_model
import base64


#load the model
model = load_model("capstone-backend/ai-model/imageclassifier.h5")

#function that loads the model and calculates the weight from the model
#img is an encoded base64 string
#returns a value between 0 and 1
#In current model, less than 0.5 means happy, greater than 0.5 means sad
def returnImageWeight(img):
    if (img is None):
        raise ValueError("No or empty image was passed")

    image = cv2.imdecode(np.frombuffer(base64.b64decode(img),dtype=np.uint8),cv2.IMREAD_COLOR)
    resize = tf.image.resize(image,(256,256))
    weightArray = model.predict(np.expand_dims(resize/255,0))
    weight=weightArray[0][0]
    return weight

#img = cv2.imread("capstone-backend/ai-model/testImages/sadimage3.jpg")
""""
TEST IMAGE
img = "iVBORw0KGgoAAAANSUhEUgAAAdUAAAAICAYAAACvbmWyAAAACXBIWXMAAA7EAAAOxAGVKw4bAAACjElEQVR4nO3Z11JUQRSF4fM65izmHDALDMmcYEgDQxbJSJYsGXPChDmgPhxWqVU6ylpH9q52To998T1AX/3Va3tTn7PnFuyLZSRv/GHSmCyZT9iEKbPY+Gym3Eczxj5IZVCj780YeZcuMvxW4U0Ius685oaYV2nQ4Eu5gRep2AzWP5MC9T338QzrZZ4ep3qeYNceH4O6memjVNcjrPPhEewB13H/MNR+D2u7ewhqvcNdvX0Qu4W13DwANd/gmqaSY3guKC4o8QqKNCZBDAqNiQuKb1BYTGwLCotJogflV42TWMPEfqp+HKsb2wfVju7FRria4T3YEFY9uDuGJw2KKiqBCwqPivuhKKMSsKCooiINiiIqLCiaqIiDoogKC4omKtKgaKLCgqKJCguKqajQoCwwKjEGdkFV/Vxl306oohcr79kBlXVvp0q7sGjnNqik4yfPBcVNXrYGhcbEsqCwmNgWFBYTTVBYTIwFhcTEBeXPoPyuuH0rFWnbAhW1YoUtm6mC5k1QfhOW17gRCjdsoHLrv/NcUFxQ/segsJjYFhQaE8uCwmJiKigsJrYFhcXkXwRlXnVJUE4tdvHKeq4Gu3B5HXS+ei11roqoXAOdrVj9jWdjUNzkFcwfipu8/IOiiYo0KJqosKBooiINiiYqLCiaqEiDoooKCYomKjQofxmV+Zwpx06X+ShdBZ2KYiejK6ETJVx28QosgmVFls95LijBDkpcJq8EuqGYCgqLiW1BYTGxLSgsJqqgkJgYCwqJSVCDAhVxmYXLRDIKuHQmHwvlLRXzXFASNyjxuKGYCko8biimgsJiYltQWExsCwqNiWVBoTExGJRQGEsLL8FysVQ/OYuhFKlLfhZBXwHtjJHMz1/pjwAAAABJRU5ErkJggg=="
if(img is None):
    print("Failed to load image")
else:
    #encoded = base64.b64encode(img)
    #.decode('utf-8')
    print(returnImageWeight(img))

"""
#decode to send to AI component




