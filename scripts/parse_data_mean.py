#!/usr/bin/env python

import sys

def main(residue):
    from MMPBSA_mods import API as MMPBSA_API
    
    data = MMPBSA_API.load_mmpbsa_info('_MMPBSA_info')
    decomp_data = data['decomp']['gb']['complex']['TDC']
    
    # data for given residue
    print(decomp_data[residue])

    # data for all residues
    # print(decomp_data)

if __name__ == '__main__':
    # get residue number (index starts from 1)
    residue = int(sys.argv[1])

    main(residue)
