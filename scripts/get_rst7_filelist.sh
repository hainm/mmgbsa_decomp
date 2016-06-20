#!/bin/sh

folder=$1

grep "as Amber NC Restart" $folder/cpptraj.log
