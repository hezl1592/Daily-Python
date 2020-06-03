import cv2
import numpy as np

if __name__ == "__main__":
    heat_list = [[i for j in range(256)] for i in range(256)]
    heat_mat = np.uint8(heat_list)

    # 热力图，https://blog.csdn.net/u013381011/article/details/78341861
    heat_color = cv2.applyColorMap(heat_mat, cv2.COLORMAP_WINTER)
    # print(heat_mat.shape)

    # 三通道
    img = cv2.cvtColor(heat_mat, cv2.COLOR_GRAY2BGR)

    # 拼接，确保通道数
    show_image = cv2.hconcat([img, heat_color])
    # cv2.imshow("heat", heat_mat)
    # cv2.imshow("color", heat_color)
    cv2.imshow("show", show_image)
    cv2.waitKey(0)
