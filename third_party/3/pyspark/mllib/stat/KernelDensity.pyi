# Stubs for pyspark.mllib.stat.KernelDensity (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

xrange = ...  # type: Any

class KernelDensity:
    def __init__(self) -> None: ...
    def setBandwidth(self, bandwidth): ...
    def setSample(self, sample): ...
    def estimate(self, points): ...