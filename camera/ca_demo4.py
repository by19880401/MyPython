# -*- coding: utf-8 -*-
"""完整demo：画出画面里所有物体的轮廓（已亲测，可行）"""
import cv2

class OpenDefaultCameraDemo2:
    # 初始化class，new的时候才会执行
    def __init__(self):
        print("initializing start")
        print("initializing end")
        pass

    # 打印python版本
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

        # 无法获取一帧图像时
        if not ret:
            print("Cannot receive frame");
            break;

        # 摄像头画面 旋转180度（因测试的摄像头是倒着放的，所以这里，我要把它旋转180度）
        frame_rotate_180 = cv2.rotate(frame, cv2.ROTATE_180);  # 彩色画面

        # 转为灰度图，处理快
        frame_gray = cv2.cvtColor(frame_rotate_180, cv2.COLOR_BGR2GRAY); # 变灰色画面

        # 转二进制图像
        ret,binary = cv2.threshold(frame_gray,127,255,0);

        # 寻找物体轮廓，轮廓检索模式：RETR_TREE，轮廓逼近方法：CHAIN_APPROX_NONE，返回contours（轮廓）、hierarchy（层级）
        contours,hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE);

        dst = frame_rotate_180.copy(); # TODO 这里不清楚为什么要copy一次原数据帧
        dst = cv2.drawContours(dst, contours, -1, (0,0,255), 2);# thickness的值：数字越大，线条越粗

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
