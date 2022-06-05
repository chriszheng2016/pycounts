# read version from installed package
import imp
from importlib.metadata import version

__version__ = version("pycounts")

# populate package namespace
from pycounts.pycounts import count_words
from pycounts.plotting import plot_words
