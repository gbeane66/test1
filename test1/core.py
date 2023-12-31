# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/new_nb1.ipynb.

# %% auto 0
__all__ = ['exp_decay']

# %% ../nbs/new_nb1.ipynb 3
def exp_decay(t, # first value
        A, # Amplitude
        t0, # t offset
        y0, # y offset
        tau # decay time, tau 
          ):
    return A*np.exp(-((t-t0)/tau)**2) + y0 # exponential decay
