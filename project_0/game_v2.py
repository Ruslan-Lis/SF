'''The game predict a number
the computer self create and predict the number'''

import numpy as np

number = np.random.randint(1, 101) # create number


def random_predict(number:int=1) -> int:
    ''' random predict the number
    
    Args:
        number (int, optional): create the number. Defaults to 1.
        
    Returns:
        int: caunt of attempts
    '''
    
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) 
    
        if predict_number == number:
            # print(f'You predict the number! This number is {number}, {count} attempt')
            break
        
    return count

    
def score_game(random_predict) -> int:
    '''[summary]
    
    Args:
        random_predict ([type]): function prediction
        
    Returns:
        int: mean count of attempt
    '''
    count_ls = []
    np.random.seed(42)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'your algorifm gess the number in mean {score} attempts')
    return score
    

if __name__ == '__main__':
    score_game(random_predict)