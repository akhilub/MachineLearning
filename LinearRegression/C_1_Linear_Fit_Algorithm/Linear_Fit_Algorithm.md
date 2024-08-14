**[PlayGround](https://platform.stratascratch.com/algorithms/10432-linear-fit-algorithm?code_type=1)**


Linear Fit Algorithm


Microsoft   Medium    ID-10432


Data Scientist  ML Engineer   Software Engineer


Write an algorithm that linearly fits given inputs and outputs the slope and intercept of the linear function.

Constraints

- The input variable inputs must be a list of floats.


Test Case #1
```
Input: [10.5, 35.3, 19.0, 47.8, 25.0, 8.1]
Output: [0.014922492023865272, 2.52397977410287]
Description: This test case involves a list with varied floating-point numbers to check that the algorithm can accurately compute the slope and intercept.
```

Test Case #2
```
Input: [5.0, 2.3, 7.8, 1.0, 4.4, 8.2, 0.6]
Output: [-0.048765432098765465, 3.9398765432098775]
Description: This test includes a mixture of small floating-point numbers, ensuring the algorithm can handle minimal values and calculate the correct linear fit parameters.
```


Test Case #3
```
Input: [3.1415, 2.7182, 1.4142, 1.732, 0.5772, 2.6854]
Output: [-0.23073486216466155, 3.059508924169337]
Description: This test case checks the function with irrational numbers to ensure it can process complex floating-point numbers without numerical instability or precision loss.
```


## Solution


This algorithm calculates the slope and intercept using the formulas:

Slope (m) = (n * Σxy - Σx * Σy) / (n * Σx^2 - (Σx)^2)

Intercept (c) = (Σy - m * Σx) / n

Where:
- n is the number of inputs
- Σx is the sum of the inputs
- Σx^2 is the sum of the squared inputs
- Σxy is the sum of the product of inputs and their indices
- Σy is the sum of the indices