#!/usr/bin/env python

import sys
import pytraj as pt

def main():
    from MMPBSA_mods import API as MMPBSA_API
    
    data = MMPBSA_API.load_mmpbsa_info('_MMPBSA_info')
    decomp_data = data['decomp']['gb']['complex']['TDC']
    pt.to_pickle(decomp_data, 'energy_per_residue_per_structure.pk')
    
if __name__ == '__main__':
    main()
