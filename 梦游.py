from PIL import Image  #导入所需的模块
i = 1 #循环变量i
Pic = """

|                             |                                               | 
|                             |                                               |
|                             |                                               | 
|                             |                       B                       |
|                             |                                               |
|                             | _______________________________________________
|                 A           |                                               |
|                             |                                               |
|                             |                                               |
|                             |                       C                       |
|                             |                                               |
|                             |                                               |


"""
#字符画（如有地图等可替换）
print(Pic)
#循环
for i in range(1,65536):
    look=input("请输入你想查看的区域---   quit可退出") #将输入存入变量
    Look = look.lower() #输入一律改为小写
    if Look == 'a' :  #判断语句a
        imagea =Image.open('./a.JPG') #image方法
        imagea.show() #打开图片
        pass #空语句后续补充使用
    elif Look == 'b' :
        imageb =Image.open('./b.JPG') #判断语句b
        imageb.show()
        pass
    elif Look == 'c' :
        imagec = Image.open('./c.JPG') #判断语句c
        imagec.show()
        pass
    elif Look == "quit": #判断语句--退出循环
        break
    else: #检查其他符号识别并提示
        print('请检查输入是否有误')

print('感谢你的使用')
    