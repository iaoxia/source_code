"""
#--------------------
Created on 2021.10.28
Version 1.0
__author__ = 'Xx'
#--------------------
"""
import math
from conf_test import conf_test
from tview import tview
'''
Description:
         Routine for performing clear sky tests over land surfaces during daylight hours.
         For daytime land the groups are:
              Group 1: High thick cloud，高厚云
                       13.9 micron bt test (masir13) 
                       6.75 micron bt test 
        
              Group 2: Low cloud - thick
                       11-12 micron bt tests
                       11- 4 micron bt tests
            
              Group 3: Thick cloud， 厚云
                       .66 micron reflectance test (masv66)
                       .87/.66 micron reflectance ratio test(masv88)
        

Input Parameters:
pxldat        Array containing reflectance or brightness temperatures for all bands for a single pixel.
              单个像素点所有波段的反射率和亮温
vza           Viewing zenith angle for current pixel.
              当前像素点的天顶角
visusd        Logical variable indicating whether vis data used or not.
              用来表明是否使用vis数据的逻辑变量
              
# cirrus_vis 	Logical variable flagging thin cirrus contaminated  scenes in the visible.
#               用来标注薄卷云影响可见光的逻辑变量
# hi_elev       Logical variable indicating high elevation (> 2000 meters).
#               用来表明高海拔的逻辑变量

Output Parameters:
# testbits      six byte integer containing bit results.
#               包含bit结果的六字节整数
# qa_bits       ten byte integer containing qa bit results.
#               包含qa bit结果的十字节整数
# nmtests       Counts number of inidividual tests applied.
#               单独测试次数

confdnc       product of all applied individual confidences.
              所有置信度的乘积
'''


def land(a0064, a0086, a0390, a0700, a1120, a1230, vza,
         dlh20, dl11_12hi, dl11_4lo, dlref1, dlvrat):
    # initialize variables
    visusd = 'true'
    vrused = 'true'  # 这两个逻辑变量需要商榷

    pi = math.acos(-1.0)
    dtr = pi/180.0
    nmtests = 0  # counts the number of tests applied to this pixel
    nptests = 0  # counts the number of tests passed
    ngtests = 0  # initialize group number.
    confdnc = 1.0  # set confidence to 1.0 to begin with
    # dlh20 = [215.0, 220.0, 225.0, 1.0]
    # dl11_12hi = 3.0
    # dl11_4lo = [-14.0, -12.0, -10.0, 1.0]
    # dlref1 = [0.24, 0.20, 0.16, 1.0]
    # dlvrat = [1.80, 1.85, 1.90, 1.0]
    masv66 = a0064   # 1
    masv88 = a0086   # 2
    masir4 = a0390   # 22
    masir65 = a0700  # 27  实际是6.715
    masir11 = a1120  # 31
    masir12 = a1230  # 32

    # masv66 = pxldat(1)     ---0.659   ***0064
    # masv88 = pxldat(2)     ---0.865   ***0086
    # masv188 = pxldat(26)   ---1.375
    # masir4 = pxldat(22)    ---3.959   ***0390
    # masir65 = pxldat(27)   ---6.715   ***0700
    # masir11 = pxldat(31)   ---11.030  ***1120
    # masir12 = pxldat(32)   ---12.020  ***1230
    # masir13 = pxldat(35)   ---13.935

    cmin1 = 1.0
    cmin2 = 1.0
    cmin3 = 1.0

    '**** GROUP 1 TESTS **************************************'
    'H20 vapor channel (6.7 micron) high cloud test.'
    if round(masir65) != round(-999.0):
        # nmtests = nmtests + 1
        # if masir65 > dlh20[1]:
        #     nptests = nptests + 1

        c2 = conf_test(masir65, dlh20[0], dlh20[2], dlh20[3], dlh20[1], 1)
        cmin1 = min(cmin1, c2)

    ngtests = ngtests + 1
    '**** GROUP 1 TESTS END **********************************'

    '**** GROUP 2 TESTS **************************************'
    '11-12um brightness temperature difference test for thin cirrus.'
    if round(masir11) != round(-999.0) and round(masir12) != round(-999.0) and vza > 0.0:
        masdf1 = int(masir11 - masir12)
        cosvza = math.cos(vza * dtr)

        if abs(cosvza) > 0.000001:
            schi = 1.0 / cosvza
        else:
            schi = 99.0

        'interpolate look-up table values of 11 - 12 micron bt difference thresholds ' \
        '(function of viewing zenith and 11 micron brightness temperature).'
        diftemp = tview(1, schi, masir11)
        'if a threshold was determined by apollo, then use this as the thin cirrus test,' \
        ' otherwise use a standard threshold.'
        if diftemp < 0.1 or abs(schi - 99.0) < 0.0001:
            dfthrsh = dl11_12hi
        else:
            dfthrsh = diftemp

        'Set flags if test passed.'
        # nmtests = nmtests + 1
        # if masdf1 <= dfthrsh:
        #     nptests = nptests + 1
        locut = dfthrsh + (0.3 * dfthrsh)
        hicut = dfthrsh - 1.25
        c3 = conf_test(masdf1, locut, hicut, 1.0, dfthrsh, 1)
        cmin21 = min(cmin2, c3)
    '======================================================='
    '11 minus 4 micron BTDIF fog and low cloud test.'
    if visusd == 'true':
        if (round(masir11) != round(-999.0) and round(masir4) != round(-999.0)):
            # nmtests = nmtests + 1
            mas11_4 = int(masir11 - masir4)
            # if mas11_4 >= dl11_4lo[1]:
            #     nptests = nptests + 1

            c4 = conf_test(mas11_4, dl11_4lo[0], dl11_4lo[2], dl11_4lo[3], dl11_4lo[1], 1)
            cmin22 = min(cmin2, c4)

    cmin2 = max(cmin21, cmin22)
    ngtests = ngtests + 1
    '**** GROUP 2 TESTS END **********************************'

    '**** GROUP 3 TESTS **************************************'
    'visible (channel 1) reflectance threshold test.'
    if visusd == 'true':
        if round(masv66) != round(-999.0):
            # nmtests = nmtests + 1
            # if masv66 <= dlref1[1]:
            #     nptests = nptests + 1

            c5 = conf_test(masv66, dlref1[0], dlref1[2], dlref1[3], dlref1[1], 1)
            cmin31 = min(cmin3, c5)
    '======================================================='
    'visible channel ratio test(channel2/channel1).' \
    ' Changed to implement GEMI test instead of straight ratio.'
    if visusd == 'true' and vrused == 'true':
        if round(masv66) != round(-999.0) and round(masv88) != round(-999.0):
            # nmtests = nmtests + 1
            # Scale values by 100 to make consistent with MAS version.
            s1 = masv66*100.
            s2 = masv88*100.
            etan = 2.0*(s2 - s1)+1.5*s2+0.5*s1
            etad = s2+s1+0.5
            eta = etan/etad
            vrat = eta*(1.0 - 0.25*eta)-((s1-0.125)/(1.0-s1))
            # if vrat >= dlvrat[1]:
            #     nptests = nptests + 1
            c6 = conf_test(vrat, dlvrat[0], dlvrat[2], dlvrat[3], dlvrat[1], 1)
            cmin32 = min(cmin3, c6)

    cmin3 = max(cmin31, cmin32)
    ngtests = ngtests + 1
    '**** GROUP 3 TESTS END **********************************'

    if ngtests == 3:
        pre_confdnc = cmin2 * cmin3
        fac = 1.0 / 2
        confdnc = pre_confdnc**fac

    return confdnc, cmin21, cmin22, cmin31, cmin32


