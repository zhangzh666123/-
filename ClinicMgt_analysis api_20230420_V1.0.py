import numpy as np
from sklearn import preprocessing

# 标准化：将数据转换为均值为0，方差为1的数据，即标注正态分布的数据
x = np.array([[1, -1, 2], [2, 0, 0], [0, 1, -1]])
x_scale = preprocessing.scale(x)
print(x_scale.mean(axis=0), x_scale.std(axis=0))

std_scale = preprocessing.StandardScaler().fit(x)
x_std = std_scale.transform(x)
print(x_std.mean(axis=0), x_std.std(axis=0))

# 将数据缩放至给定范围（0-1）
mm_scale = preprocessing.MinMaxScaler()
x_mm = mm_scale.fit_transform(x)
print(x_mm.mean(axis=0), x_mm.std(axis=0))

# 正则化
nor_scale = preprocessing.Normalizer()
x_nor = nor_scale.fit_transform(x)
print(x_nor.mean(axis=0), x_nor.std(axis=0))

# 将分类特征或数据标签转换位独热编码
ohe = preprocessing.OneHotEncoder()
x1 = ([["大象"], ["猴子"], ["老虎"], ["老鼠"]])
x_ohe = ohe.fit(x1).transform([["老虎"]]).toarray()
print(x_ohe)
"""
Machine learning module for Python
==================================

sklearn is a Python module integrating classical machine
learning algorithms in the tightly-knit world of scientific Python
packages (numpy, scipy, matplotlib).

It aims to provide simple and efficient solutions to learning problems
that are accessible to everybody and reusable in various contexts:
machine-learning as a versatile tool for science and engineering.

See http://scikit-learn.org for complete documentation.
"""
import sys
import logging
import os
import random


from ._config import get_config, set_config, config_context

logger = logging.getLogger(__name__)


# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
#
# Generic release markers:
#   X.Y.0   # For first release after an increment in Y
#   X.Y.Z   # For bugfix releases
#
# Admissible pre-release markers:
#   X.Y.ZaN   # Alpha release
#   X.Y.ZbN   # Beta release
#   X.Y.ZrcN  # Release Candidate
#   X.Y.Z     # Final release
#
# Dev branch marker is: 'X.Y.dev' or 'X.Y.devN' where N is an integer.
# 'X.Y.dev0' is the canonical version of 'X.Y.dev'
#
__version__ = "1.2.2"


# On OSX, we can get a runtime error due to multiple OpenMP libraries loaded
# simultaneously. This can happen for instance when calling BLAS inside a
# prange. Setting the following environment variable allows multiple OpenMP
# libraries to be loaded. It should not degrade performances since we manually
# take care of potential over-subcription performance issues, in sections of
# the code where nested OpenMP loops can happen, by dynamically reconfiguring
# the inner OpenMP runtime to temporarily disable it while under the scope of
# the outer OpenMP parallel section.
os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "True")

# Workaround issue discovered in intel-openmp 2019.5:
# https://github.com/ContinuumIO/anaconda-issues/issues/11294
os.environ.setdefault("KMP_INIT_AT_FORK", "FALSE")

try:
    # This variable is injected in the __builtins__ by the build
    # process. It is used to enable importing subpackages of sklearn when
    # the binaries are not built
    # mypy error: Cannot determine type of '__SKLEARN_SETUP__'
    __SKLEARN_SETUP__  # type: ignore
except NameError:
    __SKLEARN_SETUP__ = False

if __SKLEARN_SETUP__:
    sys.stderr.write("Partial import of sklearn during the build process.\n")
    # We are not importing the rest of scikit-learn during the build
    # process, as it may not be compiled yet
else:
    # `_distributor_init` allows distributors to run custom init code.
    # For instance, for the Windows wheel, this is used to pre-load the
    # vcomp shared library runtime for OpenMP embedded in the sklearn/.libs
    # sub-folder.
    # It is necessary to do this prior to importing show_versions as the
    # later is linked to the OpenMP runtime to make it possible to introspect
    # it and importing it first would fail if the OpenMP dll cannot be found.
    from . import _distributor_init  # noqa: F401
    from . import __check_build  # noqa: F401
    from .base import clone
    from .utils._show_versions import show_versions

    __all__ = [
        "calibration",
        "cluster",
        "covariance",
        "cross_decomposition",
        "datasets",
        "decomposition",
        "dummy",
        "ensemble",
        "exceptions",
        "experimental",
        "externals",
        "feature_extraction",
        "feature_selection",
        "gaussian_process",
        "inspection",
        "isotonic",
        "kernel_approximation",
        "kernel_ridge",
        "linear_model",
        "manifold",
        "metrics",
        "mixture",
        "model_selection",
        "multiclass",
        "multioutput",
        "naive_bayes",
        "neighbors",
        "neural_network",
        "pipeline",
        "preprocessing",
        "random_projection",
        "semi_supervised",
        "svm",
        "tree",
        "discriminant_analysis",
        "impute",
        "compose",
        # Non-modules:
        "clone",
        "get_config",
        "set_config",
        "config_context",
        "show_versions",
    ]


def setup_module(module):
    """Fixture for the tests to assure globally controllable seeding of RNGs"""

    import numpy as np

    # Check if a random seed exists in the environment, if not create one.
    _random_seed = os.environ.get("SKLEARN_SEED", None)
    if _random_seed is None:
        _random_seed = np.random.uniform() * np.iinfo(np.int32).max
    _random_seed = int(_random_seed)
    print("I: Seeding RNGs with %r" % _random_seed)
    np.random.seed(_random_seed)
    random.seed(_random_seed)
