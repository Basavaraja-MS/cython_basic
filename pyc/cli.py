from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Validator, ValidationError
from pprint import pprint
from pcie_log import *
from difflib import SequenceMatcher
import common as main

class NumberValidator(Validator):
     def validate(self, document):
         try:
             int(document.text)
         except ValueError:
             raise ValidationError(
                 message='Please enter a number',
                 cursor_position=len(document.text))  # Move cursor to end

"""
questions = [
     {
          'type': 'input',
          'name': 'rpbus',
          'message': 'Enter RP bus number:',
          'validate': NumberValidator,
          'filter': lambda val: int(val),
          'default': '0'

      },

     {
          'type': 'input',
          'name': 'rpdev',
          'message': 'Enter RP device number:',
          'validate': NumberValidator,
          'filter': lambda val: int(val)
      },
     {
          'type': 'input',
          'name': 'rpfun',
          'message': 'Enter RP function number:',
          'validate': NumberValidator,
          'filter': lambda val: int(val)
      },
     {
          'type': 'input',
          'name': 'epbus',
          'message': 'Enter EP bus number:',
          'validate': NumberValidator,
          'filter': lambda val: int(val)
      },
     {
          'type': 'input',
          'name': 'epdev',
          'message': 'Enter EP dev number:',
          'validate': NumberValidator,
          'filter': lambda val: int(val)
      },
     {
          'type': 'input',
          'name': 'epfun',
          'message': 'Enter EP function number:',
          'validate': NumberValidator,
          'filter': lambda val: int(val)
      },
    {
        'type': 'list',
        'name': 'testname',
        'message': 'Select test:',
        'choices': ['All',
                    'PCI power managment test',
                    'ASPM test',
                    'Link Equ test',
                    'Link Retrain test',
                    'Link Disable/Enable test',
                    'Link Speed test'
                    ],
    },
    {
         'type': 'input',
         'name': 'testcount',
         'message': 'Enter test iteration count:',
         'validate': NumberValidator,
         'filter': lambda val: int(val)
     },
     {
         'type': 'confirm',
         'name': 'aer',
         'message': 'Enable AER?',
         'default': False
     },
     {
         'type': 'list',
         'name': 'loglevel',
         'message': 'Log Level',
         'choices': ['Error', 'Warning', 'Info', 'Debug'],
         'filter': lambda val: val.lower()
     },


     {
         'type': 'input',
         'name': 'debugfile',
         'message': 'Log file name',
         'default': 'testlog.txt'
     },


]
"""

questions = [
     {
          'type': 'input',
          'name': 'rpbus',
          'message': 'Enter RP bus number:',
          'validate': NumberValidator,
          'filter': lambda val: int(val),
          'default': '0'
      },

     {
          'type': 'input',
          'name': 'rpdev',
          'message': 'Enter RP device number:',
          'validate': NumberValidator,
          'filter': lambda val: int(val),
          'default': '1'
      },
     {
          'type': 'input',
          'name': 'rpfun',
          'message': 'Enter RP function number:',
          'validate': NumberValidator,
          'filter': lambda val: int(val),
          'default': '1'
      },
     {
          'type': 'input',
          'name': 'epbus',
          'message': 'Enter EP bus number:',
          'validate': NumberValidator,
          'filter': lambda val: int(val),
          'default': '2'
      },
     {
          'type': 'input',
          'name': 'epdev',
          'message': 'Enter EP dev number:',
          'validate': NumberValidator,
          'filter': lambda val: int(val),
          'default': '0'
      },
     {
          'type': 'input',
          'name': 'epfun',
          'message': 'Enter EP function number:',
          'validate': NumberValidator,
          'filter': lambda val: int(val),
          'default': '0'
      },
    {
        'type': 'list',
        'name': 'testname',
        'message': 'Select test:',
        'choices': ['All',
                    'PCI power managment test',
                    'ASPM test',
                    'Link Equ test',
                    'Link Retrain test',
                    'Link Disable/Enable test',
                    'Link Speed test'
                    ],

    },
    {
         'type': 'input',
         'name': 'testcount',
         'message': 'Enter test iteration count:',
         'validate': NumberValidator,
         'filter': lambda val: int(val),
         'default': '10'
     },
     {
         'type': 'confirm',
         'name': 'aer',
         'message': 'Enable AER?',
         'default': False
     },
     {
         'type': 'list',
         'name': 'loglevel',
         'message': 'Log Level',
         'choices': ['Error', 'Warning', 'Info', 'Debug'],
         'filter': lambda val: val.lower()
     },


     {
         'type': 'input',
         'name': 'debugfile',
         'message': 'Log file name',
         'default': 'testlog.txt'
     },


]

