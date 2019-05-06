*** Settings ***
Library  py-lib.classroom.Classroom
Variables  cfg.py
*** Test Cases ***
增加班级-tc000001
    [Teardown]  delallclassroom
#增加班级
    ${class}  addClassroom  &{add_classroom}[grade]  &{add_classroom}[name]  &{add_classroom}[limit]
#列出班级
    ${classs}  listClassroom
    ${onlyclass}   evaluate  &{classs}[retlist][0]
#判断
    should be true  &{class}[id]==&{onlyclass}[id]
    should be true  $onlyclass['invitecode']==$class['invitecode']