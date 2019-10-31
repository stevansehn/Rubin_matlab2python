import scipy.io
import os

# Load the trained parameter matrices for Springer's HSMM model.
# The parameters were trained using 409 heart sounds from MIT heart
# sound database, i.e., recordings a0001-a0409.

dirpath = '/media/linse/dados/stevan/datasets/heart-sound/sources/rubin/matlab'
files = [('Springer_B_matrix'),('Springer_pi_vector'),('Springer_total_obs_distribution')];

SpringerList = []
for fname in files:
    path = os.path.join(dirpath, fname + '.mat')
    mat = scipy.io.loadmat(path)
    SpringerList.append(mat.get(fname))

Springer_B_matrix = SpringerList[0]
Springer_pi_vector = SpringerList[1]
Springer_total_obs_distribution = SpringerList[2]

# Load data and resample data
from default_Springer_HSMM_options import *
springer_options = default_Springer_HSMM_options(SpringerOptions)

print(springer_options.audio_Fs)