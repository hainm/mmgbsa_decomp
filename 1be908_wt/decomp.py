#!/usr/bin/evn python
import subprocess

def main():
    command = "MMPBSA.py -i ../mmgbsa.in -cp ../../{pdb_folder}/prmtop -y ../../{pdb_folder}/no_restraint_new_protocol/min_NoH_*rst7"
    pdb_folder = '1be908_wt'
    
    print('processing {}'.format(pdb_folder))
    subprocess.check_call(command.format(pdb_folder=pdb_folder).split())

if __name__ == '__main__':
    main()
