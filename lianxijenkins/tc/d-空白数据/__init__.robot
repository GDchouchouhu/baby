*** Settings ***
Library  py-lib.classroom.Classroom
Library  py-lib.teachers.Teachers
Library  py-lib.student.Student
Suite Setup  run keywords  delallstudent  AND  delallteacher  AND  delAllClassroom
Suite Teardown  run keywords  delallstudent  AND  delallteacher  AND  delAllClassroom