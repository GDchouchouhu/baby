*** Settings ***
Library  py-lib.student.Student
Suite Setup  addstudent   hlw  hlw  1  ${suit_eid01}  135252525  studentid
Suite Teardown  delstudent  ${studentid}