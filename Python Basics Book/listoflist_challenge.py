universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

# mean() function takes a single list as an argument and return the mean of
# the values in each list.
def get_mean(list):
    return sum(list)/len(list)

# median() function takes a single list as an argument and return the median of
# the values in each list.
def get_median(list):
    list.sort()
    # if it is an even number get the middle two values add them together and divide by 2
    if ((len(list))%2) == 0:
        return ((((list[int(len(list)/2)-1]) + (list[int(len(list)/2)]))/2))
    # other wise it is odd grab middle and return    
    else:
        return list[int(len(list)/2)]

#enrollment_stats(), that takes one input a list of
# lists where each individual list contains three elements: (a) the name
# of a university, (b) the total number of enrolled students, and (c) the
# annual tuition fees. returns two lists: the first containing all of
# the student enrollment values and the second containing all of the
# tuition fees.

def enrollment_stats(lol):
    s_enrollment_vals = [universities[i][1] for i in range(len(universities))]
    s_tuition_vals = [universities[i][2] for i in range(len(universities))]
    return s_enrollment_vals , s_tuition_vals

# Using universities, enrollment_stats(), mean(), and median(), calculate
# the total number of students, the total tuition, the mean and median
# of the number of students, and the mean and median tuition values.
# Finally, output all values, and format the output so that it looks like
# this:
# ******************************
# Total students: 77,285
# Total tuition: $ 271,905
# Student mean: 11,040.71
# Student median: 10,566
# Tuition mean: $ 38,843.57
# Tuition median: $ 39,849
# ******************************

enroll_vals , tuition_vals = enrollment_stats(universities)
print('******************************')  
print(f'Total student: {sum(enroll_vals):,}')
print(f'Total tuition: ${sum(tuition_vals):,}')
print(f'Student mean: {get_mean(enroll_vals):,.2f}')
print(f'Student median: {get_median(enroll_vals):,}')
print(f'Tuition mean: ${get_mean(tuition_vals):,.2f}')
print(f'Tuition median: ${get_median(tuition_vals):,}')
print('******************************') 