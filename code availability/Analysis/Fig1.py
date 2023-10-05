import h5py
import glob
import math
import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
plt.rcParams['font.sans-serif'] = 'Helvetica'
# f = open('CN-border-La.gmt')
# d = f.readlines()
# borders = [np.fromstring(dd, dtype=float, sep='  ') for dd in d]

ds = xr.open_dataset('ETOPO2v2c_f4.nc')

lon = np.linspace(min(ds['x'].data), max(ds['x'].data), len(ds['x'].data))
lat = np.linspace(min(ds['y'].data), max(ds['y'].data), len(ds['y'].data))
lon, lat = np.meshgrid(lon, lat)
dem = ds['z'].data


with open('CN-border-La.dat') as src:
    context = src.read()
    blocks = [cnt for cnt in context.split('>') if len(cnt) > 0]
    borders = [np.fromstring(block, dtype=float, sep=' ') for block in blocks]


ran = [72, 137, 17, 55]
xticks = [75, 85, 95, 105, 115, 125, 135]
yticks = [10, 20, 30, 40, 50]

LW = 0.1


fig = plt.figure()
proj = ccrs.PlateCarree()
ax = plt.axes(projection=proj)
ax.add_feature(cfeature.OCEAN.with_scale('50m'))
# ax.add_feature(cfeature.LAND.with_scale('50m'), color='w')
ax.add_feature(cfeature.RIVERS.with_scale('50m'), lw=0.25)
ax.add_feature(cfeature.LAKES.with_scale('50m'), color='w')
ax.add_feature(cfeature.COASTLINE, lw=LW)  # 添加海岸线
ax.add_feature(cfeature.BORDERS, linestyle='-', lw=LW)

for line in borders:
    ax.plot(line[0::2], line[1::2], '-', color='black',transform=ccrs.Geodetic(), lw=0.3)
'----------------------------------------------------------------------------------------------------------------------'
levels = [0, 200, 500, 1000, 2000, 3000, 4000, 5000, 7000]  # 创建分级
color =['white', 'whitesmoke', 'gainsboro', 'lightgray', 'silver', 'darkgray', 'gray', 'dimgray', 'black']

m = ax.contourf(lon, lat, dem, levels=levels, extend='both', colors=color)  # 绘图，并设置图例两端显示尖端

cb = fig.colorbar(m, pad=0.01, aspect=30, shrink=0.5)  # 图例在底端显示
cb.set_ticks(levels)  # 设置色带刻度
cb.ax.tick_params(labelsize=5)  # 刻度字号大小
plt.text(x=137.5, y=51, s='Elevation (m)', fontsize='4', fontweight='bold')
'----------------------------------------------------------------------------------------------------------------------'
data1 = pd.read_csv("global_power_plant_database.csv", usecols=["country_long", "name", "capacity_mw",
                                                               "latitude", "longitude", "primary_fuel"])
data = np.array(data1)
Cdata1 = []
for i in range(0, data.shape[0]):
    if data[i][0] == "China":
        Cdata1.append(data[i])
    if data[i][0] == "Taiwan":
        Cdata1.append(data[i])
Cdata = np.array(Cdata1)
x1 = []
y1 = []
for i in range(0, Cdata.shape[0]):
    if Cdata[i][5] == 'Solar':
        x1.append(float(Cdata[i][4]))
        y1.append(float(Cdata[i][3]))

x1 = np.array(x1)
y1 = np.array(y1)
s3 = ax.scatter(x1, y1, marker='o', s=0.4, c='darkgreen')

y = [41.4, 35.667,  43.95,   43.9, 40.383,   37.4,
     34.5, 30.9, 28.817, 30.233, 24.9, 23.333]
x = [106.4, 106.2, 116.117, 125.217, 116.867,  122.7,
     113.05, 113.95, 108.767, 120.167, 118.917, 113.833]
