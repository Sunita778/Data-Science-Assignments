import logging
logging.basicConfig(filename="oops.log", level=logging.DEBUG, format='%(asctime)s %(message)s')

class String:
    def __init__(self, s):
        logging.info("**************************************************************************************")
        logging.info("**** These tasks are about string... ****\n")
        self.s = s

    def extract_data(self):
        try:
            logging.info("Q - Try to extract data from index one to index 300 with a jump of 3")
            logging.info(self.s[0:300:3])
        except Exception as e:
            logging.error( e)

    def reverse_str(self):
        try:
            logging.info("Q - Try to reverse a string without using reverse function")
            logging.info(self.s[::-1])
        except Exception as e:
            logging.error(e)

    def split_upper_str(self):
        try:
            logging.info("Q - Try to split a string after conversion of entire string in uppercase.")
            logging.info(self.s.upper().split(" "))
        except Exception as e:
            logging.error(e)

    def lower_str(self):
        try:
            logging.info("Q - Try to convert the whole string into lower case.")
            return self.s.lower()
        except Exception as e:
            logging.error(e)

    def capitalize_str(self):
        try:
            logging.info("Q - Try to capitalize the whole string.")
            return self.s.capitalize()
        except Exception as e:
            logging.error(e)

    def isalnum_and_isalpha(self,s1):
        try:
            logging.info("Q - Check the given str is alpha numeric or not")
            logging.info(s1.isalnum())
            logging.info("Q - Check the given string contain only alphabet or not")
            logging.info(s1.isalpha())
        except Exception as e:
            logging.error(e)

    def expand_tab_str(self, s1):
        try:
            logging.info("Q - Try to give an example of expand tab.")
            return s1.expandtabs()
        except Exception as e:
            logging.error(e)

    def strip_str(self, s1):
        try:
            logging.info("Q - Give an example of strip, lstrip and rstrip")
            logging.info("Removing white space from both side of string")
            logging.info(s1.strip())
            logging.info("Removing white space from left side of string")
            logging.info(s1.lstrip())
            logging.info("Removing white space from right side of string")
            logging.info(s1.rstrip())
        except Exception as e:
            logging.error(e)

    def replace_str(self,s1):
        try:
            logging.info("Q - Replace a string charecter by another charecter by taking your own example.")
            return s1.replace("sunita", "suni")
        except Exception as e:
            logging.error(e)

    def center_str(self, s1):
        try:
            logging.info("Q - Try  to give an example of string center function.")
            return s1.center(20, '-')
        except Exception as e:
            logging.error(e)


Given_str = String("this is My First Python programming class and i am learning python string and its function")
Given_str.extract_data()
Given_str.reverse_str()
Given_str.split_upper_str()
logging.info(Given_str.lower_str())
logging.info(Given_str.capitalize_str())
Given_str.isalnum_and_isalpha("ssu23")
logging.info(Given_str.expand_tab_str("class\tand\tobject"))
Given_str.strip_str("          suni        ")
logging.info(Given_str.replace_str("sunita"))
logging.info(Given_str.center_str("suni"))


