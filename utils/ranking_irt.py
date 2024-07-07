import numpy as np
from girth import twopl_mml

def irt_ranking(data, models):
    '''
    This function ranks the models based on their scores calculated using the 2PL model.

    :param data: A 2D numpy array where each row represents a model and each column represents a question.
                data[i][j] = 1 if question i is answered by model j correctly, 0 otherwise.
    :param models: A list of strings where each string represents a model.
    '''
    
    result = twopl_mml(data)
    discrimination = result['Discrimination']
    difficulty = result['Difficulty']

    # Use min-max function to normalize the difficulties
    # If we just shift the data, the distribution will change and give wrong results.
    min_difficulty = np.min(difficulty)
    max_difficulty = np.max(difficulty)
    normalized_difficulties = (difficulty - min_difficulty) / (max_difficulty - min_difficulty)

    model_scores = []
    for j in range(len(models)):
        score = 0
        for i in range(len(data)):
            score += data[i][j] * normalized_difficulties[i]
        model_scores.append((models[j], score))

    # Return the ranking of the models based on their scores.
    return sorted(model_scores, key=lambda x: x[1], reverse=True)
