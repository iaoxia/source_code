import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'Helvetica'


def mean1(MBE_list9, MBE_list10, MBE_list11, MBE_list12):
    mean_list = []
    for i in range(0, 24):
        mean_v = (MBE_list9[i]+MBE_list10[i]+MBE_list11[i]+MBE_list12[i])/4
        mean_list.append(round(mean_v, 5))

    return mean_list


def mean(MBE_list9, MBE_list10, MBE_list11, MBE_list12, MBE_list1, MBE_list2):
    mean_list = []
    for i in range(0, 24):
        mean_v = (MBE_list9[i]+MBE_list10[i]+MBE_list11[i]+MBE_list12[i]+MBE_list1[i]+MBE_list2[i])/6
        mean_list.append(round(mean_v, 5))

    return mean_list


# beijing 202209-202212
# RMSE_list9= [0.28758, 0.31139, 0.26343, 0.23573, 0.22661, 0.24709, 0.2603, 0.2965, 0.30637, 0.32667, 0.32994, 0.32664, 0.26453, 0.31435, 0.28414, 0.28554, 0.29794, 0.29461, 0.27048, 0.25846, 0.26912, 0.26459, 0.292, 0.29019]
# RMSE_list10= [0.22276, 0.22302, 0.20153, 0.23952, 0.24894, 0.22169, 0.20924, 0.26958, 0.25441, 0.26203, 0.28707, 0.3314, 0.33359, 0.29704, 0.29205, 0.29517, 0.27722, 0.30677, 0.37426, 0.38211, 0.44219, 0.46448, 0.48515, 0.49084]
# RMSE_list11= [0.32734, 0.3588, 0.28943, 0.25258, 0.24204, 0.27538, 0.29217, 0.34603, 0.34737, 0.35803, 0.33155, 0.32102, 0.25324, 0.29971, 0.31245, 0.30781, 0.31634, 0.32345, 0.30437, 0.28434, 0.2831, 0.26434, 0.25909, 0.28679]
# RMSE_list12= [0.23381, 0.2213, 0.23567, 0.25053, 0.27197, 0.22431, 0.22723, 0.2383, 0.2431, 0.26836, 0.30854, 0.33761, 0.3495, 0.34062, 0.34226, 0.32015, 0.30536, 0.31887, 0.34631, 0.35749, 0.35153, 0.4152, 0.45629, 0.46687]
#
# MBE_list9= [-0.19448, -0.22276, -0.1931, -0.18034, -0.16345, -0.20172, -0.20069, -0.21655, -0.23552, -0.23207, -0.21, -0.20586, -0.14448, -0.15897, -0.15828, -0.14414, -0.13069, -0.12897, -0.13828, -0.13207, -0.08621, -0.08655, -0.07828, -0.07]
# MBE_list10= [-0.10032, -0.10548, -0.10613, -0.08, -0.07258, -0.07839, -0.08452, -0.05194, -0.02613, -0.01742, 0.01581, 0.04032, 0.04516, 0.02097, 0.01742, 0.05032, 0.02935, 0.03903, 0.09581, 0.09355, 0.1029, 0.14774, 0.10226, 0.15355]
# MBE_list11= [-0.24053, -0.27158, -0.21579, -0.19842, -0.18474, -0.22211, -0.22263, -0.25368, -0.25421, -0.24684, -0.21474, -0.22211, -0.16895, -0.17316, -0.16158, -0.15474, -0.16474, -0.15895, -0.16316, -0.14895, -0.10211, -0.09368, -0.09158, -0.13737]
# MBE_list12= [-0.09889, -0.12278, -0.13056, -0.12444, -0.09444, -0.11722, -0.10889, -0.09444, -0.07889, -0.05722, -0.01444, -0.00222, 0.01056, 0.00556, 0.00778, 0.01944, -0.00556, 0.00222, 0.06611, 0.09556, 0.11833, 0.12556, 0.15667, 0.1778]


'-0.15 -0.10 -0.06 0.03'

