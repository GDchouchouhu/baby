#_*_ coding:utf-8 _*_
import requests
from cfg import vcode,studenturl
import pprint,json
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.BuiltIn import BuiltIn
class Student():
    def __init__(self):
        self.url=studenturl
        self.vcode=vcode
    def liststudent(self):
        param = {
            'vcode': self.vcode,
            'action': 'search_with_pagenation'
        }
        r = requests.get(self.url,params=param)
        pprint.pprint(r.json())
        return r.json()

    def delstudent(self,studentid):
        url='{}/{}'.format(self.url,studentid)
        data={
            'vcode':self.vcode
        }
        r = requests.delete(url, data=data)
        pprint.pprint(r.json())
        return r.json()

    def delallstudent(self):
        list=self.liststudent()
        if list['retlist']:
            for i in list['retlist']:
                self.delstudent(i['id'])
        a=self.liststudent()
        if a['retlist']:
            raise Exception('no clear all teachers')

    def addstudent(self,username,
                   realname,
                   gradeid,
                   classid,
                   phonenumber,
                   returnid=None):

        data={
            'vcode':self.vcode,
            'action':'add',
            'username':username,
            'realname':realname,
            'gradeid':gradeid,
            'classid':classid,
            'phonenumber':phonenumber
        }
        r=requests.post(self.url,data=data)
        responses=r.json()
        pprint.pprint(responses)
        if returnid:
            BuiltIn().set_global_variable('${%s}'%returnid,responses['id'])
        return responses

    def modifystudent(self,studentid,
                      realname=None,
                      phonenumber=None):
        url='{}/{}'.format(self.url,studentid)
        data={
            'vcode':self.vcode,
            'action':'modify'
        }
        if realname:
            data['realname']=realname
        if phonenumber:
            data['phonenumber']=phonenumber
        r =requests.put(url,data=data)
        pprint.pprint(r.json())
        return r.json()

    def studentshouldContain(self,classid,username,realname,phonenumber,id,more):
        now={
            "classid": classid,
            "username": username,
            "realname": realname,
            "phonenumber": phonenumber,
            "id": id
        }
        pprint.pprint(now)
        if more.count(now) != 1:
            raise Exception("bad guy")

