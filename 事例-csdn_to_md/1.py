import cv2
import matplotlib.pyplot as plt

# 读取图像文件
img = cv2.imread(r"C:\Users\LENOVO\Desktop\image.png")  # 替换为你的图像路径

# 将 BGR 图像转换为 RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 使用 Matplotlib 显示图像
plt.imshow(img_rgb)
plt.axis('off')  # 隐藏坐标轴
plt.show()
