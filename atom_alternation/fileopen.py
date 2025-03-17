import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

list = [1024, 32, 4]
r= 1024+32+4

m = 0
fig, ax = plt.subplots(1, 2, figsize=(20, 10))

# Get matplotlib's default color cycle
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

for i, color in zip(list, colors):
    x = pd.read_csv('eigenvalues_' + str(i) + 'e_2a2b1close.txt', sep='\t', header=None)
    x1 = pd.read_csv('eigenvalues_' + str(i+1) + 'e_2a2b1close.txt', sep='\t', header=None)
    x = x.sort_values(by=0, ascending=True)
    x1 = x1.sort_values(by=0, ascending=True)

    f = np.array(range(1, len(x) + 1))
    f = f / len(x)
    f1 = np.array(range(1, len(x1) + 1))
    f1 = f1 / len(x1)

    # Use the same color for scatter and axhlines
    ax[0].scatter(f, x[0], alpha=0.7, label=str(i) + ' atoms', color=color)
    ax[1].scatter(f1, x1[0], alpha=0.7, label=str(i) + ' atoms', color=color)

    # Full electron line and text for first plot
    full_e_value = x.iloc[int(len(x)/2)-1].values[0]
    ax[0].axhline(y=full_e_value, color=color, linewidth=1,
                  label='Full electron Fermi Level ({:.2f} electrons)'.format(i), linestyle=':')
    ax[0].text(0.95, full_e_value, 'E = {:.4f}'.format(full_e_value),
               style='italic', color=color, ha='right', va='bottom')

    # Half electron line and text for first plot
    half_e_value = x.iloc[int(len(x)/4)-1].values[0]
    ax[0].axhline(y=half_e_value, color=color, linewidth=1,
                     label='Half electron Fermi Level({:.2f} electrons)'.format(i/2), linestyle='--')
    ax[0].text(i/r, half_e_value, 'E = {:.4f}'.format(half_e_value),
               style='italic', color=color, ha='right', va='bottom')

    # Full electron line and text for second plot
    full_e1_value = x1.iloc[int((len(x1)+1)/2)-1].values[0]
    ax[1].axhline(y=full_e1_value, color=color, linewidth=1,
                  label='Full electron Fermi Level({:.2f} electrons)'.format(i+1), linestyle=':')
    ax[1].text(0.95, full_e1_value, 'E = {:.4f}'.format(full_e1_value),
               style='italic', color=color, ha='right', va='bottom')

    # Half electron line and text for second plot
    half_e1_value = x1.iloc[int((len(x1)+3)/4)-1].values[0]
    ax[1].axhline(y=half_e1_value, color=color, linewidth=1,
                  label='Half electron Fermi Level({:.2f} electrons)'.format((i/2+1)), linestyle='--')
    ax[1].text(i/r, half_e1_value, 'E = {:.4f}'.format(half_e1_value),
               style='italic', color=color, ha='right', va='bottom')

    ax[0].set_xlabel('Normalized number of atoms')
    ax[0].set_ylabel('Energy Eigenvalue')
    ax[1].set_xlabel('Normalized number of atoms')
    ax[1].set_ylabel('Energy Eigenvalue')

    m += 1

ax[0].legend()
ax[1].legend()
plt.savefig('eigenvalues_2a2b1close.png')
