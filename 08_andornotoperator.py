# Logical Operators = evaluates the multiple condition. There are AND, OR and NOT operator to do this task.


#OR Operator

score = 98
student_status= False

if score > 90 or student_status:
    print(' You are pass. ')
else:
    print('Study hard to get nice grade. ')

# AND operator

if score > 90 and student_status:
    print('Excellent Job')

else:
    print(' You need to work hard')

#Not operator

if not score > 90:
    print(' WORK better. ')
else:
    print('You are doing great job. ')