#coding=utf-8

import cv2

#frameSize 视频尺寸
VIDEO_HEIGHT = 768
VIDEO_WIDTH = 1024
def handleGaussian(img2, scale):
    kernel_size = (135, 135)
    sigma = 15.5
    #图片高斯化，作为背景图
    gImg = cv2.GaussianBlur(img2, kernel_size, sigma)

    #scale: zooming picture
    imgResize = cv2.resize(img2, (0, 0), fx=scale, fy=scale, interpolation = cv2.INTER_LINEAR)
    #高斯化图片尺寸和视频尺寸一致
    gImgResize = cv2.resize(gImg, (VIDEO_WIDTH, VIDEO_HEIGHT), interpolation = cv2.INTER_LINEAR)

    rows, cols, channels = imgResize.shape
    gRows, gCols, gChannels = gImgResize.shape

    #居中
    x_offset = (gRows - rows) / 2
    y_offset = (gCols - cols) / 2

    gImgResize[x_offset: x_offset + rows, y_offset: y_offset + cols] = imgResize

    return gImgResize

def videoWriter(imgaes):
    imgList = map(lambda x: cv2.imread(x), imgaes)
    gImgs = []
    scale = 0.1
    for img in imgList:
        for i in range(2, 7):
            gImgs.append(handleGaussian(img, scale * i))
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 3, (VIDEO_WIDTH, VIDEO_HEIGHT), True)
    for gImg in gImgs:
        video.write(gImg)

    video.release()

if __name__ == '__main__':
    try:
        videoWriter(['1.jpg', '2.jpg', '3.jpg', '4.jpg'])
    except Exception as err:
        print(err, '########')