def ispcipmtest(answer):
    answer1 = 'PCI power managment test'
    if SequenceMatcher(None, answer, answer1).ratio() == 1.0:
        return True
    return False

def isaspmtest(answer):
    answer1 = 'ASPM test'
    if SequenceMatcher(None, answer, answer1).ratio() == 1.0:
        return True
    return False

def islinkrettest(answer):
    answer1 = 'Link Retrain test'
    if SequenceMatcher(None, answer, answer1).ratio() == 1.0:
        return True
    return False

def islinkdisabletest(answer):
    answer1 = 'Link Disable/Enable test'
    if SequenceMatcher(None, answer, answer1).ratio() == 1.0:
        return True
    return False

def islinkequtest(answer):
    answer1 = 'Link Equ test'
    if SequenceMatcher(None, answer, answer1).ratio() == 1.0:
        return True
    return False

def islinkspeedtest(answer):
    answer1 = 'Link Speed test'
    if SequenceMatcher(None, answer, answer1).ratio() == 1.0:
        return True
    return False

def isalltest(answer):
    answer1 = 'All'
    if SequenceMatcher(None, answer, answer1).ratio() == 1.0:
        return True
    return False

def get_log_level(answer):
    if answer == 'Debug':
        return 10
    elif answer == 'Info':
        return 20
    elif answer == 'Warnning':
        return 30
    elif answer == 'Error':
        return 40
    else:
        return 10

def check_test_parm(param):
    print(param["busrp"])
    print(param["devrp"])
    print(param["funrp"])
    print(param["pcipm_test"])
    print(param["aspm_test"])
    print(param["link_ret_test"])
    print(param["link_disable_test"])
    print(param["link_equ_test"])
    print(param["link_speed_test"])
    print(param["all_test"])
    print(param["aer_chk"])

if __name__ == "__main__":
    answers = prompt(questions)

    #logging.basicConfig(filename=answers["debugfile"], level=get_log_level(answers['loglevel']), format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #logging.basicConfig(filename="file.txt", level=get_log_level(answers['loglevel']), format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.basicConfig(filename="file.txt", level=10, format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logging.info("RP BUS:%s DEV:%s FUN :%s",
            answers['rpbus'], answers['rpdev'], answers['rpfun'])
    logging.info("EP BUS:%s DEV:%s FUN :%s",
            answers['epbus'], answers['epdev'], answers['epfun'])
    logging.info("Test Name: %s", answers['testname'])
    logging.info("Test Count: %s", answers['testcount'])
    logging.info("AER Enable: %s", answers['aer'])
    logging.info("Logging Leve: %s", answers['loglevel'])
    logging.info("Logging File: %s", answers['debugfile'])

    #fill the test parameters
    test_param_dict = {
            "segrp": 0,
            "busrp": answers['rpbus'],
            "devrp": answers['rpdev'],
            "funrp": answers['rpfun'],

            "segep": 0,
            "busep": answers['epbus'],
            "devep": answers['epdev'],
            "funep": answers['epfun'],


            "pcipm_test": ispcipmtest(answers['testname']),
            "pcipm_test_count": answers['testcount'],

            "aspm_test": isaspmtest(answers['testname']),
            "aspm_test_count": answers['testcount'],

            "link_ret_test": islinkrettest(answers['testname']),
            "link_ret_test_count": answers['testcount'],

            "link_disable_test": islinkdisabletest(answers['testname']),
            "link_disable_test_count": answers['testcount'],

            "link_equ_test": islinkequtest(answers['testname']),
            "link_equ_test_count": answers['testcount'],

            "link_speed_test": islinkspeedtest(answers['testname']),
            "link_speed_test_count": answers['testcount'],

            "all_test": isalltest(answers['testname']),
            "all_test_count": answers['testcount'],

            "aer_chk": answers['aer'],
            "dll_active_chk": True,
            "print_only": False,

            "d1": True,
            "d2": True,

            "id": True,

            "max_aspm": 1,
     }

    #check_test_parm(test_param_dict)
    main.main_test_fun(test_param_dict)
