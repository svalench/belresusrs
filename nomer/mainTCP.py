import socket
import time
import os
import sys
import matplotlib.image as mpimg
import multiprocessing as mp
from termcolor import cprint
import cv2

# ----------------------------------------------------------------------------------------------------------------------
# change this property
NOMEROFF_NET_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.getcwd())
MASK_RCNN_DIR = os.path.join(NOMEROFF_NET_DIR, 'model')
MASK_RCNN_LOG_DIR = os.path.join(NOMEROFF_NET_DIR, 'logs')
sys.path.append(NOMEROFF_NET_DIR)
print(MASK_RCNN_DIR, MASK_RCNN_LOG_DIR)
# ----------------------------------------------------------------------------------------------------------------------
# Import license plate recognition tools.
import sys
sys.path.insert(0, '/home/mvlab/belresusrs/nomer')
from NomeroffNet import filters, RectDetector, TextDetector, OptionsDetector, Detector, textPostprocessing

def loadModel():
    global nnet, textDetector, rectDetector, optionsDetector
    try:
        # Initialize npdetector with default configuration file.
        nnet = Detector(MASK_RCNN_DIR, MASK_RCNN_LOG_DIR)
        nnet.loadModel("latest")

        rectDetector = RectDetector()

        optionsDetector = OptionsDetector()
        optionsDetector.load("latest")

        # Initialize text detector.
        textDetector = TextDetector.get_static_module("eu")()
        textDetector.load("latest")

        return True
    except:
        return False

def detect(path_to_img):
    print("START RECOGNIZING")

    startTime = time.time()
    # img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ex2.jpeg')
    # read image in RGB format
    # p.s. opencv read in BGR format
    # img = mpimg.imread(img_path)
    # DETECT
    img = mpimg.imread(path_to_img)

    # ROI
    # img = img[720:, 400:-400, :]
    # img = cv2.resize(img, (720, 400))
    #
    NP = nnet.detect([img])
    # Generate image mask.
    cv_img_masks = filters.cv_img_mask(NP)

    # Detect points.
    arrPoints = rectDetector.detect(cv_img_masks)
    zones = rectDetector.get_cv_zonesBGR(img, arrPoints)

    # find standart
    regionIds, stateIds, countLines = optionsDetector.predict(zones)
    regionNames = optionsDetector.getRegionLabels(regionIds)

    # find text with postprocessing by standart
    textArr = textDetector.predict(zones)
    textArr = textPostprocessing(textArr, regionNames)
    cprint(textArr, 'blue', attrs=['reverse'])
    print(time.time() - startTime)
    return textArr

def serverTCP(port=6000, host='127.0.0.1'):
    ''' Сервер, ожидает входное соединение для получения данных и отсылает ответ после '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
    try:
        s.bind((host, port))
        s.listen()
        cprint('wait connect host: %s, port: %s' % (host, port), 'yellow')

        while True:
            conn, addr = s.accept()
            while True:
                # ts = time.time()
                data = conn.recv(512)
                if len(data)>5:
                    number = detect(data.decode())
                    if len(number)>0:
                        conn.sendall(str.encode(number[0]))
                    else:
                        conn.sendall(b'false')
                if not data:
                    break
            time.sleep(2)
    except:
        s.close()
    finally:
        cprint('CLOSE CONNECTION', 'red', attrs=['reverse'])
        s.close()
        time.sleep(2)
        serverTCP(port=6000, host='127.0.0.1')


def clientTCP(path_to_image, port=6000, host='127.0.0.1'):
    data = str.encode(path_to_image)
    # send data
    s = socket.create_connection((host, port), timeout=60)
    s.sendall(data)
    # recive data
    number = s.recv(512)
    s.close()
    return number


if __name__ == '__main__':
    try:
        print(loadModel())
    # im = mpimg.imread('cam6.jpg')
    # t1 = time.time()
        print(detect('maz002.jpg'))
    # print(time.time() - t1)
    #     serverTCP()
    finally:
        cprint('KILL ALL PROCESS PYTHON3', 'red', attrs=['reverse'])
    #     os.system('killall -s 9 python3')

    # img = mpimg.imread('maz01.jpg')
    # img = img[720:, 400:-400, :]
    # img = cv2.resize(img, (720, 400))
    #
    # cv2.imshow('123', img)
    # cv2.waitKey()




