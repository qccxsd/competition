import easygui as a 
from PIL import Image

for i in range(1,65536):
    Area=a.buttonbox(msg="请点击您想查看的区域",image="微信图片_20210417192908.jpg",title="学校图",choices=("学生公寓","学生食堂和超市","环校路","校园A岗","荷花池","梧桐景观造","文化广场","篮球场","实验楼","行政楼","珠海楼","深圳楼","中山楼","足球场","阶梯教室","四号楼","校园B岗","教师值班室","门厅转盘花台","知识阶梯","退出"))
    print(Area)
    if Area == "学生公寓":
        image_studentInpartment = Image.open()
        image_studentInpartment.show
        pass
    elif Area == "学校食堂和超市":
        image_diningHall = Image.open()
        image_diningHall.show
        pass
    elif Area == "环校路":
        image_surroundRoad = Image.open()
        image_surroundRoad.show
        pass
    elif Area == "校园A岗":
        image_A = Image.open()
        image_A.show
        pass
    elif Area == "荷花池":
        image_lotusPond = Image.open()
        image_lotusPond.show
        pass
    elif Area == "教师值班室":
        image_teacherDutyRoom = Image.open()
        image_teacherDutuRoom.show
        pass
    elif Area == "实验楼":
        image_laboratoryBuilding = Image.open()
        image_laboratoryBuilding.show
        pass
    elif Area == "行政楼":
        image_administrationBuilding = Image.open()
        image_administrationBuilding.show
        pass
    elif Area == "珠海楼":
        image_zhuhaiBuilding = Image.open()
        image_zhuhaiBuilding.show
        pass
    elif Area == "文化广场":
        image_culturalSquare = Image.open()
        image_culturalSquare.show
        pass
    elif Area == "梧桐景观造":
        image_Sycamore = Image.open()
        image_Sycamore.show
        pass
    elif Area == "篮球场":
        image_BasketballCourt = Image.open()
        image_BasketballCourt.show
        pass
    elif Area == "阶梯教室":
        image_LectureRoom = Image.open()
        image_LectureRoom.show
        pass
    elif Area == "中山楼":
        image_zhongshanBuilding = Image.open()
        image_zhongshanBuilding.show
        pass
    elif Area == "四号楼":
        image_forthBuilding = Image.open()
        image_forthBuilding.show
        pass
    elif Area == "门厅转盘花台":
        image_flowerStand = Image.open()
        image_flowerStand.show
        pass
    elif Area == "知识阶梯":
        image_ladder = Image.open()
        image_ladder.show
        pass
    elif Area == "退出":
        break
    elif Area == "足球场":
        image_footballCourt = Image.open()
        image_footballCourt.show
        pass
    elif Area == "校园B岗":
        image_B = Image.open()
        image_B.show
        pass
    elif Area == "深圳楼":
        image_shenzhenBuilding = Image.open()
        image_shenzhenBuilding.show
        pass

print("感谢你的使用")