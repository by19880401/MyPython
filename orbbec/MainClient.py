# -*- coding: utf-8 -*-
from ObTypes import *
from Property import *
import Pipeline
from Error import ObException
import Version

import cv2
import numpy as np

"""调用orbbec彩色和深度相机，实现物体识别及测距离"""


# 初始化模型
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights",
                      "dnn_model/yolov4-tiny.cfg")  # 导入模型，加载模型
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1 / 255)  # 压缩图片至DNN可处理的尺寸，尺寸越大检测效果越好，但处理速度会变慢

# 将识别分类表赋值到classes
classes = []
with open("dnn_model/classes.txt", "r") as file_object:  # 只读模式读取文件
    for class_name in file_object.readlines():  # 将识别结果赋值到数组
        class_name = class_name.strip()  # 去掉头尾的空格或换行
        classes.append(class_name)  # 将class_name加入到classes里



version= Version.Version();
print(f"Orbbec SDK Version: {version.getMajor()}.{version.getMinor()}.{version.getPatch()}");

try:
    pipe = Pipeline.Pipeline(None, None)
    config = Pipeline.Config() # 读取配置文件：OrbbecSDKConfig_v1.0.xml
    profiles = pipe.getStreamProfileList(OB_PY_SENSOR_COLOR)
    videoProfile = profiles.getProfile(0)
    colorProfile = videoProfile.toConcreteStreamProfile(OB_PY_STREAM_VIDEO)
    windowsWidth = colorProfile.width()
    windowsHeight = colorProfile.height()
    config.enableStream(colorProfile)

    pipe.start(config, None)

    # 检查镜像属性是否有可写的权限
    if pipe.getDevice().isPropertySupported(OB_PY_PROP_COLOR_MIRROR_BOOL, OB_PY_PERMISSION_WRITE):
        pipe.getDevice().setBoolProperty(OB_PY_PROP_COLOR_MIRROR_BOOL, True)


    while True:
        frameSet = pipe.waitForFrames(100);
        if frameSet is None:
            continue
        else:
            colorFrame = frameSet.colorFrame()
            if colorFrame is None:
                continue
            size = colorFrame.dataSize()
            data = colorFrame.data()

            if size == 0:
                continue

            newData = data
            if colorFrame.format() == OB_PY_FORMAT_MJPG:
                newData = cv2.imdecode(newData, 1)
                if newData is not None:
                    newData = np.resize(newData, (windowsHeight, windowsWidth, 3))
            elif colorFrame.format() == OB_PY_FORMAT_RGB888:
                newData = np.resize(newData, (windowsHeight, windowsWidth, 3))
                newData = cv2.cvtColor(newData, cv2.COLOR_RGB2BGR)
            elif colorFrame.format() == OB_PY_FORMAT_YUYV:
                newData = np.resize(newData, (windowsHeight, windowsWidth, 2))
                newData = cv2.cvtColor(newData, cv2.COLOR_YUV2BGR_YUYV)
            elif colorFrame.format() == OB_PY_FORMAT_UYVY:
                newData = np.resize(newData, (windowsHeight, windowsWidth, 2))
                newData = cv2.cvtColor(newData, cv2.COLOR_YUV2BGR_UYVY)
            elif colorFrame.format() == OB_PY_FORMAT_I420:
                newData = newData.reshape((windowsHeight * 3 // 2, windowsWidth))
                newData = cv2.cvtColor(newData, cv2.COLOR_YUV2BGR_I420)
                newData = cv2.resize(newData, (windowsWidth, windowsHeight))

            # 物体检测
            (class_ids, scores, bboxes) = model.detect(newData)
            for class_id, score, bbox in zip(class_ids, scores, bboxes):  # 将多帧数据打包重组成单帧
                (x, y, w, h) = bbox  # x,y代表识别框左上角位置坐标，w宽度，h高度
                class_name = classes[class_id]
                cv2.rectangle(newData, (x, y), (x + w, y + h), (255, 0, 0), 3)  # 画面，左上角坐标，右下角坐标，RGB颜色，厚度
                cv2.putText(newData, class_name +", haha12", (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0),
                            3)  # 画面，文本内容，位置，字体，字体大小，RGB颜色，厚度
                print(f"class id: {class_id}, class name: {class_name}")  # 分类结果
                print("score", score)  # 准确度
                print("bbox", bbox)  # 识别框的位置信息

            if newData is not None:
                cv2.imshow("Model Detect", newData)


            key = cv2.waitKey(1)
            if key ==27:
                cv2.destroyAllWindows();
                print("User press ESC to exit");
                break

    pipe.stop()




except ObException as e:
    print(e)