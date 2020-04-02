# 国际与国内身体质量指数计算
height,weight=eval(input("请输入身高（米）和体重（kg），数据之间用逗号隔开并按回车确认："))
bim=weight/pow(height,2)
print ("BMI指数为：{:.2f}",format(bim))
who,nat="",""
if bim<18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5<=bim<24:
    who, nat = "正常", "正常"
elif 24<=bim<25:
    who, nat = "正常", "偏胖"
elif 25<=bim<28:
    who, nat = "偏胖", "偏胖"
elif 28<=bim<30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BIM 指标为：国际{0},国内{1}。".format(who,nat))

