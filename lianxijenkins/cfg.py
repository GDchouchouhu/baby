vcode='00000005288165324011'
url='http://ci.ytesting.com/api/3school/school_classes'
teacherurl='http://ci.ytesting.com/api/3school/teachers'
studenturl='http://ci.ytesting.com/api/3school/students'
# 同名班级参数配置
add_same_classroom={"name":'七年级一班','grade':1,"limit":20}
# 增加班级
add_classroom={"name":'七年级二班','grade':1,"limit":20,'nianji':"七年级"}
# 修改班级
modifyclassroom={'name':"七年级二班修改版",'limit':100}
# 不存在的班级
impossible_classroom={'id':9999,'name':'修改不存在id','limit':100}


#########老师配置############
subjectid='''
初中数学	1
初中科学	5
初中英语	11
初中体育	12
高中语文	13
高中数学	14
'''
add_teacher = {
             'username':'huangliangwei',
             'realname':'黄良威',
             'subjectid':1,
             'email':'1029432643@qq.com',
             'idcard':4455454545,
             'phonenumber':13144115486
            }
teacher_should_be_contain = {
             'username':'huangliangwei',
             'realname':'黄良威',
             'subjectid':1,
             'email':'1029432643@qq.com',
             'idcard':'4455454545',
             'phonenumber':'13144115486'
            }

add_teacher2 = {
             'username':'yangjinglin',
             'realname':'杨婧琳',
             'subjectid':5,
             'email':'1029432643@qq.com',
             'idcard':88888888,
             'phonenumber':13927956211
            }
teacher_should_be_contain2= {
             'username':'yangjinglin',
             'realname':'杨婧琳',
             'subjectid':5,
             'email':'1029432643@qq.com',
             'idcard':'88888888',
             'phonenumber':'13927956211'
            }
impossible_teacher={'id':55555,
                    'realname':'ssdsfd',
                    'subjectid':1,
                    'phonenumber':15544564222,
                    'email':'10365421@qq.com',
                    'idcardnumber':12222122}

#########学生配置############
onestudent={'name':'hlw',
            'realname':'黄雪松',
            'gradeid':1,
            'phonenumber':'4213213'
}
two_student={'name':'yjl',
            'realname':'杨经理',
            'gradeid':1,
            'phonenumber':'131321315'
}


seleniumloginweb='http://ci.ytesting.com/teacher/login/login.html'
seleniumsudentlogin='http://ci.ytesting.com/student/login/login.html'