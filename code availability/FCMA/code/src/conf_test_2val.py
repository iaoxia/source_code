"""
#--------------------
Created on 2021.11.05
Version 1.0
__author__ = 'Xx'
#--------------------
"""
'''
Description:
            Routine for determining the level of confidence of a particular clear sky test. Input two threshold values 
            ('midpt') with associated confidence limits ('locut', 'hicut') which define a range of values for a test.  
            "Low" and "high" cutoffs refer to low or high confidence ends of an interval and not necessarily to absolute 
            value. Routine calculates the confidence based on an "S" function. One may change the shape of the function 
            by changing 'power' and/or 'midpt'. This version accepts 2 threshold values.

Input Parameters:
val      current individual test value.
         当前单个测试值
locut    low confidence cutoff value (less then this is 0 conf.).
         最小置信值
hicut    high confidence cutoff value (greather than this is 100% conf.).
         最大置信值
power    S function curve power
midpt    midpoint of S curve (currently 50% - test straight threshold)
nmval    1 or 2 threshold values for this test?

Output Parameters:
conflev  calculated confidence that fov is unobstructed for this test.
         无遮挡视野置信值
'''
def conf_test_2val(val, locut, hicut, power, midpt, nmval):
    coeff = 2.0 ** (power - 1.0)
    # Check if testing a single threshold or a range of values.
    if nmval == 2:
        gamma1 = hicut[0]
        gamma2 = hicut[1]
        alpha1 = locut[0]
        alpha2 = locut[1]
        beta1 = midpt[0]
        beta2 = midpt[1]
        # Find if interval between inner cutoffs passes test or fails.
        if (alpha1 - gamma1) > 0.0:
            # Inner region fails test.
            # Check for value beyond function range.
            if val > alpha1 and val < alpha2:
                c = 0.0
            elif val < gamma1 or val > gamma2:
                c = 1.0
            elif val <= alpha1:
                # Value is within range of lower set of limits.
                if val >= beta1:
                    range = 2*(beta1-alpha1)
                    s1 = (val-alpha1)/range
                    c = coeff*s1**power
                else:
                    range = 2*(beta1-gamma1)
                    s1 = abs(val-gamma1)/range
                    c = 1-coeff*s1**power
            else:
                # Value is within range of upper set of limits.
                if val <= beta2:
                    range = 2.0 * (beta2 - alpha2)
                    s1 = (val - alpha2) / range
                    c = coeff * s1 ** power
                else:
                    range = 2.0 * (beta2 - gamma2)
                    s1 = (val - gamma2) / range
                    c = 1.0 - (coeff * s1 ** power)

        else:
            # Inner region passes test.
            # Check for value beyond function range.
            if val > gamma1 and val < gamma2:
               c = 1.0
            elif val < alpha1 or val > alpha2:
               c = 0.0
            elif val <= gamma1:
                # Value is within range of lower set of limits.
                if val <= beta1:
                    range = 2.0 * (beta1 - alpha1)
                    s1 = (val - alpha1) / range
                    c = coeff * s1 ** power
                else:
                    range = abs(2.0 * (beta1 - gamma1))
                    s1 = abs((val - gamma1) / range)
                    c = 1.0 - (coeff * s1 ** power)
            else:
                # Value is within range of upper set of limits.
                if val >= beta2:
                    range = 2.0 * (beta2 - alpha2)
                    s1 = (val - alpha2) / range
                    c = coeff * s1 ** power
                else:
                    range = 2.0 * (beta2 - gamma2)
                    s1 = (val - gamma2) / range
                    c = 1.0 - (coeff * s1 ** power)

    # Force confidence values to be between 0 and 1.
    if c > 1.0:
        c = 1.0
    if c < 0.0:
        c = 0.0
    conflev = c

    return conflev
