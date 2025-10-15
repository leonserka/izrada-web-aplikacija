#!python.exe
from http import cookies
import os

# Podaci o predmetima
subjects = {
    'ip' : { 'name' : 'Introduction' , 'year' : 1, 'ects' : 6 },
    'c1' : { 'name' : 'Calculus1' , 'year' : 1, 'ects' : 7 },
    'cu' : { 'name' : 'Computerusage' , 'year' : 1, 'ects' : 5 },
    'dmt' : { 'name' : 'Digitalandmicroprocessortechnology', 'year' : 1, 'ects' : 6 },
    'db' : { 'name' : 'Databases' , 'year' : 2, 'ects' : 6 },
    'c2' : { 'name' : 'Calculus2' , 'year' : 2, 'ects' : 7 },
    'dsa' : { 'name' : 'Datastructuresandalghoritms' , 'year' : 2, 'ects' : 5 },
    'ca' : { 'name' : 'Computerarchitecture', 'year' : 2, 'ects' : 6 },
    'isd' : { 'name' : 'Informationsystemsdesign' , 'year' : 3, 'ects' : 5 },
    'c3' : { 'name' : 'Calculus3' , 'year' : 3, 'ects' : 7 },
    'sa' : { 'name' : 'ServerArchitecture' , 'year' : 3, 'ects' : 6 },
    'cds' : { 'name' : 'Computeranddatasecurity', 'year' : 3, 'ects' : 6 }
}

year_names = {
    1 : '1st Year',
    2 : '2nd Year',
    3 : '3rd Year'
}

year_ids = {
    '1st Year' : 1,
    '2nd Year' : 2,
    '3rd Year' : 3
}

status_names = {
    'not' : 'Not Selected',
    'enr' : 'Enrolled',
    'pass' : 'Passed',
}

