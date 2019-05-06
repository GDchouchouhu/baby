*** Settings ***
Variables  cfg.py
Library  py-lib.student.Student
*** Test Cases ***
添加学生2-tc002002
#增加新学生
    ${addstudent}  addstudent   &{two_student}[name]  &{two_student}[realname]  &{two_student}[gradeid]
    ...  ${suit_eid01}  &{two_student}[phonenumber]
    should be true  &{addstudent}[retcode]==0

    ${list}  liststudent
#判断包含
    studentshouldContain  ${suit_eid01}  &{two_student}[name]  &{two_student}[realname]  &{two_student}[phonenumber]
    ...  &{addstudent}[id]  &{list}[retlist]
    [Teardown]  delstudent  &{addstudent}[id]


删除学生1-tc002081
    ${beforelist}  liststudent
#增加一个学生
    ${addstudent}  addstudent   &{two_student}[name]  &{two_student}[realname]  &{two_student}[gradeid]
    ...  ${suit_eid01}  &{two_student}[phonenumber]

    should be true  &{addstudent}[retcode]==0
#删除学生
    ${del_s}  delstudent  &{addstudent}[id]

    should be true  &{del_s}[retcode]==0

    ${afterlist}  liststudent
#判断
    should be true  ${beforelist}  ${afterlist}