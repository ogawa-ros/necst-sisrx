#!/usr/bin/env python3



def iv_plot(file_name, save_name):
    import os, sys
    import matplotlib.pyplot as plt
    import std_msgs.msg
    import pandas

    import necstdb
    db = necstdb.necstdb()  #plot graph
    db.open(file_name)

    d = db.read_as_pandas()
    d['time'] = pandas.to_datetime(d['time'], unit='s')
    d['data'] = [_[0]['data'] for _ in d['msgs']]
    d2 = d.set_index(['topic', 'time']).sort_index()

    dd = pandas.concat(
        [
            d2.loc['/tz2019/sis_v1/v'][['data']].rename(columns={'data': 'V1V'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_v1/i'][['data']].rename(columns={'data': 'V1I'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_h1/v'][['data']].rename(columns={'data': 'H1V'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_h1/i'][['data']].rename(columns={'data': 'H1I'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_v2/v'][['data']].rename(columns={'data': 'V2V'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_v2/i'][['data']].rename(columns={'data': 'V2I'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_h2/v'][['data']].rename(columns={'data': 'H2V'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_h2/i'][['data']].rename(columns={'data': 'H2I'}).astype(float).resample('0.1S').mean(),
            #d2.loc['/dev/ma24126a/power'][['data']].rename(columns={'data': 'power'}).astype(float).resample('0.1S').mean(),
        ],
        axis = 1,
    )
    #under the i-v graph plot

    fig = plt.figure(figsize=(7, 6))
    ax = [fig.add_subplot(2, 2, i) for i in range(1, 5)]
    ax[0].plot(dd['V1V'], dd['V1I'], '.')
    #ax[0].plot(dd['V1V'], dd['power'], '.')
    ax[1].plot(dd['H1V'], dd['H1I'], '.')
    ax[2].plot(dd['H2V'], dd['H2I'], '.')
    ax[3].plot(dd['V2V'], dd['V2I'], '.')
    ax[0].set_title('V1 I-V')
    ax[1].set_title('H1 I-V')
    ax[2].set_title('H2 I-V')
    ax[3].set_title('V2 I-V')
    [_.set_xlabel('Voltage (mV)') for _ in ax]
    [_.set_ylabel('Current (uA)') for _ in ax]
    [_.grid(True, linestyle=':') for _ in ax]

    plt.suptitle(str(save_name))
    #plt.show()
    graph_file_name = '/home/exito/data/logger/test/' + str(save_name) +'iv_plot.png'
    plt.savefig(graph_file_name)



def att_iv_plot(file_name, save_name, att_vol):
    import os, sys
    import matplotlib.pyplot as plt
    import std_msgs.msg
    import pandas

    import necstdb
    db = necstdb.necstdb()  #plot graph
    db.open(file_name)

    d = db.read_as_pandas()
    d['time'] = pandas.to_datetime(d['time'], unit='s')
    d['data'] = [_[0]['data'] for _ in d['msgs']]
    d2 = d.set_index(['topic', 'time']).sort_index()

    dd = pandas.concat(
        [
            d2.loc['/tz2019/sis_v1/v'][['data']].rename(columns={'data': 'V1V'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_v1/i'][['data']].rename(columns={'data': 'V1I'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_h1/v'][['data']].rename(columns={'data': 'H1V'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_h1/i'][['data']].rename(columns={'data': 'H1I'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_v2/v'][['data']].rename(columns={'data': 'V2V'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_v2/i'][['data']].rename(columns={'data': 'V2I'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_h2/v'][['data']].rename(columns={'data': 'H2V'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_h2/i'][['data']].rename(columns={'data': 'H2I'}).astype(float).resample('0.1S').mean(),
            #d2.loc['/dev/ma24126a/power'][['data']].rename(columns={'data': 'power'}).astype(float).resample('0.1S').mean(),
        ],
        axis = 1,
    )
    #under the i-v graph plot

    fig = plt.figure(figsize=(7, 6))
    ax = [fig.add_subplot(2, 2, i) for i in range(1, 5)]
    ax[0].plot(dd['V1V'], dd['V1I'], '.')
    ax[1].plot(dd['H1V'], dd['H1I'], '.')
    ax[2].plot(dd['H2V'], dd['H2I'], '.')
    ax[3].plot(dd['V2V'], dd['V2I'], '.')
    ax[0].set_title('V1 I-V')
    ax[1].set_title('H1 I-V')
    ax[2].set_title('H2 I-V')
    ax[3].set_title('V2 I-V')
    [_.set_xlabel('Voltage (mV)') for _ in ax]
    [_.set_ylabel('Current (uA)') for _ in ax]
    [_.grid(True, linestyle=':') for _ in ax]

    plt.suptitle('att_level = ' + str(att_vol))
    #plt.show()
    graph_file_name = '/home/exito/data/logger/test/' + str(save_name) + '/fig_att_level=' + str(att_vol) +'iv_plot.png'
    plt.savefig(graph_file_name)

def yfactor_plot(file_name, save_name):
    import os, sys
    import matplotlib.pyplot as plt
    import std_msgs.msg
    import pandas
    import numpy
    import necstdb
    import exp_yfactor
    db = necstdb.necstdb()  #plot graph
    db.open(file_name)

    d = db.read_as_pandas()
    d['time'] = pandas.to_datetime(d['time'], unit='s')
    d['data'] = [_[0]['data'] for _ in d['msgs']]
    d2 = d.set_index(['topic', 'time']).sort_index()


    spdata = d2.loc['/dev/n9343c/ip_192_168_100_185/spec'][['data']]

    p = numpy.array(spdata)
    power = p[30][0]
    trx = exp_yfactor.evaluate_trx_from_rotating_chopper_data(power, 300, 77)

    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(111)
    ax.plot(power)
    ax.set_xlabel('time')
    ax.set_ylabel('power (dBm)')
    ax.set_title('yfactor-measurement')
    ax.grid(True)
    fig.savefig('/home/exito/data/logger/test/' + str(save_name) +'_yfactor_plot.png')
    return trx

def sis_bias_and_yfactor_matrix_plot(v1, v2, trx, save_name):
    import matplotlib.pyplot as plt
    import std_msgs.msg
    import numpy as np
    import necstdb
    import exp_yfactor

    #vp = numpy.linspace(-1, 0, 5)

    #v1 = []
    #v2 = []
    #for vol in vp:
    #    h = 6.626*10**(-34)
    #    e = 1.602*10**(-19)
    #    lofreq = 92*10**9
    #    n = 3
    #    v = ((n*h*lofreq*vol)/e + 2.8*n)
    #    v1.append(v)
    #    v2.append(v)
    #    continue


    #Y = numpy.array(v1)
    #X = numpy.array(v2)
    #Z = numpy.array(trx).reshape(5,5)

    x = v1
    y = v2
    z = trx
    #print(str(x))
    #print(str(y))
    #print(str(z))
    np.save(
    '/home/exito/data/logger/test/'+str(save_name)+'/v1_data',
    x
    )
    np.save(
    '/home/exito/data/logger/test/'+str(save_name)+'/v2_data',
    y
    )
    np.save(
    '/home/exito/data/logger/test/'+str(save_name)+'/trx_data',
    z
    )

    plt.scatter(x, y, c=z)
    pp=plt.colorbar (orientation="vertical")
    pp.set_label("Trx[K]")
    plt.xlabel('v1_vol[mV]')
    plt.ylabel('v2_vol[mV]')
    plt.title("yfactor_map")
    plt.xlim(5, 9)
    plt.ylim(5, 9)
    plt.grid()

    plt.savefig('/home/exito/data/logger/test/' + str(save_name) + '/yfactor_matrix.png')

def sis_vol_average(file_name):
    import std_msgs.msg
    import numpy
    import necstdb
    import pandas

    db = necstdb.necstdb()  #plot graph
    db.open(file_name)

    d = db.read_as_pandas()
    d['time'] = pandas.to_datetime(d['time'], unit='s')
    d['data'] = [_[0]['data'] for _ in d['msgs']]
    d2 = d.set_index(['topic', 'time']).sort_index()

    dd = pandas.concat(
        [
            d2.loc['/tz2019/sis_v1/v'][['data']].rename(columns={'data': 'V1V'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_h1/v'][['data']].rename(columns={'data': 'H1V'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_v2/v'][['data']].rename(columns={'data': 'V2V'}).astype(float).resample('0.1S').mean(),
            d2.loc['/tz2019/sis_h2/v'][['data']].rename(columns={'data': 'H2V'}).astype(float).resample('0.1S').mean(),
        ],
        axis = 1,
    )

    v1v = numpy.mean(dd['V1V'])
    h1v = numpy.mean(dd['H1V'])
    v2v = numpy.mean(dd['V2V'])
    h2v = numpy.mean(dd['H2V'])

    average = [v1v, h1v, h2v, v2v]

    return average

def att_level_yfactor_plot(att_v, trx, save_name):
    import matplotlib.pyplot as plt
    import std_msgs.msg
    import numpy
    import necstdb
    import exp_yfactor

    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(111)
    ax.plot(att_v, trx)
    ax.set_xlabel('att_i[mA]')
    ax.set_ylabel('Trx or Tsys [K]')
    ax.set_title('att_level_yfactor_plot')
    ax.grid(True)
    fig.savefig('/home/exito/data/logger/test/' + str(save_name) +'att_level_trx_plot.png')






#if __name__ == '__main__':
#iv_plot(file_name, save_name)
