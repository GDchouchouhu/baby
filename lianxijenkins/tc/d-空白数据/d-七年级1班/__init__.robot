*** Settings ***
Library  py-lib.classroom.Classroom
Variables  cfg.py
Suite Setup  addClassroom  &{add_same_classroom}[grade]  &{add_same_classroom}[name]
  ...  &{add_same_classroom}[limit]  suit_eid01
Suite Teardown  delClassroom   ${suit_eid01}