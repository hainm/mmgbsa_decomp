import subprocess, os

cm = """
parm ../../{pdb_folder}/prmtop 
trajin ../../{pdb_folder}/no_restraint_new_protocol/min_NoH_*rst7"
"""

for pdb in open('../pdblist.txt').read().split():
    pwd = os.getcwd()
    os.chdir(pdb)
    with open('cpptraj.in', 'w') as fh:
        fh.write(cm.format(pdb_folder=pdb))
    subprocess.check_call('cpptraj -i cpptraj.in > cpptraj.log', shell=True)
    os.chdir(pwd)
