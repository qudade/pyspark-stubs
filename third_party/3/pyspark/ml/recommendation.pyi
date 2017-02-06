# Stubs for pyspark.ml.recommendation (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from pyspark.ml.util import *
from pyspark.ml.wrapper import JavaEstimator, JavaModel
from pyspark.ml.param.shared import *

class ALS(JavaEstimator, HasCheckpointInterval, HasMaxIter, HasPredictionCol, HasRegParam, HasSeed, JavaMLWritable, JavaMLReadable):
    rank = ...  # type: Any
    numUserBlocks = ...  # type: Any
    numItemBlocks = ...  # type: Any
    implicitPrefs = ...  # type: Any
    alpha = ...  # type: Any
    userCol = ...  # type: Any
    itemCol = ...  # type: Any
    ratingCol = ...  # type: Any
    nonnegative = ...  # type: Any
    intermediateStorageLevel = ...  # type: Any
    finalStorageLevel = ...  # type: Any
    def __init__(self, rank: int = ..., maxIter: int = ..., regParam: float = ..., numUserBlocks: int = ..., numItemBlocks: int = ..., implicitPrefs: bool = ..., alpha: float = ..., userCol: str = ..., itemCol: str = ..., seed: Optional[Any] = ..., ratingCol: str = ..., nonnegative: bool = ..., checkpointInterval: int = ..., intermediateStorageLevel: str = ..., finalStorageLevel: str = ...) -> None: ...
    def setParams(self, rank: int = ..., maxIter: int = ..., regParam: float = ..., numUserBlocks: int = ..., numItemBlocks: int = ..., implicitPrefs: bool = ..., alpha: float = ..., userCol: str = ..., itemCol: str = ..., seed: Optional[Any] = ..., ratingCol: str = ..., nonnegative: bool = ..., checkpointInterval: int = ..., intermediateStorageLevel: str = ..., finalStorageLevel: str = ...): ...
    def setRank(self, value): ...
    def getRank(self): ...
    def setNumUserBlocks(self, value): ...
    def getNumUserBlocks(self): ...
    def setNumItemBlocks(self, value): ...
    def getNumItemBlocks(self): ...
    def setNumBlocks(self, value): ...
    def setImplicitPrefs(self, value): ...
    def getImplicitPrefs(self): ...
    def setAlpha(self, value): ...
    def getAlpha(self): ...
    def setUserCol(self, value): ...
    def getUserCol(self): ...
    def setItemCol(self, value): ...
    def getItemCol(self): ...
    def setRatingCol(self, value): ...
    def getRatingCol(self): ...
    def setNonnegative(self, value): ...
    def getNonnegative(self): ...
    def setIntermediateStorageLevel(self, value): ...
    def getIntermediateStorageLevel(self): ...
    def setFinalStorageLevel(self, value): ...
    def getFinalStorageLevel(self): ...

class ALSModel(JavaModel, JavaMLWritable, JavaMLReadable):
    @property
    def rank(self): ...
    @property
    def userFactors(self): ...
    @property
    def itemFactors(self): ...
