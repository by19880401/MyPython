import cv2 as cv

def main():
    orbbec_cap = cv.VideoCapture(0, cv.CAP_OBSENSOR);

    if not orbbec_cap.isOpened():
        exit("Could not open camera");

    while True:
        if orbbec_cap.grab():
            # RGB data
            ret_bgr, bgr_image = orbbec_cap.retrieve(None, cv.CAP_OBSENSOR_BGR_IMAGE);
            if ret_bgr:
                # color_depth_map = cv.applyColorMap(cv.convertScaleAbs(depth_map, alpha=0.0255), cv.COLORMAP_JET);
                cv.imshow("RGB", bgr_image);

            # Depth data
            ret_depth, depth_map = orbbec_cap.retrieve(None, cv.CAP_OBSENSOR_DEPTH_MAP);
            if ret_depth:
                color_depth_map = cv.normalize(depth_map, None, 0, 255, cv.NORM_MINMAX, cv.CV_8UC1)
                color_depth_map = cv.applyColorMap(color_depth_map, cv.COLORMAP_JET)
                cv.imshow("Depth Map", color_depth_map);
        else:
            print("Could not grap data from camera");

        if cv.pollKey()>= 0: # 任意键退出
            print("exit now")
            break;

    orbbec_cap.release();

if __name__ == "__main__":
    main();