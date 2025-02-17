
import cv2
import numpy as np

class OpenDefaultCameraDemo2:
    def __init__(self):
        pass

    print(f"python cv version: {cv2.__version__}")

    # 打开默认的摄像头（通常是第一个摄像头，下标为0，如果有多个摄像头，可修改为1，2等）
    cap = cv2.VideoCapture(0);

    # 检查摄像头是否成功打开
    if not cap.isOpened():
        raise IOError("Cannot open camera")
        exit()

    print("Camera opened");

    while True:
        # 捕获一帧图像
        ret, frame = cap.read();

        if not ret:
            print("Cannot receive frame");
            break;

        # cv2.imshow("frame", frame);
        rotate_180_frame = cv2.rotate(frame, cv2.ROTATE_180); # 旋转180度
        # 应用边缘检测
        edges = cv2.Canny(rotate_180_frame, 100, 200);
        # 显示图像窗口
        cv2.imshow("edges", edges);


        # 等待1毫秒，缓冲，如不添加，则无法显示图片
        key_code = cv2.waitKey(1); # 监听键盘
        # ESC的ASCII值是：27
        if key_code == ord('\x1b'):
            break;

    cap.release(); # 释放摄像头
    cv2.destroyAllWindows(); # 关闭所有opencv窗口
