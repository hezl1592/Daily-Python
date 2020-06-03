import cv2

if __name__ == "__main__":
    image = cv2.imread('test.jpg')
    print(image.shape)
    image_h = cv2.hconcat([image, image])
    image_h = cv2.vconcat([image_h, image_h])
    print(image_h.shape)
    # cv2.imshow("ss", image_h)

    cv2.waitKey(0)
