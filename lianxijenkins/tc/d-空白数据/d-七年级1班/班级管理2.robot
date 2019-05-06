*** Settings ***
Library  py-lib.classroom.Classroom
Variables  cfg.py
*** Test Cases ***
增加班级2-tc000002
    [Documentation]  增加新的班级
    [Teardown]  delclassroom  &{class}[id]
#增加班级
    ${class}  addClassroom  &{add_classroom}[grade]  &{add_classroom}[name]  &{add_classroom}[limit]
    should be true  $class['retcode']==0

#列出班级
    ${classs}  listClassroom
    ${onlyclass0}   evaluate  $classs['retlist']
#判断
    tshouldContain  ${onlyclass0}
    ...  &{add_classroom}[name]   &{add_classroom}[nianji]
    ...  &{class}[invitecode]  &{add_classroom}[limit]  0  &{class}[id]


增加班级3-tc000003
    [Documentation]  增加新的班级
#列出班级
    ${class}  listClassroom  1
    ${onlyclass}   evaluate  $class['retlist']
    ${len}  evaluate  len(${onlyclass})
#增加同名班级
    ${class1}  addClassroom  &{add_same_classroom}[grade]
    ...  &{add_same_classroom}[name]  &{add_same_classroom}[limit]
    should be true  $class1['retcode']==1

    ${newclass}  listClassroom
    ${twoclass}   evaluate  $newclass['retlist']
    ${newlen}  evaluate  len(${twoclass})
#判断
    should be true  $newlen==$len
    should be equal  ${twoclass}  ${onlyclass}


修改班级1-tc000051
#增加班级
        [Teardown]  delClassroom  &{class}[id]
        ${class}  addclassroom  &{add_classroom}[grade]  &{add_classroom}[name]  &{add_classroom}[limit]
        should be true  $class['retcode']==0
#修改班级
        ${newclass}  modifyClassroom  &{class}[id]  &{modifyclassroom}[name]  &{modifyclassroom}[limit]
        should be true  $newclass['retcode']==0

        ${afterclass}  listClassroom
#对比列表是否只包含一次修改后的参数
        tshouldContain  &{afterclass}[retlist]  &{modifyclassroom}[name]
        ...  &{add_classroom}[nianji]  &{class}[invitecode]  &{modifyclassroom}[limit]  0  &{class}[id]

修改班级2-tc000052
#增加班级
        [Teardown]  delClassroom  &{class}[id]
        ${class}  addclassroom  &{add_classroom}[grade]  &{add_classroom}[name]  &{add_classroom}[limit]
        should be true  $class['retcode']==0
#修改为同名班级
        ${beforerclass}  listClassroom
        ${newclass}  modifyClassroom  &{class}[id]  &{add_same_classroom}[name]  &{add_same_classroom}[limit]

        should be true  $newclass['retcode']==1       #有bug
        should be true  $newclass['reason']=='duplicated class name'
#判断
        ${afterclass}  listClassroom
        should be true  $afterclass['retlist']==$beforerclass['retlist']

修改班级3-tc000053

        ${beforeclass}  listClassroom

#增加不存在的班级
        ${newclass}  modifyClassroom  &{impossible_classroom}[id]
          ...  &{impossible_classroom}[name]  &{impossible_classroom}[limit]

        should be true  $newclass['retcode']==404
        should be true  $newclass['reason']=='id 为`&{impossible_classroom}[id]`的班级不存在'

        ${afterclass}  listClassroom
#判断
        should be true  $afterclass['retlist']==$beforeclass['retlist']

删除班级1-tc000081
#删除不存在班级
        ${ret}  delclassroom  5454545
        should be true  $ret['retcode']==404
        should be true  $ret['reason']=="id 为`5454545`的班级不存在"

删除班级2-tc000082
        ${beforeclass}  listClassroom
#增加班级

        ${ret}  addClassroom  &{add_classroom}[grade]  &{add_classroom}[name]  &{add_classroom}[limit]
        should be true  $ret['retcode']==0
#删除该新增班级
        ${ret}  delclassroom  &{ret}[id]
        should be true  $ret['retcode']==0
#判断
        ${afterclass}  listClassroom
        should be true  $beforeclass['retlist']==$afterclass['retlist']