*** Settings ***
Library  py-lib.seleniumlib
Suite Setup  openbrower
Suite Teardown  closebrower
Variables  cfg.py
*** Test Cases ***
老师发布作业1-tc005101
    denglu   ${seleniumloginweb}  &{add_teacher}[username]  888888
    teacher_send_homework
    denglu_student   ${seleniumsudentlogin}  &{onestudent}[name]  888888
    student_do_homework
    denglu   ${seleniumloginweb}  &{add_teacher}[username]  888888
    ${jieguo}  teacher_see_student_homework
    should be true  $jieguo==['A','A','A']