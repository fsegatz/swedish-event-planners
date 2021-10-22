#Description 
#"A SeniorCustomerServiceOfficer and a FinacialManager should be able to review 
# an event request through a form (similar to the event request form, but only 
# with the option to edit the feasibility_review resp. financial_review attribute"

# Needed to import rom parent directory
import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from main import main


main()


