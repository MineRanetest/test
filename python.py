# 这是注释，Python会忽略这些行

# 导入标准库中的math模块，用于数学计算
import math

# 定义一个函数，用于计算两个数的和
def add_numbers(a, b):
    return a + b

# 定义一个函数，用于判断一个数是否为偶数
def is_even(number):
    return number % 2 == 0

# 定义一个类，表示一个简单的矩形
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 定义一个方法，用于计算矩形的面积
    def area(self):
        return self.width * self.height

    # 定义一个方法，用于表示矩形的信息
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# 主程序开始
if __name__ == "__main__":
    # 定义两个变量
    num1 = 10
    num2 = 20

    # 调用函数并打印结果
    sum_result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {sum_result}")

    # 判断一个数是否为偶数，并打印结果
    if is_even(sum_result):
        print(f"{sum_result} is an even number.")
    else:
        print(f"{sum_result} is an odd number.")

    # 创建矩形对象
    rect = Rectangle(10, 5)
    # 打印矩形信息
    print(rect)
    # 打印矩形的面积
    print(f"The area of the rectangle is {rect.area()}")

    # 使用math模块计算圆的面积
    radius = 7
    circle_area = math.pi * radius ** 2
    print(f"The area of the circle with radius {radius} is {circle_area}")
