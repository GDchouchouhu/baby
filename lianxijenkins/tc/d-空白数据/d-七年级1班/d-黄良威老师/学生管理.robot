*** Settings ***
Library  py-lib.student.Student
Variables  cfg.py
*** Test Cases ***
添加学生1-tc002001
#增加学生
    ${addstudent}  addstudent   &{onestudent}[name]  &{onestudent}[realname]  &{onestudent}[gradeid]
      ...  ${suit_eid01}  &{onestudent}[phonenumber]

    should be true  &{addstudent}[retcode]==0

    ${list}  liststudent
#判断包含
    studentshouldContain  ${suit_eid01}  &{onestudent}[name]  &{onestudent}[realname]  &{onestudent}[phonenumber]
    ...  &{addstudent}[id]  &{list}[retlist]
    [Teardown]  delstudent   &{addstudent}[id]