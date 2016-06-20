@Sagar: Please check "Parse data" section

0. download (@Sagar)

    git clone https://github.com/hainm/mmgbsa_decomp

1. For Hai: Run mmgbsa decomposition (Done)

    ```bash
    # n_proteins = 87
    mpirun -n 87 python decomp_mpi.py

    # update ./mmgbsa.in if needed
    ```

2. Parse data (@Sagar)

    ```bash
    cd 1be908_wt
    python ../scripts/parse_data.py residue_number
    
    # update parse_data.py if needed

    # Expectation: This script will print out the energy for `residue_number` for each component
    # (tot, vwd, eel, ...). Each array has length of n_snapshots (rst7 files)
    # to get a list of those snatshots, see below.
    ```

3. Get list of corrensponding rst7 (coordinates) files (@Sagar)
    
    ```bash
    sh scripts/get_rst7_filelist.sh 1be908_wt
    ```

4. See also (@Sagar)

    ```bash
    Section: "Decomposition Data" in http://ambermd.org/doc12/Amber16.pdf (page 675)
    ```
