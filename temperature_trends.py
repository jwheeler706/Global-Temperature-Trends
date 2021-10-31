from collections import OrderedDict
from progressBar import update
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

## Read in data ##
globe = pd.read_csv('./global_temperatures/GLB.Ts+dSST.csv',header=1)
north = pd.read_csv('./global_temperatures/NH.Ts+dSST.csv',header=1)
south = pd.read_csv('./global_temperatures/SH.Ts+dSST.csv',header=1)
zones = pd.read_csv('./global_temperatures/ZonAnn.Ts+dSST.csv')

def p21():
    ## Extract 5 year spans from data ##
    five_yr = [[i for i in range(j,j+5)] for j in range(1880,2014)]
    five_yr_temp = {}

    for yr in five_yr:
        five_yr_temp[yr[2]] = globe[globe['Year'].isin(yr)]['J-D'].mean()
        
    five_yr_series = pd.Series(five_yr_temp)
        
    ## Extract 11 year spans from data ##
    elev_yr = [[i for i in range(j,j+10)] for j in range(1880,2009)]
    elev_yr_temp = {}

    for yr in elev_yr:
        elev_yr_temp[yr[5]] = globe[globe['Year'].isin(yr)]['J-D'].mean()

    elev_yr_series = pd.Series(elev_yr_temp)

    return five_yr_series, elev_yr_series

def p23():

    seven_yr = [[i for i in range(j,j+7)] for j in range(1880,2012)]
    seven_yr_globe = {}
    seven_yr_north = {}
    seven_yr_south = {}
    
    for yr in seven_yr:
        seven_yr_globe[yr[3]] = globe[globe['Year'].isin(yr)]['J-D'].mean()
        seven_yr_north[yr[3]] = north[north['Year'].isin(yr)]['J-D'].mean()
        seven_yr_south[yr[3]] = south[south['Year'].isin(yr)]['J-D'].mean()

    seven_yr_gseries = pd.Series(seven_yr_globe)
    seven_yr_nseries = pd.Series(seven_yr_north)
    seven_yr_sseries = pd.Series(seven_yr_south)

    return seven_yr_gseries, seven_yr_nseries, seven_yr_sseries

def p24():

    seven_yr = [[i for i in range(j,j+7)] for j in range(1880,2012)]
    tropic = {}
    n_temp = {}
    s_temp = {}
    n_pole = {}
    s_pole = {}

    for yr in seven_yr:
        tropic[yr[3]] = zones[zones['Year'].isin(yr)]['24S-24N'].mean()
        n_temp[yr[3]] = (zones[zones['Year'].isin(yr)]['24N-44N'].mean()+zones[zones['Year'].isin(yr)]['44N-64N'].mean())/2
        s_temp[yr[3]] = (zones[zones['Year'].isin(yr)]['44S-24S'].mean()+zones[zones['Year'].isin(yr)]['64S-44S'].mean())/2
        n_pole[yr[3]] = zones[zones['Year'].isin(yr)]['64N-90N'].mean()
        s_pole[yr[3]] = zones[zones['Year'].isin(yr)]['90S-64S'].mean()
    
    tropic_s = pd.Series(tropic)
    n_temp_s = pd.Series(n_temp)
    s_temp_s = pd.Series(s_temp)
    n_pole_s = pd.Series(n_pole)
    s_pole_s = pd.Series(s_pole)

    return tropic_s, n_temp_s, s_temp_s, n_pole_s, s_pole_s

