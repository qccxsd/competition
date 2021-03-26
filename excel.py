#已安装 xlrd xlwt serial模块
import xlrd,xlwt,serial,datetime

#串口部分
ser=serial.Serial("com3",9600,timeout=5) #winsows系统使用com3口连接串行口 com具体看系统配置
ser.open #打开端口
print(ser.is_open)#检测端口是否打开
Date=ser.readline() #读取串口
print(Date)#输出调试
# print(type(Date)) 检测数据类型
Date1=list(Date) #设置新变量改变数据 
# print(type(Date1)) 检测新变量数据类型

#向串口写入
"""
ser.write("a".encode('utf-8'))
"""

#创建时间变量
time= datetime.datetime.now()
year = time.strftime('%Y')
month= time.strftime('%m')
day= time.strftime('%d')
printtime = year + month + day

#将端口存储方便写入excel
#创建workbook和sheet对象
workbook = xlwt.Workbook() 
sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
#向sheet页中写入数据
sheet1.write(0,0,'')
sheet1.write(0,1,'')
sheet1.write(0,3,'')
sheet1.write(0,2,'')
sheet1.write(0,4,'')
sheet1.write(1,0,'')
sheet1.write(1,1,'')
sheet1.write(1,2,'')
sheet1.write(1,3,'')
sheet1.write(1,4,'')
#如有需要可以添加
#保存该excel文件,有同名文件时直接覆盖
workbook.save('%s.xlsx'% printtime)
print('创建excel文件完成!')

#读取excel表格
date = xlrd.open_workbook('%s.xlsx '%printtime)#打开xlsx文件(相对路径)
table = date.sheets()[0]#打开第一张表
nrows =table.nrows#获取表的行数
#for循环逐行输出
for i in range(nrows):
    print(table.row_values(i)[:4])#前四行数据

#ser.close #关闭端口