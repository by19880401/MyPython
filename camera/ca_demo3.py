
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
            print("Cannot receive frame"); # 无法获取一帧图像时
            break;

        # 转为灰度图，处理快
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 旋转180度
        frame_rotate_180 = cv2.rotate(frame_gray, cv2.ROTATE_180); # 旋转180度

        frame_blurred = cv2.GaussianBlur(frame_rotate_180, (11, 11), 0);

        edges  = cv2.Canny(frame_blurred, 30, 150);

        contours,_ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE);

        for contour in contours:
            x,y,w,h = cv2.boundingRect(contour);
            aspect_ratio = float(2)/h
            if 0.8 < aspect_ratio <1.2:
                cv2.rectangle(frame_rotate_180,(x,y),(x+w,y+h),(0,255,0),2);

        # 显示图像窗口
        cv2.imshow("edges", frame_rotate_180);


        # 等待1毫秒，缓冲，如不添加，则无法显示图片
        key_code = cv2.waitKey(1); # 监听键盘
        # ESC的ASCII值是：27
        if key_code == ord('\x1b'):
            print("User press ESC to exit");
            break;

    cap.release(); # 释放摄像头
    cv2.destroyAllWindows(); # 关闭所有opencv窗口
    print("Camera closed");
