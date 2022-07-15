# Abstraction
import logging as lg
lg.basicConfig(filename= "abstraction.log", level= lg.DEBUG, format="%(asctime)s %(message)s")

class class_objet:
    def __init__(self, name):
        """ The given task is that, the concepts about class and object that we have discussed in our
         class point by point you have to write atleast 10 examples."""
        self.name = name
        pass

class ineuron:
    try:
        def about_ineuron(self):       # Public
            lg.info("iNeuron offers affordable online courses, job guarantee programs, placement assistance, a revolutionary self-paced internship portal and an unparalleled job portal")
        def _address(self):            # Protected
            lg.info("17th Floor tower A Brigade Signature Towers, Sannatammanahalli, Bengaluru, Karnataka 562129")
        def __contact_mail(self):      # privet
            lg.info("contact@ineuron.ai")
    except Exception as e:
        lg.error(e)

i = ineuron()
i.about_ineuron()             # Public object
i._address()                  # Protected object
i._ineuron__contact_mail()    # Privet object

class one_neuron:
    try:
        def about_one_neuron(self):
            lg.info("lifetime access to 400+ courses in all technologies under one subscription")
        def __tech_neuron(self):
            lg.info("There are 200+ courses in tech neuron and enrollment fees is 11800 Rs.")
        def _kids_neuron(self):
            lg.info("There are 50+ courses in kids neuron and enrollment fees is 7080 Rs.")
    except Exception as e:
        lg.error(e)

one_i = one_neuron()
one_i.about_one_neuron()
one_i._one_neuron__tech_neuron()
one_i._kids_neuron()

class blog:
    try:
        def _website(self):
            """Is is the official website of ineuron blog."""
            lg.info("https://blog.ineuron.ai")
        def __category(self):
            for i in blogs:
                if "python" in i:
                    lg.info("I like python blogs")
    except Exception as  e:
        lg.error(e)

Blg = blog()
blogs = ["Data Science, Big Data, Machine Learning, python"]
Blg._website()
Blg._blog__category()

class number_of_courses:
    try:
        def total_courses(self):
            lg.info("There are 400+ courses in ineuron.")
        def _top_catagories(self):
            lg.info(course_list)
        def __data_science(self):
            lg.info("I enrolled in data science course")
    except Exception as e:
        lg.error(e)

course = number_of_courses()
course_list = ["Data Science, Big Data, Machine Learning, Data analyst, AWS, SQl, Excel, etc."]
course.total_courses()
course._top_catagories()
course._number_of_courses__data_science()

class my_class:
    try:
        def __my_course(self):
            lg.info("My course name is Full stack data science bootcamp.")
        def recent_topic(self):
            lg.info("Python")
    except Exception as e:
        lg.error(e)

my = my_class()
my._my_class__my_course()
my.recent_topic()

class class_type:
    try:
        def _live_class(self):
            lg.info("As per schedule in every weekend there is live class.")
        def __recording_class(self):
            lg.info("After every live classes, we can access the recording of live classes at any time.")
    except Exception as e:
        lg.error(e)

type = class_type()
type._live_class()
type._class_type__recording_class()

class ineuron_students:
    try:
        def __names(self):
            lg.info("Names of all student who are learning data science")
        def recent_student(self):
            lg.info("Those students who are recently joined they will attend recording classes first.")
    except Exception as e:
        lg.error(e)

student = ineuron_students()
student._ineuron_students__names()
student.recent_student()

class internship:
    try:
        def technology(self):
            lg.info("First you've to select the technology.")
        def _domain(self):
            lg.info("Then select domain as per your desire.")
        def _project(self):
            lg.info("After that select a project whatever you like and complete that project.")
        def experience(self):
            lg.info("After completing of project you'll get internship certificate.")
    except Exception as e:
        lg.error(e)

intern = internship()
intern.technology()
intern._domain()
intern._project()
intern.experience()

class job:
    try:
        def __job_type(self):
            for i in data:
                if i == "Data Science":
                    lg.info("I want to be a data scientist")
    except Exception as e:
        lg.error(e)

j = job()
data = ["Data Science", "Python Developer", "Data Analyst"]
j._job__job_type()

class feedback:
    try:
        def __about_class(self):
            lg.info("Every classes are amazing and I able to learn new things.")
        def query_team(self):
            lg.info("They always help us.")
    except Exception as e:
        lg.error(e)

fb = feedback()
fb._feedback__about_class()
fb.query_team()
