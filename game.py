'''predict number'''

import numpy as np

number = np.random.randint(1, 101) # create number

count = 0

while True:
    count += 1
    predict_number = int(input('Predict number from 1 to 100 '))
    
    if predict_number > number:
        print("The number must be less!")
        
    elif predict_number < number:
        print("The number must be greater!")
        
    else:
        print(f'You predict the number! This number is {number}, {count} attempt')
        break