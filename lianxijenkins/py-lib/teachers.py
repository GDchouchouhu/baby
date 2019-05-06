#_*_ coding:utf-8 _*_
import requests
from cfg import vcode,teacherurl
import pprint,json
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.BuiltIn import BuiltIn
class Teachers():
    def __init__(self):
        self.url=teacherurl
        self.vcode=vcode
    def listteacher(self,subjectid=None):
        if subjectid:
            param={
                'vcode':self.vcode,
                'action':'search_with_pagenation',
                'subjectid':int(subjectid)
            }
        else:
            param = {
                'vcode': self.vcode,
                'action': 'search_with_pagenation'
            }
        r = requests.get(self.url,params=param)
        pprint.pprint(r.json())
        return r.json()

    def delteacher(self,teacherid):
        url='{}/{}'.format(self.url,teacherid)
        data={
            'vcode':self.vcode
        }
        r = requests.delete(url, data=data)
        pprint.pprint(r.json())
        return r.json()

    def delallteacher(self):
        list=self.listteacher()
        if list['retlist']:
            for i in list['retlist']:
                self.delteacher(i['id'])
        a=self.listteacher()
        if a['retlist'] !=[]:
            raise Exception('no clear all teachers')

    def addteacher(self,username,
                   realname,
                   subjectid,
                   classlist,
                   phonenumber,
                   email,
                   idcard,
                   returnid=None):
        list=str(classlist).split(',')
        newlist=[{'id':i.strip()} for i in list if i !='']
        data={
            'vcode':self.vcode,
            'action':'add',
            'username':username,
            'realname':realname,
            'subjectid':subjectid,
            'phonenumber':phonenumber,
            'classlist':json.dumps(newlist),
            'email':email,
            'idcardnumber':idcard
        }
        r=requests.post(self.url,data=data)
        responses=r.json()
        pprint.pprint(responses)
        if returnid:
            BuiltIn().set_global_variable('${%s}'%returnid,responses['id'])
        return responses

    def modifyteacher(self,teacherid,
                      realname=None,
                      subjectid=None,
                      classlist=None,
                      phonenumber=None,
                      email=None,
                      idcardnumber=None):
        url='{}/{}'.format(self.url,teacherid)
        data={
            'vcode':self.vcode,
            'action':'modify'
        }
        if realname:
            data['realname']=realname
        if subjectid:
            data['subjectid']=subjectid
        if classlist:
            list = str(classlist).split(',')
            newlist = [{'id': i.strip()} for i in list if i != '']
            data['classlist']=json.dumps(newlist)
        if phonenumber:
            data['phonenumber']=phonenumber
        if email:
            data['email']=email
        if idcardnumber:
            data['idcardnumber']=idcardnumber
        r =requests.put(url,data=data)
        pprint.pprint(r.json())
        return r.json()

    def teachershouldContain(self,name,list,realname,id,phonenumber,email,idcardnumber,more):
        list=str(list).split(',')
        now={
            "username": name,
            "teachclasslist": [int(i) for i in list if i !=''],
            "realname": realname,
            "id": id,
            "phonenumber": str(phonenumber),
            "email": email,
            "idcardnumber": idcardnumber
        }
        pprint.pprint(now)
        if more.count(now) != 1:
            raise Exception("bad guy")

if __name__=='__main__':
    t=Teachers()
    print(t.listteacher())