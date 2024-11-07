#Linear fit Algorithm
def linear_fit(inputs):
    """
    :type inputs: List[float]
    :rtype: Tuple[float, float]
    """    
    n = len(inputs)
    sum_x = sum(inputs)
    sum_y = sum(range(n))
    sum_x_squared = sum(x**2 for x in inputs)
    sum_xy = sum(inputs[i]*i for i in range(n))
    
    slope = (n*sum_xy - sum_x*sum_y)/(n*sum_x_squared - sum_x**2)
    
    intercept = (sum_y -slope*sum_x)/n
    
    return slope,intercept

# Test cases
print(linear_fit([10.5, 35.3, 19.0, 47.8, 25.0, 8.1]))
print(linear_fit([5.0, 2.3, 7.8, 1.0, 4.4, 8.2, 0.6]))
print(linear_fit([3.1415, 2.7182, 1.4142, 1.732, 0.5772, 2.6854]))




#Accepted ans in this format

from typing import List, Tuple
from decimal import Decimal
def linear_fit(inputs: List[float]) -> Tuple[float, float]:
    """
    :type inputs: List[float]
    :rtype: Tuple[float, float]
    """
    n = Decimal(len(inputs))
    sum_x = sum(Decimal(x) for x in inputs)
    sum_y = sum(Decimal(i) for i in range(len(inputs)))
    sum_x_squared = sum(Decimal(x)**2 for x in inputs)
    sum_xy = sum(Decimal(inputs[i])*i for i in range(len(inputs)))
    
    slope = (n *sum_xy - sum_x*sum_y) / (n*sum_x_squared -sum_x**2 )
    
    intercept = (sum_y - slope*sum_x)/n
    
    return float(slope) , float(intercept)

# Test cases
print(linear_fit([10.5, 35.3, 19.0, 47.8, 25.0, 8.1]))
print(linear_fit([5.0, 2.3, 7.8, 1.0, 4.4, 8.2, 0.6]))
print(linear_fit([3.1415, 2.7182, 1.4142, 1.732, 0.5772, 2.6854]))