

def num_to_digit(num):
    alpha_l = ['Zero', 'One', 'Two', 'Three', 'Four',
               'Five', 'Six', 'Seven', 'Eight', 'Nine']
    if 0 > num <= 9:
        return alpha_l[num]
    else:
        return 'invalid input'


num = int('Enter the num between 0 to 9 :- ')
print(num_to_digit(num))
