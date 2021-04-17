from PIL import Image  #导入所需的模块函数
import cv2

Pic = """

|                             |                                   |            | 
|                             |                                   |            |
|                             |                                   |            | 
|                             |                       B           |      D     |
|                             |                                   |            |
|                             | __________________________________|____________|
|                 A           |                                   |            |
|                             |                                   |            |
|                             |                                   |            |
|                             |                       C           |      E     |
|                             |                                   |            |
|                             |                                   |            |


"""
#字符画（如有地图等可替换）
print(Pic)
#循环
for i in range(1,65536):
    look=input("请输入你想查看的区域---   quit可退出/all查看全部") #将输入存入变量
    Look = look.lower() #输入一律改为小写
    if Look == 'a' :  #判断语句a
        image_a =Image.open('a.JPG') #image方法
        image_a.show() #打开图片
        pass #空语句后续补充使用
    elif Look == 'b' :
        image_b =Image.open('b.JPG') #判断语句b
        image_b.show()
        pass
    elif Look == 'c' :
        image_c = Image.open('c.JPG') #判断语句c
        image_c.show()
        pass
    elif Look == 'e':
        image_e =Image,open ('d.JPG')
        image_e.show()
        pass
    elif Look == 'f ':
        image_f =Image.open('f.JPG')
        image_f.show()
        pass
    elif Look == 'all': 
        photos = ['a','b','c','d','e']  #设置列表变量
        for p in photos :
            form = p + '.JPG' #将列表中所有元素加上.jpg的格式
            image_all =Image.open(form)
            image_all.show()
        pass
    elif Look == "quit": #判断语句--退出循环
        break
    else: #检查其他符号识别并提示
        print('请检查输入是否有误')

print('感谢你的使用')
#  暂时注释化使用opencv
