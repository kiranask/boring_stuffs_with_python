import matplotlib.pyplot as plt
import numpy

bug_id = numpy.array([37, 9, 8, 9])

def absolute_value(val):
    a  = numpy.round(val/100.*bug_id.sum(), 0)
    return int(a)
bug_status = ['Verified/Closed Bugs ', 'New Bugs',' Re-opened Bugs', 'Duplicate Bugs']
colors = ['g', 'r','b','c']
plt.pie(bug_id, labels=bug_status, colors=colors, startangle=90, autopct=absolute_value)
plt.title('NAPP-10650 JS/HTML5 4.20 Bug Report')
plt.show()