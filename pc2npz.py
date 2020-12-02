# $Id: pc2npz.py 
#
# Convert data from PencilCode format to npz files (Numpy zip file). 
#
# Author: Manuel H. Canas (canasmh@nmsu.edu)

from pencil_old import read_var, read_pvar, read_dim, read_ts, read_grid
import numpy as np


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
    else:
        varfile  = "VAR" + str(ivar)
        pvarfile = "PVAR" + str(ivar)

    if "ts" in files or "all" in files:
        print("Reading time series")
        print(" ")
        ts = read_ts(datadir=datadir2)
        print(" ")
        ts_vars = vars(ts)
        print("Saving time series as ts{}.npz".format(ivar))
        np.savez("ts{}.npz".format(ivar), **ts_vars)
        print("...")
        print("...")

    if "dim" in files or "all" in files:
        print("Reading dim files")
        print(" ")
        dim = read_dim(datadir=datadir2)
        print(" ")
        dim_vars = vars(dim)
        print("Saving dim files as dim{}.npz".format(ivar))
        np.savez("dim{}.npz".format(ivar), **dim_vars)
        print("...")
        print("...")

    if "grid" in files or "all" in files:

        print("Reading grid files")
        print(" ")
        grid = read_grid(datadir=datadir2, quiet=quiet)
        print(" ")
        grid_vars = vars(grid)
        print("Saving grid files as grid{}.npz".format(ivar))
        np.savez("grid{}.npz".format(ivar), **grid_vars)
        print("...")
        print("...")
        print("Finished...")

    if "ff" in files or "all" in files:
        print("Reading {} (this might take a while) ...".format(varfile))
        print(" ")
        var = read_var(datadir=datadir, trimall=trimall, quiet=quiet, varfile=varfile)
        print(" ")
        var_vars = vars(var)
        print("Saving var files as ff{}.npz".format(ivar))
        np.savez("ff{}.npz".format(ivar), **var_vars)
        print("...")
        print("...")

    if "fp" in files or "all" in files:
        print("Reading {} (this might take a while) ...".format(pvarfile))
        print(" ")
        pvar = read_pvar(datadir=datadir2, varfile=pvarfile)
        print(" ")
        pvar_vars = vars(pvar)
        print("Saving pvar files as fp{}.npz".format(ivar))
        np.savez("fp{}.npz".format(ivar), **pvar_vars)
        print("...")
        print("...")