MBE_ZH_1 = [-0.20172, -0.07839, -0.22211, -0.11722]



# mean_list = mean1(RMSE_list9, RMSE_list10, RMSE_list11, RMSE_list12)
# mean_list = mean1(MBE_list9, MBE_list10, MBE_list11, MBE_list12)


# nanjing 202104-202109
# RMSE_list4= [0.21312, 0.18562, 0.21443, 0.19965, 0.24212, 0.23754, 0.28058, 0.27101, 0.26875, 0.2681, 0.33679, 0.35443, 0.34288, 0.35547, 0.37533, 0.41868, 0.44783, 0.42189, 0.38608, 0.35461, 0.37908, 0.34873, 0.3732, 0.40584]
# RMSE_list5= [0.2581, 0.35684, 0.34567, 0.35297, 0.3728, 0.36327, 0.38459, 0.41516, 0.43648, 0.46386, 0.43951, 0.44535, 0.42192, 0.43089, 0.43731, 0.45498, 0.46892, 0.46351, 0.42645, 0.42112, 0.4334, 0.43907, 0.45077, 0.44899]
# RMSE_list6= [0.19651, 0.17397, 0.22624, 0.22335, 0.21261, 0.16886, 0.13285, 0.19134, 0.25521, 0.28838, 0.28652, 0.29075, 0.27207, 0.292, 0.29956, 0.35331, 0.38532, 0.36187, 0.35843, 0.34466, 0.35406, 0.34416, 0.37522, 0.40223]
# RMSE_list7= [0.21132, 0.19724, 0.24122, 0.25123, 0.28801, 0.23617, 0.22412, 0.21963, 0.21122, 0.28792, 0.34261, 0.34271, 0.36665, 0.37559, 0.34473, 0.39166, 0.4192, 0.39422, 0.40297, 0.37135, 0.37692, 0.37335, 0.3887, 0.38898]
# RMSE_list8= [0.21023, 0.20107, 0.25652, 0.25104, 0.24691, 0.23927, 0.28146, 0.27451, 0.29996, 0.30501, 0.29795, 0.29721, 0.31516, 0.33999, 0.34969, 0.33866, 0.31323, 0.31127, 0.31614, 0.29922, 0.30182, 0.30022, 0.29012, 0.31376]
# RMSE_list9= [0.21871, 0.2213, 0.20488, 0.20339, 0.22161, 0.23431, 0.23068, 0.20568, 0.19154, 0.19038, 0.20634, 0.21059, 0.2287, 0.24172, 0.24868, 0.25437, 0.29808, 0.29732, 0.3163, 0.29601, 0.29579, 0.30435, 0.32893, 0.31104]
#
# MBE_list4= [-0.089, -0.0865, -0.098, -0.097, -0.122, -0.1185, -0.1435, -0.1425, -0.1365, -0.114, -0.143, -0.132, -0.1265, -0.136, -0.1465, -0.1805, -0.1925, -0.174, -0.1455, -0.1165, -0.116, -0.116, -0.1105, -0.1495]
# MBE_list5= [-0.14818, -0.20182, -0.18682, -0.17364, -0.18955, -0.20045, -0.21727, -0.24136, -0.25, -0.24591, -0.225, -0.24727, -0.20409, -0.22955, -0.26227, -0.29, -0.29545, -0.30318, -0.27818, -0.26818, -0.28091, -0.29136, -0.29091, -0.29955]
# MBE_list6= [-0.05414, -0.05, -0.07483, -0.08793, -0.10172, -0.0969, -0.07034, -0.08241, -0.11276, -0.13069, -0.08414, -0.06103, -0.10414, -0.11, -0.09276, -0.11897, -0.11034, -0.11517, -0.09793, -0.09862, -0.11, -0.10931, -0.13621, -0.12931]
# MBE_list7= [0.10, 0.0809, 0.0613, 0.0587, 0.04957, 0.05174, 0.04043, -0.00478, -0.01522, -0.05348, -0.0687, -0.05391, -0.04, 0.00174, -0.00565, 0.02652, 0.01261, 0.00783, -0.01391, -0.01, -0.04739, -0.01652, -0.01957, -0.05739]
# MBE_list8= [-0.02355, -0.03839, -0.07968, -0.10065, -0.10935, -0.10258, -0.11484, -0.13839, -0.17355, -0.1629, -0.16645, -0.17258, -0.16871, -0.18226, -0.19452, -0.14968, -0.15419, -0.12806, -0.13516, -0.12903, -0.12258, -0.0971, -0.0871, -0.07]
# MBE_list9= [-0.05036, -0.04893, -0.05393, -0.05321, -0.02964, -0.02929, -0.03286, -0.02964, -0.02714, -0.01179, -0.03464, -0.02393, -0.03821, -0.01071, -0.01607, -0.00107, 0.00964, 0.01821, 0.00107, 0.02214, 0.00929, 0.02714, 0.02357, 0.02643]

