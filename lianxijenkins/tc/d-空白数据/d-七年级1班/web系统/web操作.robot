*** Settings ***
Library  py-lib.seleniumlib
Library  py-lib.teachers.Teachers
Library  py-lib.student.Student
Variables  cfg.py
*** Test Cases ***
老师登录1-tc005001
#调用接口增加老师
        ${teacherlit}  addteacher  huangliangwei  黄良威  1  ${suit_eid01}  131114444554  1029432643@qq.com  5555555
#        登录
        should be true  &{teacherlit}[retcode]==0
        denglu  ${seleniumloginweb}  huangliangwei  888888
#获取老师信息
        ${teacher}  get_teacher_message
        should be true  $teacher==['松勤学院00523', '黄良威', '初中数学', '0', '0', '0']
#获取学生信息
        ${student}  get_student_message
        should be true  $student=={'七年级七年级一班': []}
        [Teardown]  delteacher  &{teacherlit}[id]


学生登录1-tc005081
#调用学生创建接口
    ${student}  addstudent   hlw  hlw  1  ${suit_eid01}  135252525
    should be true  &{student}[retcode]==0
    denglu_student  ${seleniumsudentlogin}  hlw  888888
    ${text}  student_text
    should be true  $text==['hlw','松勤学院00523','0','0']
    ${tips}  get_student_bad_homework
    should be true  $tips=='您尚未有错题入库哦'
    [Teardown]  delstudent  &{student}[id]