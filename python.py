import matplotlib.pyplot as plt
import numpy as np

# 生成x的值，范围从-10到10，共200个点
x = np.linspace(-10, 10, 200)
# 计算对应的y值
y = x**2

# 创建图像
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="$y = x^2$", color="blue", linewidth=2)

# 添加标题和标签
plt.title("Plot of $y = x^2$", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

# 添加网格
plt.grid(True, linestyle='--', alpha=0.7)

# 添加图例
plt.legend(fontsize=12)

# 显示图像
plt.show()