# print((MBE_list4[5+6+6+6]+MBE_list5[5+6+6+6]+MBE_list6[5+6+6+6]+MBE_list7[5+6+6+6]+MBE_list8[5+6+6+6]+MBE_list9[5+6+6+6])/6)
'-0.08 -0.11 -0.12 -0.11'
'-0.15 -0.10 -0.06 0.03'
' -0.04 -0.04 -0.04  -0.03'
# mean_list = mean(RMSE_list4, RMSE_list5, RMSE_list6, RMSE_list7, RMSE_list8, RMSE_list9)
# mean_list = mean(MBE_list4, MBE_list5, MBE_list6, MBE_list7, MBE_list8, MBE_list9)

# zhuhai 202209-202302
RMSE_list9= [0.22632, 0.24529, 0.23699, 0.24121, 0.25559, 0.2597, 0.2377, 0.26101, 0.25131, 0.246, 0.23338, 0.23914, 0.24232, 0.25137, 0.23901, 0.24538, 0.2418, 0.2402, 0.24863, 0.26759, 0.2692, 0.26871, 0.28898, 0.29918]
RMSE_list10= [0.18353, 0.16022, 0.14753, 0.17336, 0.16845, 0.14625, 0.14972, 0.1756, 0.21071, 0.24418, 0.26515, 0.28147, 0.30884, 0.28965, 0.29809, 0.26384, 0.23623, 0.25145, 0.25626, 0.29478, 0.30213, 0.31083, 0.34762, 0.30341]
RMSE_list11= [0.12038, 0.12459, 0.12192, 0.11629, 0.18077, 0.13964, 0.10953, 0.13016, 0.14036, 0.14396, 0.16463, 0.1484, 0.17027, 0.16393, 0.16408, 0.17144, 0.20835, 0.19008, 0.20666, 0.22744, 0.26578, 0.25316, 0.28764, 0.31369]
RMSE_list12= [0.19247, 0.18651, 0.18768, 0.22256, 0.22625, 0.22721, 0.22137, 0.22024, 0.22173, 0.23653, 0.25516, 0.25757, 0.27226, 0.25497, 0.25739, 0.26126, 0.26724, 0.28912, 0.29778, 0.30639, 0.32424, 0.32157, 0.33342, 0.32925]
RMSE_list1= [0.1452, 0.16031, 0.17614, 0.16899, 0.19292, 0.23558, 0.24898, 0.24123, 0.2421, 0.27304, 0.27708, 0.28152, 0.29562, 0.31172, 0.30146, 0.27047, 0.2933, 0.27415, 0.33291, 0.3238, 0.33511, 0.37528, 0.32491, 0.34014]
RMSE_list2= [0.30998, 0.31311, 0.30784, 0.30182, 0.28894, 0.30656, 0.28747, 0.30347, 0.30061, 0.29545, 0.27754, 0.25655, 0.27631, 0.27132, 0.27801, 0.29003, 0.29066, 0.31894, 0.29993, 0.31987, 0.30412, 0.29203, 0.30812, 0.31274]

