# import sys
import matplotlib as plt
import numpy as np
import pandas as pd

if __name__ == "__main__":
    script_name = __file__.split('/')[-1]
    print(f'{script_name}')
    [print(f'\t{x}') for x in locals().values() if callable(x)]