def plot(animate, five_yr, elev_yr, seven_yr_g, seven_yr_n, seven_yr_s, tropic_s, n_temp_s, s_temp_s, n_pole_s, s_pole_s):

    ## Plot! ##
    fig, axes = plt.subplots(2,2,figsize=(15,10))

    ## Part 2.1 ##
    axes[0][0].plot(globe['Year'],globe['J-D'], label='Raw data', alpha=0.5, zorder=-1)
    axes[0][0].plot(five_yr.index,five_yr.values, 'r--', label='5-year average',  linewxsxsidth=2, zorder=0)
    axes[0][0].plot(elev_yr.index,elev_yr.values, 'g--', label='11-year average', linewidth=2, zorder=1) 
    
    axes[0][0].set_xlabel('Year')
    axes[0][0].legend(fontsize='small',loc=2)
    axes[0][0].set_title('Global Temperature Anomaly')
    
    ## Part 2.2 ##
    months = list(globe.columns[1:13])
    cmap = plt.cm.Set1
    cmaplist = [cmap(i) for i in range(cmap.N)]    
    labels = [str(i)+'-'+str(i+19) for i in range(1880,2000, 20)]+['2000-2017']
    m_avgs = []
    
    for i in range(7):
        tmp_df = globe.iloc[20*i:20*(i+1)]
        tmp_avgs = [tmp_df[month].mean() for month in months]
        axes[0][1].plot(np.arange(12), tmp_avgs, label=labels[i], c=cmaplist[i])
        m_avgs.append(tmp_avgs)
        
    axes[0][1].set_ylim([-0.4,1.2])
    axes[0][1].set_xticks(np.arange(12))
    axes[0][1].set_xticklabels(months)
    axes[0][1].legend(fontsize='small',ncol=2, loc=2)
    axes[0][1].set_title('Global Seasonal Temperature Cycle')

    ## Part 2.3 ## 
    axes[1][0].plot(globe['Year'],globe['J-D'], 'C0-', label='Global total',   alpha=0.2, linewidth=1)
    axes[1][0].plot(north['Year'],north['J-D'], 'C1-', label='Northern total', alpha=0.2, linewidth=1)
    axes[1][0].plot(south['Year'],south['J-D'], 'C5-', label='Southern total', alpha=0.2, linewidth=1)
    
    axes[1][0].plot(seven_yr_g.index,seven_yr_g.values, 'C0--', label='Global 7-year average', linewidth=2)
    axes[1][0].plot(seven_yr_n.index,seven_yr_n.values, 'C1--', label='Northern 7-year average', linewidth=2)
    axes[1][0].plot(seven_yr_s.index,seven_yr_s.values, 'C5--', label='Southern 7-year average', linewidth=2)
    
    axes[1][0].legend(fontsize='small',ncol=2,loc=2)
    axes[1][0].set_title('Global, Northern, and Southern Hemisphere Temperature Anomaly')

    ## Part 2.4 ##
    axes[1][1].plot(seven_yr_g.index, seven_yr_g.values, 'C0-', label='Global', alpha=0.5)
    axes[1][1].plot(n_temp_s.index, n_temp_s.values, 'C1--', label='Northern Temperature Latitude')
    axes[1][1].plot(s_temp_s.index, s_temp_s.values, 'C5--', label='Southern Temperature Latitude')
    axes[1][1].plot(n_pole_s.index, n_pole_s.values, 'C3:', label='North Pole Latitude')
    axes[1][1].plot(s_pole_s.index, s_pole_s.values, 'C4:', label='South Pole Latitude')
    
    axes[1][1].legend(fontsize='small',ncol=2,loc=2)
    axes[1][1].set_title('Zonal Temperature Anomaly (7-year averages)')

    ## Title and save ##
    fig.suptitle('Temperature Trends 1880-2017', fontweight='heavy')
    plt.savefig('./part2_final.png', dpi=400)

    ax0_lim = axes[0][0].get_ylim()
    ax1_lim = axes[0][1].get_ylim()
    ax2_lim = axes[1][0].get_ylim()
    ax3_lim = axes[1][1].get_ylim()

    axes[0][1].cla()

    ## Animation frames ##
    if animate:
        for i in range(1,len(globe)+1):
            axes[0][0].cla()
            axes[1][0].cla()
            axes[1][1].cla()
            
            axes[0][0].set_xlim([1880,2020])
            axes[0][1].set_xlim([1,11])
            axes[1][0].set_xlim([1880,2020])
            axes[1][1].set_xlim([1880,2020])
            
            axes[0][0].set_ylim(ax0_lim)
            axes[0][1].set_ylim(ax1_lim)
            axes[1][0].set_ylim(ax2_lim)
            axes[1][1].set_ylim(ax3_lim)
            
            axes[0][0].set_title('Global Temperature Anomaly')
            axes[0][1].set_title('Average Global Seasonal Temperature Cycle')
            axes[1][0].set_title('Global, Northern, and Southern Hemisphere Temperature Anomaly')
            axes[1][1].set_title('Zonal Temperature Anomaly (7-year averages)')
            
            axes[0][1].set_xticks(np.arange(12))
            axes[0][1].set_xticklabels(months)
            
            axes[0][0].plot(globe['Year'][:i],globe['J-D'][:i], label='Raw data', alpha=0.5, zorder=-1)
            axes[1][0].plot(globe['Year'][:i],globe['J-D'][:i], 'C0-', label='Global total',   alpha=0.2, linewidth=1)
            axes[1][0].plot(north['Year'][:i],north['J-D'][:i], 'C1-', label='Northern total', alpha=0.2, linewidth=1)
            axes[1][0].plot(south['Year'][:i],south['J-D'][:i], 'C5-', label='Southern total', alpha=0.2, linewidth=1)
            axes[0][0].legend(fontsize='small',ncol=2,loc=2)
            axes[1][0].legend(fontsize='small',ncol=2,loc=2)
            
            if i > 2:
                j = i-2
                if i > 137:
                    j = 137
                axes[0][0].plot(five_yr.index[:j],five_yr.values[:j], 'r--', label='5-year average',  linewidth=2, zorder=0)

            if i > 4:
                j = i-4
                if i > 136:
                    j = 136
                axes[1][0].plot(seven_yr_g.index[:j],seven_yr_g.values[:j], 'C0--', label='Global 7-year average', linewidth=2)
                axes[1][0].plot(seven_yr_n.index[:j],seven_yr_n.values[:j], 'C1--', label='Northern 7-year average', linewidth=2)
                axes[1][0].plot(seven_yr_s.index[:j],seven_yr_s.values[:j], 'C5--', label='Southern 7-year average', linewidth=2)
                axes[1][0].legend(fontsize='small',ncol=2,loc=2)
                
                axes[1][1].plot(seven_yr_g.index[:j], seven_yr_g.values[:j], 'C0-', label='Global', alpha=0.5)
                axes[1][1].plot(n_temp_s.index[:j], n_temp_s.values[:j], 'C1--', label='Northen Temperature Latitude')
                axes[1][1].plot(s_temp_s.index[:j], s_temp_s.values[:j], 'C5--', label='Southern Temperature Latitude')
                axes[1][1].plot(n_pole_s.index[:j], n_pole_s.values[:j], 'C3:', label='North Pole Latitude')
                axes[1][1].plot(s_pole_s.index[:j], s_pole_s.values[:j], 'C4:', label='South Pole Latitude')
                axes[1][1].legend(fontsize='small',ncol=2,loc=2)

            if i > 6:
                j = i-6
                if i > 133:
                    j = 133
                axes[0][0].plot(elev_yr.index[:j],elev_yr.values[:j], 'g--', label='11-year avg', linewidth=2, zorder=1)
                axes[0][0].legend(fontsize='small',ncol=2,loc=2)

            if i%20 == 0:
                j = int((i/20)-1)
                axes[0][1].plot(np.arange(12), m_avgs[j], label=labels[j], c=cmaplist[j])
                axes[0][1].legend(fontsize='small',ncol=2,loc=2)

            if i == len(globe):
                axes[0][1].plot(np.arange(12), m_avgs[-1], label=labels[-1], c=cmaplist[6])
                axes[0][1].legend(fontsize='small',ncol=2,loc=2)

            txt = fig.text(.48,.93,'Year: '+str(1880+i))
                        
            plt.savefig('./animation_frames_update/frame_{:03d}.png'.format(i), dpi=400)
            update(i,len(globe))

            txt.remove()

            ## ffmpeg -framerate 5 -i animation_frames/frame_%03d.png -pix_fmt yuv420p part3_final.mp4 ##

def part2():
    
    ## Call functions ##
    five_yr, elev_yr = p21()
    seven_yr_g, seven_yr_n, seven_yr_s = p23()
    tropic_s, n_temp_s, s_temp_s, n_pole_s, s_pole_s = p24()
    plot(True, five_yr, elev_yr, seven_yr_g, seven_yr_n, seven_yr_s, tropic_s, n_temp_s, s_temp_s, n_pole_s, s_pole_s)
    

if __name__ == '__main__':
    part2()
