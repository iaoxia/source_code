"""
#--------------------
Created on 2021.10.28
Version 1.0
__author__ = 'Xx'
#--------------------
"""
import math
from conf_test import conf_test
from conf_test_2val import conf_test_2val
from tview import tview
'''
Description:
        Routine for performing clear sky tests over desert and arid surfaces during daylight hours.
        For daytime desert the groups are:
            Group 1: High thick cloud
                6.75 micron bt test 
            
            Group 2: Mainly Low cloud - thick
                11-4 micron bt tests
                11-12 Thin cirrus tests
                
            Group 3: Thick cloud                   
                87 micron reflectance test (masv87)
            
    
Input Parameters:
pxldat        Array containing reflectance or brightness temperatures for all bands for a single pixel.
              单个像素点所有波段的反射率和亮温
vza           Viewing zenith angle for current pixel.
              当前像素点的天顶角
visusd        Logical variable indicating whether vis data used or not.
              用来表明是否使用vis数据的逻辑变量
              
# cirrus_vis 	  Logical variable flagging thin cirrus contaminated  scenes in the visible.
#               用来标注薄卷云影响可见光的逻辑变量
# hi_elev       Logical variable indicating high elevation (> 2000 meters).
#               用来表明高海拔的逻辑变量

Output Parameters:
testbits      six byte integer containing bit results.
              包含bit结果的六字节整数
qa_bits       ten byte integer containing qa bit results.
              包含qa bit结果的十字节整数
nmtests       Counts number of inidividual tests applied.
              单独测试次数
confdnc       product of all applied individual confidences.
              所有置信度的乘积
confdnc = 1.0    
================================================================
nptests       nptests counts the number of tests passed

a0390, a0700, a1120, a1230, a1330, a0064, a0160
0390---MODIS[21/22], 0700---MODIS[27/28]
1120---MODIS[31], 1230---MODIS[32], 1330---MODIS[33]

0064---MODIS[1], 0160---MODIS[6]

'''


def desert(a0086, a0390, a0700, a1120, a1230, vza,
           ldsh20, lds11_12hi, lds11_4lo, lds11_4hi, ldsref2):
    # initialize variables
    visusd = 'ture'
    nmtests = 0  # counts the number of tests applied to this pixel
    nptests = 0  # counts the number of tests passed
    cmin1 = 1.0
    cmin2 = 1.0
    cmin3 = 1.0
    ngtests = 0  # initialize group number.
    # ldsh20 = [215.0, 220.0, 225.0, 1.0]
    # lds11_12hi = [3.5, 3.0, 2.5, 1.00]
    # lds11_4lo = [-20.0, -18.0, -16.0, 1.00]
    # lds11_4hi = [2.00, 0.00, -2.00, 1.00]
    # ldsref2 = [0.42, 0.39, 0.36, 1.00]
    pi = math.acos(-1.0)
    dtr = pi/180.0

    masv88 = a0086    # 2
    masir4 = a0390    # 22
    masir65 = a0700   # 27
    masir11 = a1120   # 31
    masir12 = a1230   # 32

    # masv88 = pxldat(2)     ---0.865   ***0086
    # masv188 = pxldat(26)   ---1.375
    # masir4 = pxldat(22)    ---3.959   ***0390
    # masir65 = pxldat(27)   ---6.715   ***0700
    # masir11 = pxldat(31)   ---11.030  ***1120
    # masir12 = pxldat(32)   ---12.020  ***1230
    # masir13 = pxldat(35)   ---13.935

    '**** GROUP 1 TESTS **************************************'
    'H20 vapor channel (6.7 micron) high cloud test.'
    if round(masir65) != round(-999.0):
        # nmtests = nmtests + 1
        # if masir65 > ldsh20[1]:
        #     nptests = nptests + 1

        c2 = conf_test(masir65, ldsh20[0], ldsh20[2], ldsh20[3], ldsh20[1], 1)
        cmin1 = min(cmin1, c2)

    ngtests = ngtests + 1
    '**** GROUP 1 TESTS END **********************************'

    '**** GROUP 2 TESTS **************************************'
    '11-12um brightness temperature difference test for thin cirrus.'
    if round(masir11) != round(-999.0) and round(masir12) != round(-999.0) and vza > 0.0:
        masdf1 = masir11 - masir12
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
            dfthrsh = lds11_12hi[1]
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
    if visusd == 'ture':
        if (round(masir11) != round(-999.0) and round(masir4) != round(-999.0)):
            if masir11 <= 320.0:
                # nmtests = nmtests + 1
                mas11_4 = masir11 - masir4
                # if mas11_4 >= lds11_4lo[1] and mas11_4 <= lds11_4hi[1]:
                #     # nptests = nptests + 1

                locuta = [0, 0]
                hicuta = [0, 0]
                midpta = [0, 0]
                locuta[0] = lds11_4lo[0]
                locuta[1] = lds11_4hi[0]
                hicuta[0] = lds11_4lo[2]
                hicuta[1] = lds11_4hi[2]
                midpta[0] = lds11_4lo[1]
                midpta[1] = lds11_4hi[1]

                c4 = conf_test_2val(mas11_4, locuta, hicuta, 1.0, midpta, 2)
                cmin22 = min(cmin2, c4)

    cmin2 = max(cmin21, cmin22)
    ngtests = ngtests + 1
    '**** GROUP 2 TESTS END **********************************'


    '**** GROUP 3 TESTS **************************************'
    'visible (0.88 micron) reflectance threshold test.'
    if round(masv88) != round(-999.0):
        # nmtests = nmtests + 1
        # if masv88 <= ldsref2[1]:
        #     nptests = nptests + 1

        c5 = conf_test(masv88, ldsref2[0], ldsref2[2], ldsref2[3], ldsref2[1], 1)
        cmin3 = min(cmin3, c5)

    ngtests = ngtests + 1
    '**** GROUP 3 TESTS END **********************************'

    if ngtests == 3:
        pre_confdnc = cmin2 *cmin3
        fac = 1.0 / 2
        confdnc = pre_confdnc**fac

    return nmtests, nptests, confdnc


