from PIL import Image  #导入所需的模块函数
import easygui as a

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
#循环
for i in range(1,65536):
    look=a.buttonbox(msg=Pic + "请输入你想查看的区域---   quit可退出/all查看全部",title='看看想看看的',choices=("a","b","c","d","e","all","quit")) 
    print(look)
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
        image_e =Image.open('e.JPG')
        image_e.show()
        pass
    elif Look == 'd':
        image_d =Image.open('d.JPG')
        image_d.show()
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
