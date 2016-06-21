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

    for residue in decomp_data:
        energy_term = 'tot'
        print('res = {}, energy={}'.format(residue, decomp_data[residue][energy_term]))
