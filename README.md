@Sagar: Please check "Parse data" section

- download (@Sagar)

    git clone https://github.com/hainm/mmgbsa_decomp

- For Hai: Run mmgbsa decomposition (Done)

    ```bash
    # n_proteins = 87
    mpirun -n 87 python decomp_mpi.py

    # update ./mmgbsa.in if needed
    ```

- Average energy (from 50 snapshots) for each residue in each protein

   ```bash
   {pdb_folder}/res.csv
   # tot = vdw  + int + eel + pol + sas

   # int: Internal energy contributions
   # vdw: van der Waals energy contributions
   # eel: Electrostatic energy contributions
   # pol: Polar solvation free energy contributions
   # sas: Non-polar solvation free energy contributions

   # tot: Total free energy contributions (sum of previous 5).
   ```

- Parse data (@Sagar)

    ```bash
    cd 1be908_wt
    python ../scripts/parse_data.py residue_number
    
    # update parse_data.py if needed

    # Expectation: This script will print out the energy for `residue_number` for each component
    # (tot, vwd, eel, ...). Each array has length of n_snapshots (rst7 files)
    # to get a list of those snatshots, see below.

    # and so on for other proteins
    ```

- Get list of corrensponding rst7 (coordinates) files (@Sagar)
    
    ```bash
    sh scripts/get_rst7_filelist.sh 1be908_wt
    ```

- See also (@Sagar)

    ```bash
    Section: "Decomposition Data" in http://ambermd.org/doc12/Amber16.pdf (page 675)
    ```

- Get average energy per residue from 50 snapshots (@Hai)
    
   ```bash
   cd 1be908_wt
   python ../scripts/process_residue.py
   # and so on for other proteins

   # TODO: better name?
   ```
