c = 300000000 
m = input("Please input the value of m: ")
m = int(m)
E = m * c * c
print(E)
#最好不要使用math库中的pow函数，因为该函数返回的是一个浮点数，输出时会使用科学技术法表示
#python中也有一些不适用科学技术法的方法（如引入一些其他库）