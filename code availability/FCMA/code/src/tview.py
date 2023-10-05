"""
#--------------------
Created on 2021.11.04
Version 1.0
__author__ = 'Xx'
#--------------------
"""
'''
Description:
            subroutine which computes the bi-dimensional linear or quadratic interpolation (lagrange form) of 
            a given value to a table of scan angle and 11um brightness temperature dependent 11-12 micron 
            brightness temperature differences.  These values were taken from APOLLO.

Input Parameters:
key      linear (1) or quadratic (2) interpolation
         线性（1）或二次（2）插值               
xmu      secant of the viewing zenith angle
         观察天顶角的正割
bt11     pixel 11 micron brightness temperature
         像素11微米亮温
        
Output Parameters:
corr     computed 11-12 micron BTDIF threshold for thin cirrus detection
         薄卷云探测的计算11-12微米BTDIF阈值
'''
import numpy as np

def tview(key, xmu, bt11):

    utab = [2.00, 1.75, 1.5, 1.25, 1.00]
    ttab = [190., 200., 210., 220., 230., 240., 250., 260., 270., 280., 290., 300., 310.]
    tab0 = [0.559, 0.424, 0.286, 0.137, 0.123, 0.198, 0.333, 0.696, 1.217, 3.184, 5.178, 8.269, 12.452]
    tab1 = [0.542, 0.416, 0.294, 0.162, 0.156, 0.240, 0.366, 0.704, 1.184, 2.926, 4.854, 7.885, 11.985]
    tab2 = [0.520, 0.405, 0.305, 0.194, 0.199, 0.294, 0.409, 0.715, 1.141, 2.591, 4.433, 7.389, 11.381]
    tab3 = [0.491, 0.391, 0.319, 0.238, 0.257, 0.367, 0.467, 0.729, 1.083, 2.140, 3.866, 6.720, 10.567]
    tab4 = [0.450, 0.370, 0.340, 0.300, 0.340, 0.470, 0.550, 0.750, 1.000, 1.500, 3.060, 5.770, 9.410]
    tab = [tab0, tab1, tab2, tab3, tab4]
    tab = np.array(tab)
    # tab[:, 0] = [0.559, 0.542, 0.520, 0.491, 0.450]
    # tab[:, 1] = [0.424, 0.416, 0.405, 0.391, 0.370]
    # tab[:, 2] = [0.286, 0.294, 0.305, 0.319, 0.340]
    # tab[:, 3] = [0.137, 0.162, 0.194, 0.238, 0.300]
    # tab[:, 4] = [0.123, 0.156, 0.199, 0.257, 0.340]
    # tab[:, 5] = [0.198, 0.240, 0.294, 0.367, 0.470]
    # tab[:, 6] = [0.333, 0.366, 0.409, 0.467, 0.550]
    # tab[:, 7] = [0.696, 0.704, 0.715, 0.729, 0.750]
    # tab[:, 8] = [1.217, 1.184, 1.141, 1.083, 1.000]
    # tab[:, 9] = [3.184, 2.926, 2.591, 2.140, 1.500]
    # tab[:, 10] = [5.178, 4.854, 4.433, 3.866, 3.060]
    # tab[:, 11] = [8.269, 7.885, 7.389, 6.720, 5.770]
    # tab[:, 12] = [12.452, 11.985, 11.381, 10.567, 9.410]

    # bounds check
    u = xmu
    t = bt11
    if u >= utab[0]:
        u = utab[0]
    if u <= utab[4]:
        u = utab[4]

    if t <= ttab[0]:
        t = ttab[0]
    if t >= ttab[12]:
        t = ttab[12]

    '=============================================================================='
    Iflag = 0
    for i in range(1, 5):
        ii = i
        if u >= utab[i] and Iflag == 0:
            Iflag = 1
            if key == 1:
                i0 = ii-1
                i1 = ii
            else:
                if ii == 4:
                    i0 = ii-2
                    i1 = ii-1
                    i2 = ii
                else:
                    i0 = ii-1
                    i1 = ii
                    i2 = ii+1

    '=============================================================================='
    # Iflag = 0
    for j in range(1, 13):
        Iflag = 0
        jj = j
        if t <= ttab[j] and Iflag == 0:
            Iflag = 1
            if key == 1:
                j0 = jj-1
                j1 = jj
            else:
                if jj == 12:
                    j0 = jj-2
                    j1 = jj-1
                    j2 = jj
                else:
                    j0 = jj-1
                    j1 = jj
                    j2 = jj+1


    # branch on scheme type.
    if key == 1:
        # linear scheme
        # designate index values
        u0 = utab[i0]
        u1 = utab[i1]
        t0 = ttab[j0]
        t1 = ttab[j1]

        # lagrange polynomials
        lu0 = (u - u1) / (u0 - u1)
        lu1 = (u - u0) / (u1 - u0)
        lt0 = (t - t1) / (t0 - t1)
        lt1 = (t - t0) / (t1 - t0)

        # interpolating polynomials for the first dimension
        p0 = tab[i0, j0] * lu0 + tab[i1, j0] * lu1
        p1 = tab[i0, j1] * lu0 + tab[i1, j1] * lu1
        # interpolating polynomial for second dimension
        corr = p0 * lt0 + p1 * lt1
    else:
        # quadratic scheme designate index values
        u0 = utab[i0]
        u1 = utab[i1]
        u2 = utab[i2]
        t0 = ttab[j0]
        t1 = ttab[j1]
        t2 = ttab[j2]
        # lagrange polynomials
        lu0 = (u - u1)*(u - u2)/(u0 - u1)/(u0 - u2)
        lu1 = (u - u0)*(u - u2)/(u1 - u0)/(u1 - u2)
        lu2 = (u - u0)*(u - u1)/(u2 - u0)/(u2 - u1)
        lt0 = (t - t1)*(t - t2)/(t0 - t1)/(t0 - t2)
        lt1 = (t - t0)*(t - t2)/(t1 - t0)/(t1 - t2)
        lt2 = (t - t0)*(t - t1)/(t2 - t0)/(t2 - t1)
        # interpolating polynomials for the first dimension
        p0 = tab[i0, j0]*lu0 + tab[i1, j0]*lu1 + tab[i2, j0]*lu2
        p1 = tab[i0, j1]*lu0 + tab[i1, j1]*lu1 + tab[i2, j1]*lu2
        p2 = tab[i0, j2]*lu0 + tab[i1, j2]*lu1 + tab[i2, j2]*lu2
        # interpolating polynomial for second dimension
        corr = p0*lt0 + p1*lt1 + p2*lt2

    return corr

