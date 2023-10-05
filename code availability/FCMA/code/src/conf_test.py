"""
#--------------------
Created on 2021.10.24
Version 1.0
__author__ = 'Xx'
#--------------------
"""
'''
Description:
        Routine for determining the level of confidence of a particular clear sky test. Input single threshold value 
        ('midpt') with associated confidence limits ('locut', 'hicut'). "Low" and "high" cutoffs refer to low or high 
        confidence ends of an interval and not necessarily to absolute value. Routine calculates the confidence based 
        on an "S" function. One may change the shape of the function by changing 'power' and/or 'midpt'. This version
        currently accepts only 1 set of limits to process.

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
# integer nmval
# real power,val,conflev,locut,hicut,midpt
# local scalars
# real alpha,gamma,range,coeff,s1,c,beta
# logical flipped
# -23.5, -22.0, -20.5

def conf_test(val, locut, hicut, power, midpt, nmval):
    coeff = 2.0**(power-1.0)  # 1
    # Check if testing a single threshold or a range of values.
    if nmval == 1:
        # Single threshold.
        ture = 'T'
        false = 'F'
        if hicut > locut:
            gamma = hicut            # 1.9
            alpha = locut            # 1.8
            flipped = 'F'
        else:
            gamma = locut
            alpha = hicut
            flipped = 'T'


        beta = midpt  # -22
        # Check for value beyond function range.
        if flipped == false and val > gamma:
            c = 1.0
        elif flipped == false and val < alpha:
            c = 0.0
        elif flipped == ture and val > gamma:
            c = 0.0
        elif flipped == ture and val < alpha:
            c = 1.0

        # Value is within the range of the function.
        if alpha <= val <= beta:
            range =2.0*(beta-alpha)
            s1 = (val-alpha)/range
            if flipped == false:
                c = coeff*(s1**power)
            if flipped == ture:
                c = 1.0-(coeff * (s1**power))
        if beta <= val <= gamma:
            range = 2.0 * (beta - gamma)
            s1 = (val - gamma) / range

            if flipped == false:
                c = 1.0 - (coeff * (s1**power))
            if flipped == ture:
                c = coeff * (s1**power)

    # Force confidence values to be between 0 and 1.
    if c > 1.0:
        c = 1.0
    if c < 0.0:
        c = 0.0
    conflev = c

    return conflev





