import turtle

def draw_concentric_circles(num_circles, start_radius, step):
    """
    绘制同心圆
    :param num_circles: 要绘制的圆的数量
    :param start_radius: 第一个圆的半径
    :param step: 每个后续圆的半径增加量
    """
    turtle.speed('fastest')  # 设置绘图速度为最快
    for i in range(num_circles):
        radius = start_radius + i * step
        turtle.penup()
        turtle.goto(0, -radius)
        turtle.pendown()
        turtle.circle(radius)

def main():
    turtle.setup(width=800, height=600)  # 设置窗口大小
    turtle.bgcolor("white")  # 设置背景颜色
    turtle.color("black")  # 设置画笔颜色
    turtle.title("Concentric Circles")  # 设置窗口标题

    num_circles = 10  # 同心圆的数量
    start_radius = 20  # 第一个圆的半径
    step = 20  # 每个圆的半径增加量

    draw_concentric_circles(num_circles, start_radius, step)

    turtle.done()  # 结束绘图

if __name__ == "__main__":
    main()
