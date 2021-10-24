#Description 
#"A CustomerServiceOfficer should be able to create a new event request through a form."

# Needed to import from parent directory
import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from main import main

#If the user is able to sucsessfully create a Event request through a form the test is a cleared
main()


