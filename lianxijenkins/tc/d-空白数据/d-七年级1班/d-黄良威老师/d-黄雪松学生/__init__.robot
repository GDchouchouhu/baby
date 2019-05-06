*** Settings ***
Library  py-lib.student.Student
Variables  cfg.py
Suite Setup   addstudent   &{onestudent}[name]  &{onestudent}[realname]  &{onestudent}[gradeid]
    ...  ${suit_eid01}  &{onestudent}[phonenumber]  studentid
Suite Teardown  delstudent  ${studentid}
