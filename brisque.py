import cv2
import copy
import numpy as np
import imquality.brisque as brisque


# 0 <= th < 1
# The smaller the 'th', the noiser the image
def get_noisy_img(origin_img, th=0.7):
    img = copy.copy(origin_img)
    h, w, c = img.shape

    for k in range(c):
        rand_mat1 = np.random.rand(h, w)
        rand_mat2 = np.random.rand(h, w)

        for i, low in enumerate(rand_mat1):
            for j, val in enumerate(low):
                if val >= th:
                    img[i][j][k] *= rand_mat2[i][j]
    return img


origin_img = cv2.imread('highq.jpg')
noisy_img = get_noisy_img(origin_img)
blurred_img = cv2.GaussianBlur(origin_img, (0, 0), 5)

# cv2.imshow("noisy img", noisy_img)
# cv2.imshow("blurred img", blurred_img)
# cv2.waitKey(0)

print("BRISQUE with original:", brisque.score(origin_img))
print("BRISQUE with blurred:", brisque.score(blurred_img))
print("BRISQUE with noisy:", brisque.score(noisy_img))