*** Settings ***
Library  py-lib.teachers.Teachers
Variables  cfg.py
*** Test Cases ***
添加老师1-tc001001
#增加老师
    ${addteacher}  addteacher  &{add_teacher}[username]   &{add_teacher}[realname]  &{add_teacher}[subjectid]
    ...  ${suit_eid01}  &{add_teacher}[phonenumber]  &{add_teacher}[email]  &{add_teacher}[idcard]

    should be true  &{addteacher}[retcode]==0

    ${teacherlist}  listteacher
#老师列表包含判断
    teachershouldContain     &{teacher_should_be_contain}[username]   ${suit_eid01}
    ...  &{teacher_should_be_contain}[realname]   &{addteacher}[id]   &{teacher_should_be_contain}[phonenumber]
    ...  &{teacher_should_be_contain}[email]     &{teacher_should_be_contain}[idcard]   &{teacherlist}[retlist]
    [Teardown]  delteacher  &{addteacher}[id]