#_*_ coding:utf-8 _*_
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains as ac
class seleniumlib():
    ROBOT_LIBRARY_SCOPE='GLOBAL'
    def openbrower(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()


    def closebrower(self):
        self.driver.quit()

    def denglu(self,url,username,password):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

        name=self.driver.find_element_by_css_selector('.form input#username')
        name.clear()
        name.send_keys(username)

        passwd=self.driver.find_element_by_css_selector('.form input#password')
        passwd.clear()
        passwd.send_keys(password)

        self.driver.find_element_by_css_selector(".form button").click()

    def get_teacher_message(self):
        self.driver.find_element_by_css_selector(".main-menu a[href='#/home'] li").click()
        time.sleep(2)
        xinxi = self.driver.find_elements_by_css_selector('table.table tr td:nth-child(2)')
        xinxi2 = self.driver.find_elements_by_css_selector('div.col-md-12:nth-child(1)>div strong')
        text=[i.text.strip() for i in xinxi]
        text2=[i.text.strip() for i in xinxi2]
        textupdate=text+text2
        return textupdate

    def get_student_message(self):
        self.driver.find_element_by_css_selector('.main-menu ul li[style]:nth-of-type(4)').click()
        self.driver.find_element_by_css_selector('.main-menu>ul>li:nth-of-type(4) a[href$=group] span').click()
        time.sleep(1)
        more = self.driver.find_elements_by_css_selector('div.panel')

        student_dict={}
        self.driver.implicitly_wait(1)
        for i in more:
            heng = i.find_element_by_css_selector('div.panel-heading a')
            title=heng.text.replace(" ",'')
            i.click()
            time.sleep(1)
            students_name=i.find_elements_by_css_selector('tr td:nth-of-type(2)')
            student_list=[i.text for i in students_name]
            student_dict[title]=student_list
        self.driver.implicitly_wait(10)
        return student_dict

    def denglu_student(self,url,names,pas):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

        name = self.driver.find_element_by_css_selector('[name="username"]')
        name.clear()
        name.send_keys(names)
        passwd=self.driver.find_element_by_css_selector('[name="password"]')
        passwd.clear()
        passwd.send_keys(pas)
        self.driver.find_element_by_css_selector('#submit').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('.text-center')

    def student_text(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@class='main-menu']/ul/a[1]/li").click()
        ts = self.driver.find_elements_by_xpath('//tbody/tr[position()<=last()-1]/td[2]')
        t = [i.text.strip() for i in ts]

        tz = self.driver.find_elements_by_xpath("//*[@class='col-md-12']//h2")
        tt = [i.text.strip() for i in tz]
        list =t+tt

        return list

    def get_student_bad_homework(self):
        self.driver.find_element_by_xpath("//*[@class='main-menu']/ul/a[4]/li").click()

        tips =self.driver.find_element_by_xpath("//*[@class='fa fa-bug']/following-sibling::span[1]")

        return tips.text



    def teacher_send_homework(self):
        self.driver.find_element_by_css_selector('.main-menu>ul>li:nth-of-type(2)').click()

        self.driver.find_element_by_css_selector('a[ng-click="show_page_addexam()"]>li').click()

        time.sleep(1)

        self.driver.find_element_by_css_selector('#exam_name_text').send_keys('作业')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#btn_pick_question').click()
        time.sleep(2)
        self.driver.switch_to.frame('pick_questions_frame')
        # time.sleep(5000)
        time.sleep(2)
        for i in range(3):
            add_homeworks = self.driver.find_elements_by_css_selector('.btn_pick_question')
            print(add_homeworks)
            add_homeworks[i].click()
            time.sleep(1)
        time.sleep(1)
        self.driver.find_element_by_css_selector('#cart_footer div.btn-group div:nth-of-type(2)').click()
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#btn_submit').click()

        time.sleep(2)
        self.driver.find_element_by_css_selector('.bootstrap-dialog-footer-buttons button:nth-child(2)').click()

        current_handle=self.driver.current_window_handle
        all_handles=self.driver.window_handles
        for i in all_handles:
            self.driver.switch_to.window(i)
            if self.driver.title=='下发学习任务':

               break
        self.driver.find_element_by_css_selector('label').click()
        self.driver.find_element_by_css_selector("h3 button[type='button']").click()
        time.sleep(1)
        atan=self.driver.find_elements_by_css_selector('.modal-content')
        if atan:
            atan[0].find_element_by_css_selector('button[ng-click="dispatchIt()"]').click()
        time.sleep(3)
        tankuang = self.driver.find_elements_by_css_selector('.modal-content ')
        if tankuang:
            time.sleep(1)
            aa=tankuang[1].find_element_by_css_selector('.bootstrap-dialog-footer button')
            aa.click()

        self.driver.switch_to.window(current_handle)

    def student_do_homework(self):
        self.driver.find_element_by_css_selector('a[href="#/task_manage"] li').click()
        self.driver.find_element_by_css_selector('button[ng-click="viewTask(taskTrack)"]').click()
        time.sleep(1)
        answer=self.driver.find_elements_by_css_selector('.btn-group button:nth-child(1)')
        for i in answer:
            i.click()
        self.driver.find_element_by_css_selector('button[ng-click="saveMyResult(true)"]').click()

        self.driver.find_element_by_xpath("//*[@class='bootstrap-dialog-footer-buttons']/button[2]").click()

    def teacher_see_student_homework(self):
        el = self.driver.find_element_by_css_selector('.main-menu>ul>li:nth-of-type(2)')
        ac(self.driver).move_to_element(el).perform()

        self.driver.find_element_by_css_selector('a[href="#/task_manage?tt=1"]>li').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('a[ng-click="trackTask(task)"] .fa.fa-search').click()

        self.driver.find_element_by_css_selector('button.btn-outlined.ng-scope').click()
        current_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for i in all_handles:
            self.driver.switch_to.window(i)
            if self.driver.title == '查看作业':
                break
        all = self.driver.find_elements_by_css_selector('.myCheckbox input:checked')
        questions=[]
        for i in all:
            question=i.find_element_by_xpath("./..").text.strip()
            questions.append(question)
            time.sleep(1)
        return questions