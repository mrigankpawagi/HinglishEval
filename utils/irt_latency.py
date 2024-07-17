import numpy as np
from scipy.optimize import minimize
from girth import twopl_mml

def irt_ranking(data : list, models : list) -> list:
    '''
    This function calculates the difficulty and the discrimination parameters of the models using the 2 parameter marginal likelihood model.
    :param data: A 2D numpy array where each row represents a model and each column represents a question.
                data[i][j] = 1 if question i is answered by model j correctly, 0 otherwise.
    :param models: A list of strings where each string represents a model in the same order as is present in the data.
    '''
    
    result = twopl_mml(data)
    discrimination = result['Discrimination']
    difficulty = result['Difficulty']
    return discrimination, difficulty

def two_parameter_logistic_model(theta, a, b):
    """
    A helper function to calculate the probability of a correct response using the 2PL model.
    :param theta: The latent ability of the student. (which is to be updated)
    :param a: The discrimination parameter of the model.
    :param b: The difficulty parameter of the model.
    """
    return 1 / (1 + np.exp(-a * (theta - b)))

def negative_log_likelihood(theta, responses, a_params, b_params):
    """
    A helper function to calculate the negative log likelihood, used for the updation of latency(theta) values in the IRT model.
    :param theta: The latent ability of the student. (which is to be updated)
    :param responses: A list of binary responses from the student.
    :param a_params: A list of discrimination parameters of the models.
    :param b_params: A list of difficulty parameters of the models.
    """
    log_likelihood = 0
    for i in range(len(responses)):
        prob_correct = two_parameter_logistic_model(theta, a_params[i], b_params[i])
        log_likelihood += responses[i] * np.log(prob_correct) + (1 - responses[i]) * np.log(1 - prob_correct)
    return -log_likelihood

def estimate_theta(responses, a_params, b_params):
    """
    Updates the theta estimation from an initial value using the negative log likelihood function and the difficulties and discrimination parameters obtained from the 2PL model.
    :param responses: A list of binary responses from the student.
    :param a_params: A list of discrimination parameters of the models.
    :param b_params: A list of difficulty parameters of the models.
    """
    initial_guess = 0.0  # Initial guess for theta
    result = minimize(negative_log_likelihood, initial_guess, args=(responses, a_params, b_params))
    return result.x[0]