from ObTypes import *
from Property import *
import Pipeline
import StreamProfile
import Device
from Error import ObException
import cv2
import numpy as np

"""调用orbbec彩色相机和深度相机，实现物体识别和物体测距"""

# Parameters
q = 113
ESC = 27
alpha = 0.0  # 深度图映射到彩色图上的透明度，一般不要高于0.7


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

# Initialize
pipe = Pipeline.Pipeline(None, None)  # Create a Pipeline
config = Pipeline.Config()  # Configure the Pipeline


# Define a function to configure and enable a stream
def enable_stream(sensor_type, align_mode):
    profiles = pipe.getStreamProfileList(sensor_type)
    profile = profiles.getProfile(0).toConcreteStreamProfile(OB_PY_STREAM_VIDEO)
    config.enableStream(profile)
    print(f"Stream width: {profile.width()}")
    print(f"Stream height: {profile.height()}")
    config.setAlignMode(align_mode)
    return profile


# Enable and align color and depth streams
color_profile = enable_stream(OB_PY_SENSOR_COLOR, OB_PY_ALIGN_D2C_SW_MODE)
depth_profile = enable_stream(OB_PY_SENSOR_DEPTH, OB_PY_ALIGN_D2C_SW_MODE)

pipe.start(config, None)


# Define the function to process the frames
def process_frames():
    frameSet = pipe.waitForFrames(100)
    colorData = None
    outputDepthImage = None
    newData = None

    if frameSet:
        colorFrame = frameSet.colorFrame()
        depthFrame = frameSet.depthFrame()
        if colorFrame and depthFrame:
            colorData = colorFrame.data()
            depthData = depthFrame.data()

            if colorData is not None and depthData is not None:
                if colorFrame.format() == OB_PY_FORMAT_MJPG:
                    colorData = cv2.imdecode(colorData, 1)
                    if colorData is not None:
                        colorData = np.resize(colorData, (colorFrame.height(), colorFrame.width(), 3))

                depthData = np.resize(depthData, (depthFrame.height(), depthFrame.width(), 2))
                newDepthData = (depthData[:, :, 0] + depthData[:, :, 1] * 256 * depthFrame.getValueScale()).astype(
                    'uint16')
                normalized_image = (newDepthData / 32).astype('uint8')
                outputDepthImage = cv2.cvtColor(normalized_image, cv2.COLOR_GRAY2RGB)

                # Resize depth image to match color image if necessary
                if colorFrame.height() != depthFrame.height():
                    outputDepthImage = cv2.resize(outputDepthImage, (colorFrame.width(), colorFrame.height()))

                # Combine depth and color images
                newData = cv2.addWeighted(colorData, (1 - alpha), outputDepthImage, alpha, 0)
                # cv2.imshow("SyncAlignViewer", newData)

                # 物体检测
                (class_ids, scores, bboxes) = model.detect(newData)
                for class_id, score, bbox in zip(class_ids, scores, bboxes):  # 将多帧数据打包重组成单帧
                    (x, y, w, h) = bbox  # x,y代表识别框左上角位置坐标，w宽度，h高度
                    class_name = classes[class_id]
                    cv2.rectangle(newData, (x, y), (x + w, y + h), (255, 0, 0), 3)  # 画面，左上角坐标，右下角坐标，RGB颜色，厚度
                    cv2.putText(newData, class_name + ", "+str(newDepthData[int(y+h/2),int(x+w/2)])+"mm", (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0),
                                3)  # 画面，文本内容，位置，字体，字体大小，RGB颜色，厚度
                    print(f"class id: {class_id}, class name: {class_name}")  # 分类结果
                    print("score", score)  # 准确度
                    print("bbox", bbox)  # 识别框的位置信息

                # 在窗口显示处理后的图像流
                if newData is not None:
                    cv2.imshow("Model Detect", newData)



    # Check user input to break the loop
    if cv2.waitKey(1) in [ESC, q]:
        cv2.destroyAllWindows()
        return False, colorData, outputDepthImage, newData

    return True, colorData, outputDepthImage, newData


# Main loop
while True:
    keep_going, colorData, outputDepthImage, newData = process_frames()
    if not keep_going:
        break

pipe.stop()
