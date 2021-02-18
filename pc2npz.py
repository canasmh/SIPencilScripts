# $Id: pc2npz.py 
#
# Convert data from PencilCode format to npz files (Numpy zip file). 
#
# Author: Manuel H. Canas (canasmh@nmsu.edu)

from pencil_old import read_var, read_pvar, read_dim, read_ts, read_grid
import numpy as np
import os.path
import re


def pc2npz(ivar=-1, datadir="data", files="all", quiet=True, trimall=True):
    """Convert pencil outputs to npz files.

    Pencil files can be extremely large, making it difficult to transfer files from a remote location to your local machine.
    This function helps mitigate that issue by reading these large files and converting them into npz files that are much 
    easier to transfer. 

    Inputs:
        ivar (int) -- The specific VAR and PVAR file you would like to read. Defaults to -1 (i.e., read var.dat, pvar.dat)
        datadir (str) -- Path to the data directory. Defaults to "data".
        quiet (bool) -- Suppress much of the print statements when reading the files. Defaults to True
        trimall (bool) -- Trim the ghost zones from the f array. Defaults to True.
    
    Returns:
         None

    """

    datadir2 = datadir + "/"

    if ivar < 0:
        varfile  = "var.dat"
        pvarfile = "pvar.dat"
        ts_file = "ts.npz"
        dim_file = "dim.npz"
        grid_file = "grid.npz"
        ff_file = "ff.npz"
        fp_file = "fp.npz"
    else:
        varfile  = "VAR" + str(ivar)
        pvarfile = "PVAR" + str(ivar)
        ts_file = "ts{}.npz".format(ivar)
        dim_file = "dim{}.npz".format(ivar)
        grid_file = "grid{}.npz".format(ivar)
        ff_file = "ff{}.npz".format(ivar)
        fp_file = "fp{}.npz".format(ivar)

    if "ts" in files or "all" in files:
        print("Reading time series")
        print(" ")
        ts = read_ts(datadir=datadir2)
        print(" ")
        ts_vars = vars(ts)
        print("Saving time series as {}".format(ts_file))
        np.savez(ts_file, **ts_vars)
        print("...")
        print("...")

    if "dim" in files or "all" in files:
        print("Reading dim files")
        print(" ")
        dim = read_dim(datadir=datadir2)
        print(" ")
        dim_vars = vars(dim)
        print("Saving dim files as {}".format(dim_file))
        np.savez(dim_file, **dim_vars)
        print("...")
        print("...")

    if "grid" in files or "all" in files:

        print("Reading grid files")
        print(" ")
        grid = read_grid(datadir=datadir2, quiet=quiet)
        print(" ")
        grid_vars = vars(grid)
        print("Saving grid files as {}".format(grid_file))
        np.savez(grid_file, **grid_vars)
        print("...")
        print("...")
        print("Finished...")

    if "ff" in files or "all" in files:
        print("Reading {} (this might take a while) ...".format(varfile))
        print(" ")
        var = read_var(datadir=datadir, trimall=trimall, quiet=quiet, varfile=varfile)
        print(" ")
        var_vars = vars(var)
        print("Saving var files as {}".format(ff_file))
        np.savez(ff_file, **var_vars)
        print("...")
        print("...")

    if "fp" in files or "all" in files:
        print("Reading {} (this might take a while) ...".format(pvarfile))
        print(" ")
        pvar = read_pvar(datadir=datadir2, varfile=pvarfile)
        print(" ")
        pvar_vars = vars(pvar)
        print("Saving pvar files as {}".format(fp_file))
        np.savez(fp_file, **pvar_vars)
        print("...")
        print("...")


def read_ts(filename='time_series.dat', datadir = 'data', comment_char='#', quiet=True):

    datadir = os.path.expanduser(datadir)
    infile = open(os.path.join(datadir, filename), "r")
    lines = infile.readlines()
    infile.close()

    nlines_init = len(lines)

    if not quiet:
        print("Reading {} lines".format(nlines_init))

    data_dict = {}
    nlines = 1
    for line in lines:

        # Check if line is a header
        if re.search("^%s--" % comment_char, line):

            # Read header
            header = line.strip("%s-\n" % comment_char)
            keys_new = re.split("-+", line)
            print(keys_new)

        else:
            continue






