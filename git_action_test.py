class calculate:

    #此处只在类被定义时才执行(一次)

    def __init__(self,a,b):#此处在类实例化时执行(每次)
        print("计算类实例化")
        self.a = a
        self.b = b
    
    def Add(self):
        return self.a + self.b
    
    def Sub(self):
        return self.a - self.b
    
    def Mul(self):
        return self.a * self.b
    
    def Div(self):
        return self.a / self.b


if __name__ == "__main__":
    calculate_test = calculate(10, 5)

    print(f"加法结果为：{calculate_test.Add()}")
    print(f"减法结果为：{calculate_test.Sub()}")
    print(f"乘法结果为：{calculate_test.Mul()}")
    print(f"除法结果为：{calculate_test.Div()}")
