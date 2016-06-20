#!/bin/sh
#SBATCH -J decomp_pdz
#SBATCH -o decomp_pdz.%J.stdout
#SBATCH -e decomp_pdz.%J.stderr
#SBATCH -p short
#SBATCH -N 4
#SBATCH -t 4:00:00


cd /project1/dacase-001/haichit/rosseta_amber/pdz/PDZ_ddG/results/refine/amber/mmgbsa_decomp

mpirun -n 87 python decomp_mpi.py
