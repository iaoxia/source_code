import h5py
import numpy as np
from Desert import *
from Land import *

pi = math.acos(-1.0)
dtr = pi / 180.0
confdnc_l = np.zeros([32, 32])
cmin21_list = np.zeros([32, 32])
cmin22_list = np.zeros([32, 32])
cmin31_list = np.zeros([32, 32])
cmin32_list = np.zeros([32, 32])



def read_hdf5_file(file_name, size):
    f = h5py.File(file_name, 'r')
    a0390 = np.array(f['ref_tbb'][:, :, 0])/100     # 5
    a0700 = np.array(f['ref_tbb'][:, :, 1])/100     # 5
    a1120 = np.array(f['ref_tbb'][:, :, 2])/100     # 5          fy3
    a1230 = np.array(f['ref_tbb'][:, :, 3])/100     # 5          fy3
    a064 = np.array(f['ref_tbb'][:, :, 4])/10000       # 1          fy3  0.65
    a086 = np.array(f['ref_tbb'][:, :, 5])/10000         # 1
    a160 = np.array(f['ref_tbb'][:, :, 6])/10000         # 1          fy3
    SunAzimuth = np.array(f['ref_tbb'][:, :, 7])/100         # 5
    SunZenith = np.array(f['ref_tbb'][:, :, 8])/100      # 5

    a0064 = np.zeros([size, size])
    a0086 = np.zeros([size, size])
    a0160 = np.zeros([size, size])
    for i in range(size):
        for j in range(size):
            a0064[i, j] = a064[i, j] / (math.cos(dtr * int(SunZenith[i, j])))
            a0086[i, j] = a086[i, j] / (math.cos(dtr * int(SunZenith[i, j])))
            a0160[i, j] = a160[i, j] / (math.cos(dtr * int(SunZenith[i, j])))

    return a0390, a0700, a1120, a1230, a0064, a0086, a0160, SunAzimuth, SunZenith


def cda_pixel(a0390, a0700, a1120, a1230, a0064, a0086, a0160, satellite_zenith_angle, size,
              dlh20, dl11_12hi, dl11_4lo, dlref1, dlvrat):
    for i in range(0, size):
        for j in range(0, size):
            aa0064 = a0064[i, j]
            aa0086 = a0086[i, j]
            aa0160 = a0160[i, j]
            aa0390 = a0390[i, j]
            aa0700 = a0700[i, j]
            aa1120 = a1120[i, j]
            aa1230 = a1230[i, j]
            '========================================================='
            'step 3.1: Select surface type.'
            '========================================================='
            # desert, land
            confdnc, cmin21, cmin22, cmin31, cmin32 = land(aa0064, aa0086, aa0390, aa0700, aa1120, aa1230,
                                             satellite_zenith_angle,
                                             dlh20, dl11_12hi, dl11_4lo, dlref1, dlvrat)

            confdnc_l[i, j] = confdnc
            cmin21_list[i, j] = cmin21
            cmin22_list[i, j] = cmin21
            cmin31_list[i, j] = cmin21
            cmin32_list[i, j] = cmin21

    return confdnc_l, cmin21_list, cmin22_list, cmin31_list, cmin32_list


def make_cld(confdnc_l, size):
    cld_data = np.zeros([size, size])
    for i in range(0, size):
        for j in range(0, size):
            if confdnc_l[i, j] <= 0.66:
                cld_data[i, j] = 0  # cloudy
            if 0.66 < confdnc_l[i, j] <= 0.95:
                cld_data[i, j] = 1  # prob cloudy
            if 0.95 < confdnc_l[i, j] <= 0.99:
                cld_data[i, j] = 2  # prob land clear
            if confdnc_l[i, j] > 0.99:
                cld_data[i, j] = 3  # land clear

    return cld_data


def write_out_cld_file(data, out_file_name):
    print('writing Cld file!')
    h5file = h5py.File(out_file_name, 'w')  # 打开h5文件


    a1 = h5file.create_dataset('cld_mask', data=np.uint8(data[:, :]))
    a1.attrs['variables'] = 'cloudmask'
    h5file.close()
