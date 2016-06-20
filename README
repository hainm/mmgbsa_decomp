0. download

    git clone https://github.com/hainm/mmgbsa_decomp

1. Run mmgbsa decomposition

    # n_proteins = 87
    mpirun -n 87 python decomp_mpi.py

    # update ./mmgbsa.in if needed

2. Parse data

    cd 1be908_wt
    python ../scripts/parse_data.py residue_number
    
    # update parse_data.py if needed

    # Expectation: This script will print out the energy for `residue_number` for each component
    # (tot, vwd, eel, ...). Each array has length of n_snapshots (rst7 files)
    # to get a list of those snatshots, see below.

3. Get list of corrensponding rst7 (coordinates) files:
    
    sh scripts/get_rst7_filelist.sh 1be908_wt

4. See also:

    Section: "Decomposition Data" in http://ambermd.org/doc12/Amber16.pdf (page 675)
