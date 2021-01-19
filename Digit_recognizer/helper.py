import numpy as np
import matplotlib.pyplot as plt
import cv2

def display_example(images, labels):
    a = int(input("Enter any number :"))
    plt.figure()
    plt.xticks([])
    plt.yticks([])
    plt.imshow(images[a], cmap = 'gray')
    plt.show()
    
    print(labels[a])
    

def normalize_images(images):
    max = float(images.max())
    min = float(images.min())
    images = (images - min) / (max - min)
    
    return images


def test_image(model):
    import canvas
    img = canvas.returnfn()
    imgnp = img.reshape(1,28,28,1)
    #print(img.shape)
    plt.figure()
    plt.xticks([])
    plt.yticks([])
    plt.title('Test Image')
    plt.imshow(img, cmap='gray')
    pred = np.argmax(model.predict(imgnp))
    print(f"Prediction : {pred}")
    
    

