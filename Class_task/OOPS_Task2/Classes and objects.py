# Classes and Objects
import logging as lg
lg.basicConfig(filename= "class_object.log", level= lg.DEBUG, format="%(asctime)s %(message)s")

class class_objet:
    def __init__(self, name):
        """ The given task is that, the concepts about class and object that we have discussed in our
         class point by point you have to write atleast 10 examples."""
        self.name = name
        pass

class ineuron:
    try:
        def about_ineuron(self):
            lg.info("iNeuron offers affordable online courses, job guarantee programs, placement assistance, a revolutionary self-paced internship portal and an unparalleled job portal")
        def address(self):
            lg.info("17th Floor tower A Brigade Signature Towers, Sannatammanahalli, Bengaluru, Karnataka 562129")
        def contact_mail(self):
            lg.info("contact@ineuron.ai")
    except Exception as e:
        lg.error(e)

class one_neuron:
    try:
        def about_one_neuron(self):
            lg.info("lifetime access to 400+ courses in all technologies under one subscription")
        def tech_neuron(self):
            lg.info("There are 200+ courses in tech neuron and enrollment fees is 11800 Rs.")
        def kids_neuron(self):
            lg.info("There are 50+ courses in kids neuron and enrollment fees is 7080 Rs.")
    except Exception as e:
        lg.error(e)

class blog:
    try:
        def website(self):
            """Is is the official website of ineuron blog."""
            lg.info("https://blog.ineuron.ai")
        def category(self):
            for i in blogs:
                if "python" in i:
                    lg.info("I like python blogs")
    except Exception as  e:
        lg.error(e)

class number_of_courses:
    try:
        def total_courses(self):
            lg.info("There are 400+ courses in ineuron.")
        def top_catagories(self):
            lg.info(course_list)
        def data_science(self):
            lg.info("I enrolled in data science course")
    except Exception as e:
        lg.error(e)

class my_class:
    try:
        def my_course(self):
            lg.info("My course name is Full stack data science bootcamp.")
        def recent_topic(self):
            lg.info("Python")
    except Exception as e:
        lg.error(e)

class class_type:
    try:
        def live_class(self):
            lg.info("As per schedule in every weekend there is live class.")
        def recording_class(self):
            lg.info("After every live classes, we can access the recording of live classes at any time.")
    except Exception as e:
        lg.error(e)

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
        def technology(self):
            lg.info("First you've to select the technology.")
        def domain(self):
            lg.info("Then select domain as per your desire.")
        def project(self):
            lg.info("After that select a project whatever you like and complete that project.")
        def experience(self):
            lg.info("After completing of project you'll get internship certificate.")
    except Exception as e:
        lg.error(e)

class job:
    try:
        def job_type(self):
            for i in data:
                if i == "Data Science":
                    lg.info("I want to be a data scientist")
    except Exception as e:
        lg.error(e)

class feedback:
    try:
        def about_class(self):
            lg.info("Every classes are amazing and I able to learn new things.")
        def query_team(self):
            lg.info("They always help us.")
    except Exception as e:
        lg.error(e)

# Creating objects of the above classes
i = ineuron()
i.about_ineuron()
i.address()
i.contact_mail()
lg.info("\n")

one_i = one_neuron()
one_i.about_one_neuron()
one_i.tech_neuron()
one_i.kids_neuron()
lg.info("\n")

Blg = blog()
Blg.website()
blogs = ["Data Science, Big Data, Machine Learning, python"]
Blg.category()
lg.info("\n")

courses = number_of_courses()
courses.total_courses()
course_list = ["Data Science, Big Data, Machine Learning, Data analyst, AWS, SQl, Excel, etc."]
courses.top_catagories()
courses.data_science()
lg.info("\n")

classes = my_class()
classes.my_course()
classes.recent_topic()
lg.info("\n")

cls_type = class_type()
cls_type.live_class()
cls_type.recording_class()
lg.info("\n")

student = ineuron_students()
student.names()
student.recent_student()
lg.info("\n")

intern = internship()
intern.technology()
intern.domain()
intern.project()
intern.experience()
lg.info("\n")

JOB = job()
data = ["Data Science", "Python Developer", "Data Analyst"]
JOB.job_type()
lg.info("\n")

FeedBack = feedback()
FeedBack.about_class()
FeedBack.query_team()


