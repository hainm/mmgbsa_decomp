#!/usr/bin/env python

import sys

def main(residue):
    from MMPBSA_mods import API as MMPBSA_API
    
    data = MMPBSA_API.load_mmpbsa_info('_MMPBSA_info')
    decomp_data = data['decomp']['gb']['complex']['TDC']
    
    # data for residue 1
    print(decomp_data[1])

if __name__ == '__main__':
    # get residue number (index starts from 1)
    residue = sys.argv[1]
    main(residue)
