#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------------------------------------
|  Copyright @, Xia Pan, 2022                                              |
|**************************************************************************|
|  All rights reserved. This source code is part of the cloud detection    |
|  algorithm and is designed for scientific and research purposes.         |
|  Pan grants USER the right to download, install, use and copy this       |
|  software for scientific and research purposes only.                     |
|  This software may be redistributed as long as this copyright notice     |
|  is reproduced on any copy made and appropriate acknowledgment is        |
|  given to Min.                                                           |
|  This software or any modified version of this software may not be       |
|  incorporated into proprietary software or commercial software offered   |
|  for sale.                                                               |
|**************************************************************************|
|  This software is provided as is without any express or implied          |
|  warranties.                                                             |
----------------------------------------------------------------------------
++++++++++++++++++++++++{ Cloud Detection Algorithm }+++++++++++++++++++++++
----------------------------------------------------------------------------
|*******Created on 2022.04.11                                              |
|*******Version 1.7                                                        |
|*******@author: Xia Pan                                                   |
|*******@unit: School of Atmospheric Sciences, Sun Yat-Sen University      |
|*******@E-mail: 1136382869@qq.com                                         |
----------------------------------------------------------------------------
"""
'''
P01 P02 P03 P04 P05 P06 P07 P08 P09 P10 P11 P12 P13 P14 P15 P16 P17 P18
the type of surface: 
land---01, desert---02;                                                       ppp
01.  : 'Yuhuan A'            28.163  121.32             01        0.83951    0.80876
02.  : 'Lanshan Reservoir'   30.027  121.626            01        0.82163    0.78457
03.  : 'Xihe'                31.76   113.515            01        0.84634    0.80622
04.  : 'Xiangshui JS'        34.401  119.951            01        0.80444    0.75464
05.  : 'Kenli A'             37.551  118.827            01   $    0.75424    0.72774
06.  : 'Yanchi'              37.982  106.999            02   $$   0.75562    0.72311
07.  : 'Yuyang D'            38.81   109.692            02   $$   0.75466    0.72742
08.  : 'Balagong IV'         40.185  107.036            02   $$   0.71366    0.66822
09.  : 'Chengde'             40.89   118.623            01   $$$  0.69799    0.68006
10.  : 'Changde'             46.245  125.006            01   $$$  0.65591    0.60803
11.  : 'ZGH'                 40.299  109.71             02   $$   0.72742    0.69346
12.  : 'Beijing'             39.8    116.4667           
13.  : 'Baoshang'            31.3833 121.45
14.  : 'Guangzhou'           23.2167 113.4833
15.  : 'Wuhan'               30.6    114.05 
16.  : 'Dongshan'            31.0833 120.4333
17.  : 'Hangzhou'            30.2333 120.1667
18.  : 'Shapingbai'          29.5833 106.4667
'''
import os
import sys
import glob
from multiprocessing import Pool
import time
sys.path.append('src/')
# from Desert import *
from Land import *
from cloud_detection_bat import *

def julianday(IY, IM, ID, IH, MIT):
    if IM <= 2:  # january & february
        IY1 = IY - 1
        IM1 = IM + 12
        JD = float(int(365.25 * (IY1 + 4716.0)) + int(30.6001 * (IM1 + 1.0)) + 2.0 - int(IY1 / 100.0) + int(
            int(IY1 / 100.0) / 4.0) + ID - 1524.5) + float((IH + MIT / 60. + 0. / 3600.) / 24.)

    else:
        JD = float(int(365.25 * (IY + 4716.0)) + int(30.6001 * (IM + 1.0)) + 2.0 - int(IY / 100.0) + int(
            int(IY / 100.0) / 4.0) + ID - 1524.5) + float((IH + MIT / 60. + 0. / 3600.) / 24.)

    return JD


def julian_to_date(JD):
    I = int(JD + 0.5)
    Fr = abs(I - (JD + 0.5))

    if I >= 2299160.0:
        A = int((I - 1867216.25) / 36524.25)
        a4 = int(A / 4)
        B = I + 1. + float(A - a4)
    else:
        B = I

    C = B + 1524.
    D = int((C - 122.1) / 365.25)
    E = int(365.25 * D)
    G = int((C - E) / 30.6001)
    day = int(C - E + Fr - int(30.6001 * G))

    if G <= 13.5:
        month = int(G - 1)
    else:
        month = int(G - 13)

    if month > 2.5:
        year = int(D - 4716)
    else:
        year = int(D - 4715)

    hour = int(Fr * 24.)
    mint = int(abs(hour - (Fr * 24.)) * 60.)
    return year, month, day


def int_to_str(a):
    if a < 10:
        c = '0' + str(a)
    else:
        c = str(a)

    return c


def main05(date_fn, x):


    xi = x
    print('-----------------------------------------------------------------------------')
    print('step 0: Cheak l1b_file path and out_file_path!')
    print('-----------------------------------------------------------------------------')

    L1b_path = code_path + '2017_l1b_hdf5/P' + xi + '/' + date_fn + '/'
    out_file_path = code_path + '2017_cda_cld_hdf5/P' + xi + '/' + date_fn + '/'

    fx = open(cda_pic_path + 'P' + xi + '/'+date_fn+'cmin.txt', mode='w')
    '-----------------------------------------------------------------------------'
    '-----------------------------------------------------------------------------'
    if os.path.isdir(L1b_path):
        print('L1b_path is ok!')
    else:
        os.system('mkdir ' + L1b_path)

    if os.path.isdir(out_file_path):
        print('Out_file_path is ok!')
    else:
        os.system('mkdir ' + out_file_path)
    '-----------------------------------------------------------------------------'
    '-----------------------------------------------------------------------------'

    L1b_list = glob.glob(L1b_path + '*.hdf5')


    if L1b_list == []:
        print(L1b_path)
        print('this path has no file!')
    else:
        L1b_list.sort(key=lambda x: int(x[-18:-10] + x[-9:-5]))
        print('-----------------------------------------------------------------------------')
        print('step 1: Check l1b_file size!')
        print('-----------------------------------------------------------------------------')
        l1b_file_number = len(L1b_list)


        for x in range(0, l1b_file_number):
            sz = os.path.getsize(L1b_list[x])
            f_kb = sz / (float(1024))

            if f_kb != 20:
                print('============================[Step 1 Warning]============================')
                print(L1b_list[x] + ', the size is not right!')
                print('========================================================================')
            else:

                size = int(L1b_list[x][-26:-24])
                TT = int(L1b_list[x][-9:-5])
                # if TT <= 930 or TT >= 2230:   # 北京时间6：30-17：30
                if TT <= 800:  # 北京时间8：00-16：00

                    print('-----------------------------------------------------------------------------')
                    print('step 2: Read l1b_file!')
                    print('-----------------------------------------------------------------------------')

                    a0390, a0700, a1120, a1230, a0064, a0086, a0160, SunAzimuth, SunZenith = \
                        read_hdf5_file(L1b_list[x], size)


                    print('-----------------------------------------------------------------------------')
                    print('step 3: Start Cloud Detection!')
                    print('-----------------------------------------------------------------------------')
                    l1b_file_name = os.path.basename(L1b_list[x])
                    site_id = int(l1b_file_name[3:5])
                    sza = satellite_zenith_angle[site_id - 1]
                    file_name = l1b_file_name[3:5] + '_h8_4km_cld_32X32_tile_' + l1b_file_name[28:41]


                    confdnc_l, cmin21_list, cmin22_list, cmin31_list, cmin32_list = \
                        cda_pixel(a0390, a0700, a1120, a1230, a0064, a0086, a0160,
                                          sza, size, dlh20, dl11_12hi, dl11_4lo, dlref1, dlvrat)


                    fx.write(l1b_file_name+'\n')
                    fx.write('-------------------cmin21---------------------------' + '\n')
                    fx.write(str(cmin21_list)+'\n')
                    fx.write('-------------------cmin22---------------------------' + '\n')
                    fx.write(str(cmin22_list)+'\n')
                    fx.write('-------------------cmin31---------------------------' + '\n')
                    fx.write(str(cmin31_list)+'\n')
                    fx.write('-------------------cmin32---------------------------' + '\n')
                    fx.write(str(cmin32_list)+'\n')


                    print('-----------------------------------------------------------------------------')
                    print('step 4: Determine if there are clouds!')
                    print('-----------------------------------------------------------------------------')

                    cld_data = make_cld(confdnc_l, size)

                    print('-----------------------------------------------------------------------------')
                    print('step 5: Output cld hdf5 files!')
                    print('-----------------------------------------------------------------------------')

                    out_file_name = out_file_path + 'pp0' + file_name + '.hdf5'
                    write_out_cld_file(cld_data, out_file_name)

    fx.close()


'*********************************************************************************************'
satellite_azimuth_angle = [327.9662, 330.2954, 323.31482, 332.40152, 333.91074, 324.2907,
                           327.08203, 326.42084, 336.3308, 345.31412, 328.4258,333.50668,
                           331.36935, 312.93988, 322.56436, 329.88846, 328.73044, 314.96136]

satellite_zenith_angle = [39.20013, 40.73619, 47.22862, 45.670155, 49.17726, 56.290207,
                          55.232555, 57.892574, 52.369534, 55.32946, 56.385242, 52.394493,
                          42.08042, 40.91461, 45.978798, 42.37487, 41.735287, 50.82784]
'*********************************************************************************************'
'=========================[ land ]========================='
# dlh20 = [215.0, 220.0, 225.0, 1.0]
# dl11_12hi = 3.0
# dl11_4lo = [-24.0, -22.0, -20.0, 0.95]
# dlref1 = [0.36, 0.32, 0.28, 0.95]
# dlvrat = [1.92, 1.97, 2.02, 0.95]
dlh20 = [215.0, 220.0, 225.0, 1.0]
dl11_12hi = 3.0
dl11_4lo = [-14.0, -12.0, -10.0, 1.0]
dlref1 = [0.24, 0.20, 0.16, 1.0]
dlvrat = [1.80, 1.85, 1.90, 1.0]

# dlh20 = [215.0, 220.0, 225.0, 1.0]
# dl11_12hi = 3.0
# dl11_4lo = [-15.0, -13.0, -11.0, 0.9]
# dlref1 = [0.26, 0.22, 0.18, 0.9]
# dlvrat = [1.83, 1.87, 1.91, 0.9]
'=========================================================='
'========================[ desert ]========================'
# ldsh20 = [215.0, 220.0, 225.0, 1.0]
# lds11_12hi = [3.5, 3.0, 2.5, 1.00]
# lds11_4lo = [-20.0, -18.0, -16.0, 1.00]
# lds11_4hi = [2.00, 0.00, -2.00, 1.00]
# ldsref2 = [0.42, 0.39, 0.36, 1.00]
'=========================================================='
x = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
     '10', '11', '12', '13', '14', '15', '16', '17', '18']
'*********************************************************************************************'
year = [2017, 2017]
month = [1, 1]
day = [1, 31]
nthreads = 200  # 并行数


code_path = '/share/home/dq014/xiap/PredRNN/CDA_20220411/'

cda_pic_path = '/share/home/dq014/xiap/PredRNN/2017_cda_picture/2017_cda_pic/'


if __name__ == '__main__':
    clock00 = time.time()

    jd1 = julianday(year[0], month[0], day[0], 0, 0)
    jd2 = julianday(year[1], month[1], day[1], 0, 0)
    nday = int(jd2 - jd1 + 1)

    for i in range(12, 13):
        xx = x[i]

        '********************************************************************************************'
        '************************************[ Cloud detection !]************************************'

        p = Pool(nthreads)

        for iday in range(0, nday):
            jd = jd1 + iday
            [y1, m1, d1] = julian_to_date(jd)
            yn = int_to_str(y1)
            mn = int_to_str(m1)
            dn = int_to_str(d1)
            date_fn = yn + mn + dn
            xx = x[i]
            print('++++++++++++++++[ date]++++++++++++++++')
            print(date_fn)
            print('++++++++++++++++[ date]++++++++++++++++')

            p.apply_async(main05, args=(date_fn, xx))

        print('=========================================================')
        print('Day is over!')
        print('=========================================================')

        p.close()
        p.join()

        '********************************************************************************************'
        '********************************************************************************************'

    clock11 = time.time()
    time_cost = clock11 - clock00
    min_cost = int(time_cost / 60)  # minute
    sec_cost = time_cost % 60  # second
    print('====================================================================')
    print('------ Processing Duration %.6f seconds.' % (time_cost))
    print('------ OR = %i minutes and %.6f seconds.' % (min_cost, sec_cost))
    print('====================================================================')