"""
This module allows the use of the PySCF software package to run
DFT calculations.
"""

import os
from subprocess import call
import time
import numpy as np
from flare import output
from flare import struc
from typing import List
import pyscf

name = "PySCF"

def run_def_par(dft_input, structure, dft_loc, ncpus = 1, dft_out = "dft.out",
                npool = None, mpi = "mpi", **dft_kwargs):
    """run DFT calculation with given input template
    and atomic configurations. if ncpus == 1, it executes serial run.

    :param dft_input: input template file name
    :param structure: atomic configuration
    :param dft_loc:   relative/absolute executable of the DFT code
    :param ncpus:   # of CPU for mpi
    :param dft_out:   output file name
    :param npool:     not used
    :param mpi:       not used
    :param **dft_wargs: not used
    :return: forces
    """

    newfilename = edit_dft_input_positions(dft_input, structure)

    #TODO: PySCF DFT stuff, write to dft_out

    os.remove(newfilename)

    return parse_dft_forces(dft_out)

def parse_dft_input(dft_input: str):
    """
    Parse a user supplied PySCF input file

    PARAMS:
        dft_input: input file name to parse

    RETURNS:
        postions:
        species:
        cell:
        masses:
    """
    positions, species, cell, masses = [], [], [], []

    with open(dft_input) as f:
        lines = f.readlines()

    cell_index = None
    positions_index = None
    nat = None

    #TODO: PySCF input parser

    for i, line in enumerate(lines):
        cell_index = None

    assert cell_index is not None, 'Failed to find cell in input file'
    assert positions_index is not None, 'Failed to find positions in input'
    assert nat is not None, 'Failed to find number of atoms in input'


