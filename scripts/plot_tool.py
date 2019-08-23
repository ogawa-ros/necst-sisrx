#!/usr/bin/env python3

def yfactor_plot(file_name, save_name, thot, tcold):
    import os, sys
    import matplotlib.pyplot as plt
    import std_msgs.msg
    import pandas
    import numpy
    import necstdb
    import exp_yfactor
    from statistics import mean,stdev
    db = necstdb.necstdb()  #plot graph
    db.open(file_name)

    d = db.read_as_pandas()
    d['time'] = pandas.to_datetime(d['time'], unit='s')
    d['data'] = [_[0]['data'] for _ in d['msgs']]
    d2 = d.set_index(['topic', 'time']).sort_index()
    sadata = d2.loc['/dev/n9343c/ip_192_168_100_185/spec'][['data']]
    trxarray = []

    p = numpy.array(sadata)
    plen = range(len(p))
    for i in plen:
        power = p[i][0]
        trx = exp_yfactor.evaluate_trx_from_rotating_chopper_data(power, thot, tcold)
        trxarray.append(trx)
        fig = plt.figure(figsize=(8,4))
        ax = fig.add_subplot(111)
        ax.plot(power)
        ax.set_xlabel('time')
        ax.set_ylabel('power (dBm)')
        ax.set_title('yfactor-measurement')
        ax.grid(True)
        fig.savefig('/home/exito/data/logger/test/' + str(save_name) +'/'+str(i)+'_yfactor_plot.png')
        continue

    #print(trxarray)
    trxave = mean(trxarray)
    stdev = stdev(trxarray)
    print("trxave = "+ str(trxave))
    print("stdev = "+ str(stdev))

    return trxave

def yfactor_cal(file_name, thot, tcold):
    import os, sys
    import matplotlib.pyplot as plt
    import std_msgs.msg
    import pandas
    import numpy
    import necstdb
    import exp_yfactor
    from statistics import mean,stdev
    import pathlib
    import pandas
    import matplotlib.pyplot
    import necstdb
    import IPython.display

    # data base にアクセス
    db_name = 'result.necstdb'
    db = necstdb.opendb(db_name)
    db.list_tables()
    IPython.display.clear_output()

    # 読み出す table を選択
    sa_list = [
        'dev-n9343c-ip_192_168_100_185-spec',
    ]
    # table open
    tb_sa = [db.open_table(i) for i in sa_list]
    df_sa = [i.read(astype='pandas') for i in tb_sa]

    sa = numpy.array(df_sa[0])
    salen = range(len(sa))
    trxarray = []
    for i in salen:
        sadata = sa[i]
        trx = evaluate_trx_from_rotating_chopper_data(sadata[0], thot, tcold)
        trxarray.append(trx)

    trxave = mean(trxarray)
    stdev = stdev(trxarray)

    return trxave



def sis_vol_average(file_name):
    import std_msgs.msg
    import numpy
    import necstdb
    import pandas
    %matplotlib inline
    import pathlib
    import pandas
    import matplotlib.pyplot
    import necstdb
    import IPython.display

    # data base にアクセス
    db_name = 'result.necstdb'
    db = necstdb.opendb(db_name)
    db.list_tables()
    IPython.display.clear_output()

    # 読み出す table を選択
    sa_list = [
        'dev-n9343c-ip_192_168_100_185-spec',
    ]

    v_list = [
        'tz2019-sis_v1-v',
        'tz2019-sis_h1-v',
        'tz2019-sis_h2-v',
        'tz2019-sis_v2-v',
    ]

    i_list = [
        'tz2019-sis_h1-i',
        'tz2019-sis_h2-i',
        'tz2019-sis_v1-i',
        'tz2019-sis_v2-i',
    ]


    # table open
    tb_sa = [db.open_table(i) for i in sa_list]
    tb_v = [db.open_table(i) for i in v_list]
    tb_i = [db.open_table(i) for i in i_list]

    df_sa = [i.read(astype='pandas') for i in tb_sa]
    df_v = [i.read(astype='pandas') for i in tb_v]
    df_i = [i.read(astype='pandas') for i in tb_i]


    # pandas として読み出し
    for i in df_v:
        i['timestamp'] = pandas.to_datetime(i['timestamp'], unit='s')

    for j in df_i:
        j['timestamp'] = pandas.to_datetime(j['timestamp'], unit='s')

    for i in df_sa:
        i['timestamp'] = pandas.to_datetime(i['timestamp'], unit='s')


    # timestamp を index に設定して時間でソート
    df_sa = [i.set_index('timestamp').sort_index() for i in df_sa]
    df_v = [i.set_index('timestamp').sort_index() for i in df_v]
    df_i = [i.set_index('timestamp').sort_index() for i in df_i]
    #df_p = [i.set_index('timestamp').sort_index() for i in df_p]


    v1v = numpy.mean(df['V1V'])
    h1v = numpy.mean(df['H1V'])
    v2v = numpy.mean(df['V2V'])
    h2v = numpy.mean(df['H2V'])

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
    fig.savefig('/home/exito/data/logger/test/' + str(save_name) +'/att_level_trx_plot.png')






#if __name__ == '__main__':
#iv_plot(file_name, save_name)
