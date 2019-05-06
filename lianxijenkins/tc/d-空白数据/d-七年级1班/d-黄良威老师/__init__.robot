*** Settings ***
Library  py-lib.teachers.Teachers
Variables  cfg.py
Suite Setup   addteacher  &{add_teacher}[username]   &{add_teacher}[realname]  &{add_teacher}[subjectid]
    ...  ${suit_eid01}  &{add_teacher}[phonenumber]  &{add_teacher}[email]  &{add_teacher}[idcard]  newteacher
Suite Teardown  delteacher  ${newteacher}