fz = 6
s1 = ax.scatter(x, y, marker='o', s=8, c='red')
plt.text(x=x[0]-4.3, y=y[0]-0.5, s='Hailisu', color='red', fontsize=fz)
plt.text(x=x[1]-3.5, y=y[1]-1.3, s='Liupanshan', color='red', fontsize=fz)
plt.text(x=x[2]+0.5, y=y[2], s='Xilinhot', color='red', fontsize=fz)
plt.text(x=x[3], y=y[3]-1.5, s='Changchun', color='red', fontsize=fz)
plt.text(x=x[4]-2, y=y[4]+0.5, s='Miyun', color='red', fontsize=fz)
plt.text(x=x[5]-1, y=y[5]-1.5, s='Chengtoushan', color='red', fontsize=fz)
plt.text(x=x[6]-3, y=y[6]-1.2, s='Songshan', color='red', fontsize=fz)
plt.text(x=x[7]-2, y=y[7]+0.5, s='Xiaogan', color='red', fontsize=fz)
plt.text(x=x[8]-5.5, y=y[8]-0.5, s='Youyang', color='red', fontsize=fz)
plt.text(x=x[9]-1, y=y[9]-1.5, s='Hangzhou', color='red', fontsize=fz)
plt.text(x=x[10]-1, y=y[10]-1.5, s='Chongwu', color='red', fontsize=fz)
plt.text(x=x[11]-4, y=y[11]+0.5, s='Zengcheng', color='red', fontsize=fz)

yy = [39.9055, 32.1086,  22.35]
xx = [116.425, 118.9596, 113.58]
# 北京，南京，珠海
s2 = ax.scatter(xx, yy, marker='o', s=8, c='blue')
plt.text(x=xx[0]-2, y=yy[0]-1.5, s='Beijing', color='blue', fontsize=fz)
plt.text(x=xx[1]+0.5, y=yy[1], s='Nanjing', color='blue', fontsize=fz)
plt.text(x=xx[2]-0.5, y=yy[2]-1.3, s='Zhuhai', color='blue', fontsize=fz)


yyy = [40.299, 37.6667, 41.2971, 29.7183, 29.6784]
xxx = [109.71, 117.2833, 119.3182, 111.9954, 114.6849]

s4 = ax.scatter(xxx, yyy, marker='o', s=8, c='orange')
plt.text(x=xxx[0]-2, y=yyy[0]-1.3, s='Sangge', color='orange', fontsize=fz)
plt.text(x=xxx[1]-2, y=yyy[1]-1.5, s='Leling', color='orange', fontsize=fz)
plt.text(x=xxx[2]-2, y=yyy[2]+0.5, s='Xiaochengzi', color='orange', fontsize=fz)
plt.text(x=xxx[3]-3.5, y=yyy[3]+0.5, s='Lijiamen', color='orange', fontsize=fz)
plt.text(x=xxx[4]-2, y=yyy[4]-1.5, s='Shiziyan', color='orange', fontsize=fz)
legend_font = {
    'family': 'Helvetica',  # 字体
    'style': 'normal',
    'size': 'xx-small',  # 字号
    }

plt.legend((s3, s1, s2, s4), ('PV plant', 'Manual observation station',
                      'All-sky imager station', 'PV power test plant'), loc='lower left', fontsize='x-small',
                        prop=legend_font)


'----------------------------------------------------------------------------------------------------------------------'
'----------------------------------------------------------------------------------------------------------------------'
'nanhai'
ax2 = fig.add_axes([0.676, 0.1915, 0.1, 0.25], projection=proj)
for line in borders:
    ax2.plot(line[0::2], line[1::2], '-', color='black',transform=ccrs.Geodetic(), lw=0.3)
ax2.contourf(lon, lat, dem, levels=levels, extend='both', colors=color)  # 绘图，并设置图例两端显示尖端
ax2.set_extent([106, 122, 2, 20], crs=ccrs.PlateCarree())
'----------------------------------------------------------------------------------------------------------------------'
ax.set_extent(ran, crs=proj)

gl = ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks, lw=0.2, color='gray', linestyle='--',
                  x_inline=False, y_inline=False, crs=proj)  # Only PlateCarree gridlines are currently supported.
gl.top_labels = False  # 关闭顶端标签
gl.right_labels = False  # 关闭右侧标签
gl.rotate_labels = False
gl.xlabel_style={'size':6}
gl.ylabel_style={'size':6}

lon = []
lat = []

# plt.show()
plt.savefig('2', dpi=1000)




