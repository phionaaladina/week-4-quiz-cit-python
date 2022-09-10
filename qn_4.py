'''
Write a python program to input 5 subject marks and 
calculate total marks, percentage and grade based on following criteria
percentage less than 50 (Grade C)
percentage equal to 50 and less than 80 (Grade B)
percentage equal to 80 and more than 80 (Grade A)
'''
def marks(mark_1,mark_2,mark_3,mark_4,mark_5):
    total_marks = mark_1+mark_2+mark_3+ mark_4+ mark_5
    print('total_marks: ' + str(total_marks))
    percentage = total_marks/500 *100
    print('percentage: ' + str(percentage) + '%')

    #percentage = 0
    if percentage >=80:
        print('Grade A')
    elif percentage < 80:
        print('Grade B')
    elif percentage < 50 :
        print('Grade C')
    else:
        print('Invalid input')

marks(50,96,78,67,90)