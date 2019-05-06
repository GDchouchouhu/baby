#_*_ coding:utf-8 _*_
import requests
from cfg import vcode,url
import pprint
from robot.libraries.BuiltIn import BuiltIn
class Classroom():
    def __init__(self):
        self.vcode=vcode
        self.url=url
    def listClassroom(self,gradeid=None):
        if gradeid==None:
            param={
                'vcode':self.vcode,
                'action':'list_classes_by_schoolgrade'
            }
        else:
            param = {
                'vcode':self.vcode,
                'action': 'list_classes_by_schoolgrade',
                'gradeid':int(gradeid)
            }
        r = requests.get(self.url,params=param)
        pprint.pprint(r.json(),indent=2)
        return r.json()

    def addClassroom(self,grade,classroomName,studentlimit,returnid=None):
        data={
            'vcode':self.vcode,
            'action':'add',
            'grade':int(grade),
            'name':classroomName,
            'studentlimit':int(studentlimit)
        }
        r= requests.post(self.url,data=data)
        pprint.pprint(r.json(),indent=2)
        aaa=r.json()

        if returnid:
            name="${%s}"%returnid
            print(name)
            BuiltIn().set_global_variable(name,aaa['id'])
        return aaa
    def delClassroom(self,classid):
        url='{0}/{1}'.format(self.url,classid)
        data={
            'vcode':self.vcode
        }
        a= requests.delete(url,data=data)
        return a.json()
    def delAllClassroom(self):
        a= self.listClassroom()
        if a['retlist']==[]:
           print('已经删除完毕')
        for i in a['retlist']:
            self.delClassroom(i['id'])
        b = self.listClassroom()
        if b['retlist']:
            raise Exception('no clear classroom')

    def tshouldContain(self,more,name,grade,invite,limit,student,id):
        now={
            'name': name,
            'grade__name': grade,
            'invitecode': invite,
            'studentlimit': int(limit),
             'studentnumber': int(student),
            'id': int(id),
            'teacherlist': []
        }
        print(now)
        print(more)
        if more.count(now) != 1:
            raise Exception("bad guy")

    def modifyClassroom(self,classid,name,limit):
        data={
            'vcode':self.vcode,
            'action':'modify',
            'name':name,
            'studentlimit':limit
        }
        url="{}/{}".format(self.url,classid)
        r=requests.put(url,data=data)
        pprint.pprint(r.json())
        return r.json()