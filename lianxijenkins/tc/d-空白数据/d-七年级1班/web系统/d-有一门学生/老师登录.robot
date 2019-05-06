*** Settings ***
Library  py-lib.teachers.Teachers
Library  py-lib.seleniumlib
Variables  cfg.py
*** Test Cases ***
老师登录2-tc005002
#增加老师
     ${teacherlit}  addteacher  huangliangwei  黄良威  1  ${suit_eid01}  131114444554  1029432643@qq.com  5555555
     [Teardown]  delteacher  &{teacherlit}[id]
     denglu  ${seleniumloginweb}  huangliangwei  888888
     ${teacher}  get teacher message
     should be true  $teacher==['松勤学院00523', '黄良威', '初中数学', '0', '0', '0']
     ${student}  get student message
     should be true  $student=={'七年级七年级一班': ['hlw']}