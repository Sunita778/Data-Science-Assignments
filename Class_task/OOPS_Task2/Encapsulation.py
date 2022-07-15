# Encapsulation
import logging as lg
lg.basicConfig(filename= "encapsulation.log", level= lg.DEBUG, format="%(asctime)s %(message)s")

class class_objet:
    def __init__(self, name):
        """ The given task is that, the concepts about class and object that we have discussed in our
         class point by point you have to write atleast 10 examples."""
        self.name = name
        pass

class ineuron:
    try:
        def __init__(self):
            self.msg = "iNeuron offers affordable online courses, job guarantee programs, placement assistance, a revolutionary self-paced internship portal and an unparalleled job portal"

        def about_ineuron(self):
            lg.info(self.msg)
        def address(self):
            self.msg = "17th Floor tower A Brigade Signature Towers, Sannatammanahalli, Bengaluru, Karnataka 562129"
            lg.info(self.msg)
        def contact_mail(self):
            lg.info(self.msg)
    except Exception as e:
        lg.error(e)

i = ineuron()
i.about_ineuron()
i.address()
i.msg = "contact@ineuron.ai"
i.contact_mail()

class one_neuron:
    try:
        def __init__(self):
            self._line = "lifetime access to 400+ courses in all technologies under one subscription"
        def about_one_neuron(self):
            lg.info(self._line)
    except Exception as e:
        lg.error(e)

one = one_neuron()
one.about_one_neuron()
one._line = "There is tech neuron and kid neuron in one neuron."
one.about_one_neuron()

class blog:
    try:
        def __init__(self):
            self.__web = "https://blog.ineuron.ai"
        def website(self):
            """Is is the official website of ineuron blog."""
            lg.info(self.__web)
        def category(self):
            self.__web = "I like python blogs"
            for i in blogs:
                if "python" in i:
                    lg.info(self.__web)
    except Exception as  e:
        lg.error(e)

blogs = ["Data Science, Big Data, Machine Learning, python"]
Blogg = blog()
Blogg.website()
Blogg.category()

class number_of_courses:
    try:
        def __init__(self):
            self._course_detail = "I enrolled in data science course"
        def total_courses(self):
            lg.info(self._course_detail)
        def _top_catagories(self):
            lg.info(self._course_detail)
        def __data_science(self):
            lg.info(self._course_detail)
    except Exception as e:
        lg.error(e)

course = number_of_courses()
course._course_detail = "There are 400+ courses in ineuron."
course.total_courses()
course._course_detail = ["Data Science, Big Data, Machine Learning, Data analyst, AWS, SQl, Excel, etc."]
course._top_catagories()
course = number_of_courses()
course._number_of_courses__data_science()

class my_class:
    try:
        def __init__(self):
            self.__name = "Python"
        def my_course(self, about):
            self.__name = about
            lg.info(self.__name)
        def recent_topic(self):
            lg.info(self.__name)
    except Exception as e:
        lg.error(e)

myclass = my_class()
myclass.my_course("My course name is Full stack data science bootcamp.")
myclass = my_class()
myclass.recent_topic()

class class_type:
    try:
        def __init__(self):
            self.type = "As per schedule in every weekend there is live class."
        def live_class(self):
            lg.info(self.type)
        def recording_class(self):
            lg.info(self.type)
    except Exception as e:
        lg.error(e)

cls_type = class_type()
cls_type.live_class()
cls_type.type ="After every live classes, we can access the recording of live classes at any time."
cls_type.recording_class()

class ineuron_students:
    try:
        def names(self):
            lg.info("Names of all student who are learning data science")
        def recent_student(self):
            lg.info("Those students who are recently joined they will attend recording classes first.")
    except Exception as e:
        lg.error(e)

class internship:
    try:
        def __init__(self):
            self.__step = "First you've to select the technology."
        def technology(self):
            lg.info(self.__step)
        def domain(self, next):
            self.__step = next
            lg.info(self.__step)
        def project(self, next1):
            self.__step =next1
            lg.info(self.__step)
        def experience(self, last):
            self.__step = last
            lg.info(self.__step)
    except Exception as e:
        lg.error(e)

intern = internship()
intern.technology()
intern.domain("Then select domain as per your desire.")
intern.project("After that select a project whatever you like and complete that project.")
intern.experience("After completing of project you'll get internship certificate.")

class job:
    try:
        def __init__(self):
            self._name = "I want to be a data scientist"
        def job_type(self):
            for i in data:
                if i == "Data Science":
                    lg.info(self._name)
    except Exception as e:
        lg.error(e)

data = ["Data Science", "Python Developer", "Data Analyst"]
j = job()
j._name = "Data Scientist"
j.job_type()

class feedback:
    try:
        def __init__(self):
            self.msg = "Every classes are amazing and I able to learn new things."
        def about_class(self):
            lg.info(self.msg)
        def query_team(self):
            lg.info(self.msg)
    except Exception as e:
        lg.error(e)

f = feedback()
f.about_class()
f.msg ="They always help us."
f.query_team()
