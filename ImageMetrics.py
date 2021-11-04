from skimage.metrics import structural_similarity, mean_squared_error, peak_signal_noise_ratio
import cv2 as cv

img1 = cv.imread("assets/metricsTest/h304-m1.png")
img2 = cv.imread("assets/metricsTest/h304-m2.png")

ssim = structural_similarity(img1, img2, multichannel=True, gaussian_weights=True,
                             sigma=1.5, use_sample_covariance=False, data_range=255)
print("ssim", ssim)

psnr = peak_signal_noise_ratio(img1, img2)
print("psnr", psnr)

mse = mean_squared_error(img1, img2)
print("mse", mse)
