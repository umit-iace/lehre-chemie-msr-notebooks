import matplotlib.pyplot as plt
import numpy as np

def three_stack_plot(timeDom, zNLin, uNLin, zLinPhy, uLinPhy, bz2Phy, zLinMes, uLinMes, bz2Messung, refLine):
    plt.close()

    _, (axes10, axes20, axes30) = plt.subplots(3, 1, figsize=(12,7), sharex=True)

    axes10.plot(timeDom, zNLin[0, :], label='physikalisch nichtlinear')
    axes10.plot(timeDom, np.ones(len(timeDom)) * refLine, color='r', linewidth=0.8)
    axes20.plot(timeDom, zLinPhy[0, :] + bz2Phy, label='physikalisch linearisiert')
    axes20.plot(timeDom, np.ones(len(timeDom)) * refLine, color='r', linewidth=0.8)
    axes30.plot(timeDom, zLinMes[0, :] + bz2Messung, label='identifiziert')
    axes30.plot(timeDom, np.ones(len(timeDom)) * refLine, color='r', linewidth=0.8)

    axes11 = axes10.twinx()
    axes21 = axes20.twinx()
    axes31 = axes30.twinx()

    axes11.plot(timeDom[:-1:], uNLin[:-1:], color='C4')
    axes11.tick_params(axis='y', labelcolor='C4')

    axes21.plot(timeDom[:-1:], uLinPhy[:-1:], color='C4')
    axes21.tick_params(axis='y', labelcolor='C4')

    axes31.plot(timeDom[:-1:], uLinMes[:-1:], color='C4')
    axes31.tick_params(axis='y', labelcolor='C4')

    axes10.set_ylabel(r'$z_2$ / $m$')
    axes11.set_ylabel(r'$u_{\mathrm{A}}$ / $V$', color='C4')
    axes20.set_ylabel(r'$z_2$ / $m$')
    axes21.set_ylabel(r'$u_{\mathrm{A}}$ / $V$', color='C4')
    axes30.set_ylabel(r'$z_2$ / $m$')
    axes31.set_ylabel(r'$u_{\mathrm{A}}$ / $V$', color='C4')
    axes30.set_xlabel(r'Zeit / $s$')

    axes10.title.set_text('physikalisch nichtlinear')
    axes20.title.set_text('physikalisch linearisiert')
    axes30.title.set_text('identifiziert')

    axes10.grid()
    axes20.grid()
    axes30.grid()
    plt.show()


def three_stack_plot_FF(timeDom, zNLin, z2NLinFF, uNLin, zLinPhy, z2LinPhyFF, uLinPhy, bz2Phy, zLinMes, z2LinMesFF, uLinMes, bz2Messung):
    plt.close()

    fig1, (axes10, axes20, axes30) = plt.subplots(3, 1, figsize=(12,7), sharex=True)

    axes10.plot(timeDom, zNLin[0, :], label='physikalisch nichtlinear')
    axes10.plot(timeDom[:-1], z2NLinFF[:-1] + bz2Messung, label='physikalisch nichtlinear')
    axes20.plot(timeDom, zLinPhy[0, :] + bz2Phy, label='physikalisch linearisiert')
    axes20.plot(timeDom[:-1], z2LinPhyFF[:-1] + bz2Messung, label='physikalisch linearisiert')
    axes30.plot(timeDom, zLinMes[0, :] + bz2Messung, label='identifiziert')
    axes30.plot(timeDom[:-1], z2LinMesFF[:-1] + bz2Messung, label='identifiziert')

    axes11 = axes10.twinx()
    axes21 = axes20.twinx()
    axes31 = axes30.twinx()

    axes11.plot(timeDom[:-1:], uNLin[:-1:], color='C4')
    axes11.tick_params(axis='y', labelcolor='C4')

    axes21.plot(timeDom[:-1:], uLinPhy[:-1:], color='C4')
    axes21.tick_params(axis='y', labelcolor='C4')

    axes31.plot(timeDom[:-1:], uLinMes[:-1:], color='C4')
    axes31.tick_params(axis='y', labelcolor='C4')

    axes10.set_ylabel(r'$z_2$ / $m$')
    axes11.set_ylabel(r'$u_{\mathrm{A}}$ / $V$', color='C4')
    axes20.set_ylabel(r'$z_2$ / $m$')
    axes21.set_ylabel(r'$u_{\mathrm{A}}$ / $V$', color='C4')
    axes30.set_ylabel(r'$z_2$ / $m$')
    axes31.set_ylabel(r'$u_{\mathrm{A}}$ / $V$', color='C4')
    axes30.set_xlabel(r'Zeit / $s$')

    axes10.title.set_text('physikalisch nichtlinear')
    axes20.title.set_text('physikalisch linearisiert')
    axes30.title.set_text('identifiziert')

    axes10.grid()
    axes20.grid()
    axes30.grid()
    plt.show()