# INHERITANCE

import logging as lg
lg.basicConfig(filename= "inheritance.log", level= lg.DEBUG, format="%(asctime)s %(message)s")

class inheritance:
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

class one_neuron(ineuron):
    try:
        def about_one_neuron(self):
            lg.info("lifetime access to 400+ courses in all technologies under one subscription")
        def tech_neuron(self):
            lg.info("There are 200+ courses in tech neuron and enrollment fees is 11800 Rs.")
        def kids_neuron(self):
            lg.info("There are 50+ courses in kids neuron and enrollment fees is 7080 Rs.")
    except Exception as e:
        lg.error(e)

# Creating objects of one_neuron after inheriting from parent class ineuron.
one_i = one_neuron()
one_i.about_ineuron()
one_i.address()
one_i.contact_mail()

one_i.about_one_neuron()
one_i.tech_neuron()
one_i.kids_neuron()
lg.info("\n")


class blog(one_neuron):
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

# By Using Multiple Inheritance

class number_of_courses(blog, one_neuron, ineuron):
    try:
        def total_courses(self):
            lg.info("There are 400+ courses in ineuron.")
        def top_catagories(self):
            lg.info(course_list)
        def data_science(self):
            lg.info("I enrolled in data science course")
    except Exception as e:
        lg.error(e)

a = number_of_courses()

blogs = ["Data Science, Big Data, Machine Learning, python"]
course_list = ["Data Science, Big Data, Machine Learning, Data analyst, AWS, SQl, Excel, etc."]
data = ["Data Science", "Python Developer", "Data Analyst"]

a.about_ineuron()
a.address()
a.contact_mail()

a.about_one_neuron()
a.tech_neuron()
a.kids_neuron()

a.website()
a.category()

a.total_courses()
a.top_catagories()
a.data_science()
lg.info("\n")


class my_class(number_of_courses):
    try:
        def my_course(self):
            lg.info("My course name is Full stack data science bootcamp.")
        def recent_topic(self):
            lg.info("Python")
    except Exception as e:
        lg.error(e)

# By multi-level Inheritance
class class_type(my_class):
    try:
        def live_class(self):
            lg.info("As per schedule in every weekend there is live class.")
        def recording_class(self):
            lg.info("After every live classes, we can access the recording of live classes at any time.")
    except Exception as e:
        lg.error(e)

class ineuron_students(class_type):
    try:
        def names(self):
            lg.info("Names of all student who are learning data science")
        def recent_student(self):
            lg.info("Those students who are recently joined they will attend recording classes first.")
    except Exception as e:
        lg.error(e)

class internship(ineuron_students):
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

class feedback(internship):
    try:
        def about_class(self):
            lg.info("Every classes are amazing and I able to learn new things.")
        def query_team(self):
            lg.info("They always help us.")
    except Exception as e:
        lg.error(e)

class job(feedback):       # By multi-level Inheritance
    try:
        def job_type(self):
            for i in data:
                if i == "Data Science":
                    lg.info("I want to be a data scientist")
    except Exception as e:
        lg.error(e)

# Creating objects of job class which inherits from the all above classes.

j = job()

# By method of overriding..
j.about_ineuron()
j.address()
j.contact_mail()

j.about_one_neuron()
j.kids_neuron()
j.tech_neuron()

j.website()
j.category()

j.total_courses()
j.top_catagories()
j.data_science()

j.my_course()
j.recent_topic()

j.live_class()
j.recording_class()

j.names()
j.recent_student()

j.technology()
j.domain()
j.project()
j.experience()

j.job_type()

j.about_class()
j.query_team()
