# -*- coding: utf-8 -*-
"""完整demo：画出画面里所有物体的轮廓（已亲测，可行）"""
import cv2

class OpenDefaultCameraDemo2:
    def __init__(self):
        print("initializing start")
        print("initializing end")
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
            print("Cannot receive frame"); # 无法获取一帧图像时
            break;

        # 旋转180度
        frame_rotate_180 = cv2.rotate(frame, cv2.ROTATE_180);  # 旋转180度

        # 转为灰度图，处理快
        frame_gray = cv2.cvtColor(frame_rotate_180, cv2.COLOR_BGR2GRAY);


        # 转二进制
        ret,binary = cv2.threshold(frame_gray,127,255,0);

        contours,hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE);

        dst = cv2.drawContours(frame_rotate_180, contours, -1, (0,0,255), 2);# thickness的值：数字越大，线条越粗

        # 显示图像窗口
        cv2.imshow("edges", dst);


        # 等待1毫秒，缓冲，如不添加，则无法显示图片
        key_code = cv2.waitKey(1); # 监听键盘
        # ESC的ASCII值是：27
        if key_code == ord('\x1b'):
            print("User press ESC to exit");
            break;

    cap.release(); # 释放摄像头
    cv2.destroyAllWindows(); # 关闭所有opencv窗口
    print("Camera closed");


if __name__=="__main__":
    demo = OpenDefaultCameraDemo2();
