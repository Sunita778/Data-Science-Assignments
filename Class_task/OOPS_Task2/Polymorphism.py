# POLYMORPHISM
import logging as lg
lg.basicConfig(filename= "polymorphism.log", level= lg.DEBUG, format="%(asctime)s %(message)s")

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
        def website(self):
            lg.info("https://ineuron.ai")
    except Exception as e:
        lg.error(e)

class one_neuron:
    try:
        def about_ineuron(self):
            lg.info("lifetime access to 400+ courses in all technologies under one subscription")
        def tech_neuron(self):
            lg.info("There are 200+ courses in tech neuron and enrollment fees is 11800 Rs.")
    except Exception as e:
        lg.error(e)

## Creating polymorphism of the 2 classes (ineuron and one_neuron)
def neuron(msg):
    msg.about_ineuron()

i = ineuron()
o = one_neuron()
neuron(i)
neuron(o)


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
        def website(self):
            lg.info("https://courses.ineuron.ai")
        def category(self):
            lg.info(course_list)
    except Exception as e:
        lg.error(e)

# Creating polymorphism of the 2 classes (blog and number_of_courses)
def fun1(x):
    x.website()
    x.category()

b = blog()
c = number_of_courses()
blogs = ["Data Science, Big Data, Machine Learning, python"]
course_list = ["Data Science, Big Data, Machine Learning, Data analyst, AWS, SQl, Excel, etc."]

fun1(b)
fun1(c)


class my_class:
    try:
        def course_name(self):
            lg.info("My course name is Full stack data science bootcamp.")
    except Exception as e:
        lg.error(e)

class class_type:
    try:
        def live_class(self):
            lg.info("As per schedule in every weekend there is live class.")
        def course_name(self):
            lg.info("Data science")
    except Exception as e:
        lg.error(e)

class ineuron_students:
    try:
        def names(self):
            lg.info("Names of all student who are learning data science")
        def course_name(self):
            lg.info("Those students who are recently joined they will attend recording classes of data science.")
    except Exception as e:
        lg.error(e)

# Creating polymorphism of the 3 classes (my_class, class_type and ineuron_students)
def student(study):
    study.course_name()

me = my_class()
t = class_type()
i = ineuron_students()

student(me)
student(t)
student(i)


class internship:
    try:
        def batch(self):
            lg.info("FSDS Bootcamp")
        def project(self):
            lg.info("After that select a project whatever you like and complete that project.")
        def experience(self):
            lg.info("After completing of project you'll get internship certificate.")
    except Exception as e:
        lg.error(e)

class job:
    try:
        def batch(self):
            "Year of joining the batch"
            lg.info("2022")
        def job_type(self):
            for i in data:
                if i == "Data Science":
                    lg.info("I want to be a data scientist")
    except Exception as e:
        lg.error(e)

class feedback:
    try:
        def batch(self):
            lg.info("FSDS Bootcamp may 7 2022")
        def about_class(self):
            lg.info("Every classes are amazing and I able to learn new things.")
    except Exception as e:
        lg.error(e)

# Creating polymorphism of the 3 classes (internship, job and feedback)
def final_function(fun):
    fun.batch()

intern = internship()
j = job()
f = feedback()

final_function(intern)
final_function(j)
final_function(f)
