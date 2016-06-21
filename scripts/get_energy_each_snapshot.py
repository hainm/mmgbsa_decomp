'''pytraj note: changed (a bit) from pandas.io.pickle module
'''
# pandas is distributed under a 3-clause ("Simplified" or "New") BSD
# license.

# Note: full license is in $PYTRAJHOME/license/externals/pandas.txt

from __future__ import print_function
import cPickle as pkl

def to_pickle(obj, path):
    with open(path, 'wb') as f:
        pkl.dump(obj, f, protocol=pkl.HIGHEST_PROTOCOL)

def read_pickle(path):
    with open(path, 'rb') as fh:
        return pkl.load(fh)

if __name__ == '__main__':
    """python ./scripts/get_energy_each_snapshot.py 1be908_wt
    """
    import sys

    pdb_folder = sys.argv[1]
    decomp_data = read_pickle(pdb_folder + '/energy_per_residue_per_structure.pk')

    residue = 1
    energy_term = 'tot'
    print(decomp_data[residue][energy_term])