# zhuhai 202209-202302
MBE_list9= [0.03172, 0.04793, 0.04448, 0.02724, 0.03448, 0.04862, 0.04448, 0.06414, 0.06828, 0.06724, 0.06586, 0.07138, 0.07586, 0.08897, 0.05897, 0.04862, 0.08069, 0.07379, 0.04931, 0.03552, 0.05103, 0.02483, -0.00552, -0.00862]
MBE_list10= [0.03161, 0.01097, 0.00613, 0.02032, 0.0271, 0.02677, 0.00613, 0.02161, 0.03903, 0.04935, 0.03871, 0.00613, -0.05806, -0.07968, -0.09548, -0.08387, -0.0771, -0.08774, -0.10258, -0.14323, -0.12194, -0.10903, -0.08742, -0.07387]
MBE_list11= [-0.03077, -0.03846, -0.04115, -0.04077, -0.06923, -0.04462, -0.02962, -0.02577, -0.03, -0.02538, -0.02192, -0.01308, -0.01615, -0.00192, -0.01, -0.01538, -0.01769, -0.01769, -0.01846, -0.02231, -0.01462, 0.00692, 0.02615, 0.10]
MBE_list12= [-0.13, -0.13241, -0.13345, -0.12276, -0.13621, -0.12103, -0.10862, -0.11345, -0.12414, -0.12241, -0.1031, -0.10241, -0.08621, -0.08724, -0.07966, -0.08379, -0.06517, -0.05828, -0.07103, -0.05793, -0.04345, -0.05172, -0.06448, -0.06276]
MBE_list1= [-0.0331, -0.03345, -0.04241, -0.03862, -0.0369, -0.02931, -0.02138, -0.01966, -0.01759, -0.05172, -0.04069, -0.04103, -0.04966, -0.03483, -0.05172, -0.02655, -0.01621, -0.03862, -0.04276, -0.0369, -0.04724, -0.07793, -0.03966, -0.02069]
MBE_list2= [-0.1392, -0.1536, -0.1404, -0.16, -0.146, -0.1504, -0.1712, -0.1644, -0.1768, -0.1472, -0.1404, -0.136, -0.1268, -0.124, -0.0932, -0.1144, -0.1308, -0.1308, -0.1264, -0.13, -0.1216, -0.1024, -0.0928, -0.1004]

# print((MBE_list9[5]+MBE_list10[5]+MBE_list11[5]+MBE_list12[5]+MBE_list1[5]+MBE_list2[5])/6)
' -0.04       -0.04         -0.04      -0.03'

# mean_list = mean(RMSE_list9, RMSE_list10, RMSE_list11, RMSE_list12, RMSE_list1, RMSE_list2)

mean_list = mean(MBE_list9, MBE_list10, MBE_list11, MBE_list12, MBE_list1, MBE_list2)



fig = plt.figure(figsize=(12,3))
ax1 = fig.add_axes([0.1, 0.2, 0.8, 0.6])
plt.ylim(0.2, 0.5)
plt.yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5])

plt.xlim(7, 243)
xx = [10., 20.,  30. , 40.,  50.,  60.,  70.,  80.,  90., 100., 110., 120., 130.,140., 150., 160., 170., 180., 190., 200., 210., 220., 230., 240.]
plt.xticks(xx)

