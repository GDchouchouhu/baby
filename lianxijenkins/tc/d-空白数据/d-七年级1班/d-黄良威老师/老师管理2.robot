*** Settings ***
Library  py-lib.teachers.Teachers
Variables  cfg.py
Library  py-lib.classroom.Classroom

*** Test Cases ***
添加老师2-tc001002
#增加第二个老师
    ${newteacher}  addteacher  &{add_teacher2}[username]   &{add_teacher2}[realname]  &{add_teacher2}[subjectid]
    ...  ${suit_eid01}  &{add_teacher2}[phonenumber]  &{add_teacher2}[email]  &{add_teacher2}[idcard]

    should be true  &{newteacher}[retcode]==0
#列出老师
    ${list}  listteacher
#判断包含
    teachershouldContain   &{teacher_should_be_contain2}[username]   ${suit_eid01}
    ...  &{teacher_should_be_contain2}[realname]   &{newteacher}[id]   &{teacher_should_be_contain2}[phonenumber]
    ...  &{teacher_should_be_contain2}[email]     &{teacher_should_be_contain2}[idcard]   &{list}[retlist]
    [Teardown]  delteacher  &{newteacher}[id]


添加老师3-tc001003
#列出老师列表
    ${beforelist}  listteacher

#增加同名老师
    ${jieguo}  addteacher  &{add_teacher}[username]   &{add_teacher}[realname]  &{add_teacher}[subjectid]
    ...  ${suit_eid01}  &{add_teacher}[phonenumber]  &{add_teacher}[email]  &{add_teacher}[idcard]
    should be true  &{jieguo}[retcode]==1
    should be true  $jieguo['reason']=="登录名 huangliangwei 已经存在"

#列出老师列表
    ${afterlist}  listteacher

# 判断
    should be true  &{beforelist}[retlist]==&{afterlist}[retlist]



修改老师1-tc001051
    [Documentation]  修改不存在的老师id
    ${list}  listteacher

#修改不存在的老师id
    ${modif_teacher}  modifyteacher  &{impossible_teacher}[id]   &{impossible_teacher}[realname]
    should be true  &{modif_teacher}[retcode]==1
    should be true  $modif_teacher['reason']=="id 为`&{impossible_teacher}[id]`的老师不存在"
#判断修改前后老师列表是否一致
    ${newlist}  listteacher
    should be true  $list['retlist']==$newlist['retlist']

修改老师2-tc001052
#增加老师
    ${newteacher}  addteacher  &{add_teacher2}[username]   &{add_teacher2}[realname]  &{add_teacher2}[subjectid]
    ...  ${suit_eid01}  &{add_teacher2}[phonenumber]  &{add_teacher2}[email]  &{add_teacher2}[idcard]
    should be true  $newteacher['retcode']==0

#增加两个新班级
     ${twoteacher}  addClassroom  1  七年级10班  20
     ${threeteacher}  addClassroom  1  七年级11班  20
#修改老师

    ${modif_teacher}  modifyteacher  &{newteacher}[id]  羊羊羊  1  &{twoteacher}[id],&{threeteacher}[id]

    should be true  &{modif_teacher}[retcode]==0
    ${list}  listteacher
#判断包含
    teachershouldContain   &{teacher_should_be_contain2}[username]   &{twoteacher}[id],&{threeteacher}[id]
    ...  羊羊羊   &{newteacher}[id]   &{teacher_should_be_contain2}[phonenumber]
    ...  &{teacher_should_be_contain2}[email]     &{teacher_should_be_contain2}[idcard]   &{list}[retlist]

    [Teardown]  run keywords  delteacher  &{newteacher}[id]
    ...  AND  delclassroom  &{twoteacher}[id]
    ...  AND  delclassroom  &{threeteacher}[id]


删除老师1-tc001081
#删除老师
    ${del_teacher}  delteacher  &{impossible_teacher}[id]
    should be true  &{del_teacher}[retcode]==404
    should be true  $del_teacher['reason']=="id 为`&{impossible_teacher}[id]`的老师不存在"

删除老师2-tc001082
    ${beforelist}  listteacher
#    增加老师
    ${newteacher}  addteacher  &{add_teacher2}[username]   &{add_teacher2}[realname]  &{add_teacher2}[subjectid]
    ...  ${suit_eid01}  &{add_teacher2}[phonenumber]  &{add_teacher2}[email]  &{add_teacher2}[idcard]
    should be true  ${newteacher}[retcode]==0
#删除老师
    ${del_teacher}  delteacher  &{newteacher}[id]
    should be true  &{del_teacher}[retcode]==0

    ${afterlist}  listteacher
    should be equal  ${afterlist}  ${beforelist}