class List:
    def __init__(self,l, l1):
        logging.info("\n")
        logging.info("**************************************************************************************")
        logging.info("**** These tasks are about list... ****\n")
        self.l =l
        self.l1 = l1

    def reverse_a_list(self):
        try:
            logging.info("Q - Try to reverse a list without using reverse funcion")
            return self.l[::-1]
        except Exception as e:
            logging.error(e)

    def access_data_from_list(self):
        try:
            logging.info("Q - try to access 456 from the list without using loop")
            return self.l[5][1]
        except Exception as e:
            logging.error(e)

    def access_data_from_list1(self):
        try:
            logging.info("Q - try to access 234 out of this list with out using loop")
            return self.l[7][0]
        except Exception as e:
            logging.error(e)

    def extract_list(self):
        try:
            logging.info("Q - Try to extract list collection form list l without using loop")
            logging.info("It's the 1st list from list l")
            logging.info(self.l[5])
            logging.info("It's the 2nd list from list l")
            logging.info(self.l[6])
            logging.info("It's the 3rd list from list l")
            logging.info(self.l[8][234])
        except Exception as e:
            logging.error(e)

    def extract_str(self):
        try:
            logging.info("Q - Try to extract 'sudh' from the list")
            return self.l[8]['key1']
        except Exception as e:
            logging.error(e)

    def key_value(self):
        try:
            logging.info("Q - Try to list separetly all the keys and values in dict element available in list")
            logging.info("Keys in dict element available in list are -")
            logging.info(self.l[8].keys())
            logging.info("Values in dict element available in list are -")
            logging.info(self.l[8].values())
        except Exception as e:
            logging.error(e)

    def ext_list(self):
        try:
            logging.info("Q - Try to extract all the list entity from the list")
            a = []
            for i in self.l1:
                if i is not a:
                    a.append(list(i))
            logging.info(list(a))
        except Exception as e:
            logging.error(e)

    def num_data_list(self):
        try:
            logging.info("Q - Try to extract all the numerical data it may be a part of dict key and values")
            a = []
            for i in self.l1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            a.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                a.append(g)
            logging.info(a)
        except Exception as e:
            logging.error(e)

    def sum_of_num_data(self):
        try:
            logging.info("Q - Try to give summation of all the numeric data")
            a = []
            for i in self.l1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            a.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                a.append(g)
            logging.info(sum(a))
        except Exception as e:
            logging.error(e)

    def odd_values_in_list(self):
        try:
            logging.info("Q - Try to filter out all the odd values out all numeric data which is a part of a list")
            a = []
            for i in self.l1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            a.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                a.append(g)
            for m in a:
                if m % 2 != 0:
                    logging.info(m)
        except Exception as e:
            logging.error(e)

    def extract_ineuron(self):
        try:
            logging.info("Q - Try to extract 'ineuron' out of this data")
            a = []
            for i in self.l1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == "ineuron":
                            a.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if g == "ineuron":
                                a.append(g)
            logging.info(a)
        except Exception as e:
            logging.error(e)

    def occurance_of_data(self):
        try:
            logging.info("Q - Try to find out the occurance of all the data")
            a = []
            for i in self.l1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            a.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int or type(g) == str:
                                a.append(g)
            for i in set(a):
                logging.info("{} : {}".format(i, a.count(i)))
        except Exception as e:
            logging.error(e)

    def find_str(self):
        try:
            logging.info("Q - Try to filter out all the string data")
            a = []
            for i in self.l1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            a.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == str:
                                a.append(g)
            logging.info(a)
        except Exception as e:
            logging.error(e)

    def check_isalnum(self):
        try:
            logging.info("Q - Try to find out the alphanum in data")
            a = []
            for i in self.l1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            a.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == str:
                                a.append(g)
            for i in a:
                if i.isalnum():
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    def mul_of_num_data(self):
        try:
            logging.info("Q - Try to find out multiplication of all the numeric value in the individual collection inside dataset")
            for i in self.l1:
                a = 1
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            a = a*j
                    logging.info("{} : {}".format(type(i), a))
                if type(i) == dict:
                    for k in i.items():
                        for h in k:
                            if type(h) == int:
                                a = a*h
                    logging.info("{} : {}".format(type(i), a))
        except Exception as e:
            logging.error(e)

    def flat_list(self):
        try:
            logging.info("Q - Try to unwrape all the collection inside the collection and creat a flat list.")
            a = []
            for i in self.l1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            a.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int or type(g) == str:
                                a.append(g)
            logging.info(a)
        except Exception as e:
            logging.error(e)

Given_list = List( [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}],
 [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':'sudh','k2':'ineuron','k3':'kumar',3:6,7:8},['ineuron','data science']])
logging.info(Given_list.reverse_a_list())
logging.info(Given_list.access_data_from_list())
logging.info(Given_list.access_data_from_list1())
Given_list.extract_list()
logging.info(Given_list.extract_str())
Given_list.key_value()
Given_list.ext_list()
Given_list.num_data_list()
Given_list.sum_of_num_data()
Given_list.odd_values_in_list()
Given_list.extract_ineuron()
Given_list.occurance_of_data()
Given_list.find_str()
Given_list.check_isalnum()
Given_list.mul_of_num_data()
Given_list.flat_list()

class Tuple:
    def __init__(self, l):
        self.l = l
        logging.info("\n")
        logging.info("**************************************************************************************")
        logging.info("**** This task is about tuple.... ****\n")

    def find_tuple_from_list(self):
        try:
            logging.info("Q -  Try to extract all the tuple entity from the given list")
            for i in self.l:
                if type(i) == tuple:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

LIST = Tuple([[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':'sudh','k2':'ineuron','k3':'kumar',3:6,7:8},['ineuron','data science']])
LIST.find_tuple_from_list()

class Dictionary:
    def __init__(self, l):
        self.l = l
        logging.info("\n")
        logging.info("**************************************************************************************")
        logging.info("**** These tasks are about dictionary element... ****\n")

    def find_dict_from_list(self):
        try:
            logging.info("Q - Try to extract all the dicttionay entity from the given list")
            for i in self.l:
                if type(i) == dict:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    def keys_in_dict(self):
        try:
            logging.info("Q - Try to find out no.of keys in dict element")
            for i in self.l:
                if type(i) == dict:
                    logging.info(len(i))
        except Exception as e:
            logging.error(e)

LIST = Dictionary([[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':'sudh','k2':'ineuron','k3':'kumar',3:6,7:8},['ineuron','data science']])
LIST.find_dict_from_list()
LIST.keys_in_dict()



