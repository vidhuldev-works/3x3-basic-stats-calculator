import numpy as np

def calculate(input_list):
    """this functions performs on python lists and make them into 3x3 numpy array matrix and perform some calculations
    on it, then results it.
    """

    #creating and reshaping list to numpy array 3x3 matrix
    arr=np.array(input_list).reshape(3,3)

    #finding mean values of each axis and 1d array
    mean_axis0=np.mean(arr, axis=0).tolist()
    mean_axis1=np.mean(arr, axis=1).tolist()
    mean_1d=arr.flatten().mean().tolist()

    #finding variance values of each axis and 1d array
    variance_axis0=np.var(arr, axis=0).tolist()
    variance_axis1=np.var(arr, axis=1).tolist()
    variance_1d=arr.flatten().var().tolist()

    #finding standard deviation values of each axis and 1d array
    standard_deviation_axis0=np.std(arr, axis=0).tolist()
    standard_deviation_axis1=np.std(arr, axis=1).tolist()
    standard_deviation_1d=arr.flatten().std().tolist()

    #finding maximum values of each axis and 1d array
    maximum_value_axis0=np.max(arr, axis=0).tolist()
    maximum_value_axis1=np.max(arr, axis=1).tolist()
    maximum_value_1d=arr.flatten().max().tolist()

    #finding minimum values of each axis and 1d array
    minimum_value_axis0=np.min(arr, axis=0).tolist()
    minimum_value_axis1=np.min(arr, axis=1).tolist()
    minimum_value_1d=arr.flatten().min().tolist()

    #finding sum values of each axis and 1d array
    sum_value_axis0=np.sum(arr, axis=0).tolist()
    sum_value_axis1=np.sum(arr, axis=1).tolist()
    sum_value_1d=arr.flatten().sum().tolist()

    #converting that calculation into dictionary
    calculations = {
        'mean': [mean_axis0, mean_axis1, mean_1d],
        'variance': [variance_axis0, variance_axis1, variance_1d],
        'standard deviation': [standard_deviation_axis0, standard_deviation_axis1, standard_deviation_1d],
        'max': [maximum_value_axis0, maximum_value_axis1, maximum_value_1d],
        'min': [minimum_value_axis0, minimum_value_axis1, minimum_value_1d],
        'sum': [sum_value_axis0, sum_value_axis1, sum_value_1d],
    }

    #making the output should print like dictionary in each different values of as key,value pairs
    output = "{\n"
    for key, value in calculations.items():
        output += f"  '{key}': {value},\n"
    output = output.rstrip(',\n') + "\n}"

    return output #returning the output

try:
    #getting user input elements and converting it into lists
    user_input=input("Enter the elements seperated by spaces: ")
    input_list=list(map(int, user_input.split()))

    #checking of list contains exact 9 elements and popup error if has
    if len(input_list) !=9:
        raise ValueError("The input list must contain exactly 9 elements.")

    #calling function and returning result
    result=calculate(input_list)
    print(result)

#handling exception or error
except ValueError as e:
    print("Error Occured:", e)