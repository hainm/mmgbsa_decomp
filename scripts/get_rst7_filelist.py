import sys

def get_filelist(pdb_folder):
    filelist = None
    with open(pdb_folder + '/_MMPBSA_info') as fh:
        for line in fh:
            if line.startswith("FILES.mdcrd"):
                filelist = eval(line.split('=')[-1])
    return filelist

if __name__ == '__main__':
    """
    Examples

    python scripts/get_rst7_filelist.py 1be908_wt
    """
    for pdb in get_filelist(sys.argv[1]):
        print(pdb)
