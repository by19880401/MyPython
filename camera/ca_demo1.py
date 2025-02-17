import cv2

import numpy as np

class OpenDefaultCamera:
    def __init__(self):
        pass

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

        # 显示图像窗口
        # cv2.imshow("frame", frame);

        # 将图像转化为灰度
        # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('frame', gray_frame);

        # rotate_90_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE); # 旋转90度
        rotate_180_frame = cv2.rotate(frame, cv2.ROTATE_180); # 旋转180度
        # cv2.imshow("Rotate 180", rotate_90_frame);

        # 应用边缘检测
        edges = cv2.Canny(rotate_180_frame, 100, 100);
        cv2.imshow("edges", edges);

        # 按q退出
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     print("Camera closed");
        #     break;
        # 等待1毫秒，缓冲，如不添加，则无法显示图片
        key_code = cv2.waitKey(1); # 监听键盘
        # ESC的ASCII值是：27
        if key_code == ord('\x1b'):
            break;

    cap.release(); # 释放摄像头
    cv2.destroyAllWindows(); # 关闭所有opencv窗口