lw = 1.5
'----------------------------------------------------------------------------------------------------------------------'
# plt.ylim(0.2, 0.5)
# plt.yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5])
# plt.plot(xx, RMSE_list9, color='#0072BD', lw=lw)
# plt.plot(xx, RMSE_list10, color='#D95319', lw=lw)
# plt.plot(xx, RMSE_list11, color='#EBD120', lw=lw)
# plt.plot(xx, RMSE_list12, color='#7E2F8E', lw=lw)
'----------------------------------------------------------------------------------------------------------------------'
# plt.ylim(-0.3, 0.2)
# plt.yticks([-0.3, -0.2, -0.1, 0, 0.1, 0.2])
# plt.plot(xx, MBE_list9, color='#0072BD', lw=lw)
# plt.plot(xx, MBE_list10, color='#D95319', lw=lw)
# plt.plot(xx, MBE_list11, color='#EBD120', lw=lw)
# plt.plot(xx, MBE_list12, color='#7E2F8E', lw=lw)
'----------------------------------------------------------------------------------------------------------------------'
# plt.ylim(0.1, 0.5)
# plt.yticks([0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5])
# plt.plot(xx, RMSE_list4, color='#0072BD', lw=lw )
# plt.plot(xx, RMSE_list5, color='#D95319', lw=lw )
# plt.plot(xx, RMSE_list6, color='#EBD120', lw=lw )
# plt.plot(xx, RMSE_list7, color='#7E2F8E', lw=lw )
# plt.plot(xx, RMSE_list8, color='#77AC30', lw=lw )
# plt.plot(xx, RMSE_list9, color='#4DBEEE', lw=lw )
'----------------------------------------------------------------------------------------------------------------------'
# plt.ylim(-0.3, 0.2)
# plt.yticks([-0.3, -0.2, -0.1, 0, 0.1, 0.2])
# plt.plot(xx, MBE_list4, color='#0072BD', lw=lw )
# plt.plot(xx, MBE_list5, color='#D95319', lw=lw )
# plt.plot(xx, MBE_list6, color='#EBD120', lw=lw )
# plt.plot(xx, MBE_list7, color='#7E2F8E', lw=lw )
# plt.plot(xx, MBE_list8, color='#77AC30', lw=lw )
# plt.plot(xx, MBE_list9, color='#4DBEEE', lw=lw )
'----------------------------------------------------------------------------------------------------------------------'
# plt.ylim(0.1, 0.4)
# plt.yticks([0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4])
# plt.plot(xx, RMSE_list9, color='#0072BD', lw=lw )
# plt.plot(xx, RMSE_list10, color='#D95319', lw=lw )
# plt.plot(xx, RMSE_list11, color='#EBD120', lw=lw )
# plt.plot(xx, RMSE_list12, color='#7E2F8E', lw=lw )
# plt.plot(xx, RMSE_list1,  color='#77AC30', lw=lw )
# plt.plot(xx, RMSE_list2,  color='#4DBEEE', lw=lw )
'----------------------------------------------------------------------------------------------------------------------'
plt.ylim(-0.2, 0.15)
plt.yticks([-0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1, 0.15])
plt.plot(xx, MBE_list9, color='#0072BD', lw=lw )
plt.plot(xx, MBE_list10, color='#D95319', lw=lw )
plt.plot(xx, MBE_list11, color='#EBD120', lw=lw )
plt.plot(xx, MBE_list12, color='#7E2F8E', lw=lw )
plt.plot(xx, MBE_list1,  color='#77AC30', lw=lw )
plt.plot(xx, MBE_list2,  color='#4DBEEE', lw=lw )


plt.plot(xx, mean_list, ls='--', color='black', lw=lw)

legend_font = {
    'family': 'Helvetica',  # 字体
    'style': 'normal',
    'size': 'medium',  # 字号
    'weight': "bold"}

plt.legend(['202209', '202210', '202211','202212', '202301', '202302', 'mean'],
           loc=[0.01, 0.85], prop=legend_font, ncol=7)

# plt.legend(['202104', '202105', '202106','202107', '202108', '202109', 'mean'],
#            loc=[0.55, 0.02], prop=legend_font, ncol=4)

# plt.legend(['202104', '202105', '202106','202107', '202108', '202109', 'mean'],
#            loc=[0.01, 0.85], prop=legend_font, ncol=7)

# plt.legend(['202209', '202210', '202211','202212', 'mean'],
#            loc=[0.01, 0.85], prop=legend_font, ncol=5)

# plt.xlabel('Forecast horizon [mins]', fontweight='bold', fontsize=14)
#
# plt.ylabel('MBE_Zhuhai', fontweight='bold', fontsize=14)
#
# plt.grid(ls='--', lw=0.5)
#
# plt.savefig('MBE_Zhuhai', dpi=1000)
