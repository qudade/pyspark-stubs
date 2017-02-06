# Stubs for pyspark.ml.tuning (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from pyspark.ml import Estimator, Model
from pyspark.ml.param.shared import HasSeed

class ParamGridBuilder:
    def __init__(self) -> None: ...
    def addGrid(self, param, values): ...
    def baseOn(self, *args): ...
    def build(self): ...

class ValidatorParams(HasSeed):
    estimator = ...  # type: Any
    estimatorParamMaps = ...  # type: Any
    evaluator = ...  # type: Any
    def setEstimator(self, value): ...
    def getEstimator(self): ...
    def setEstimatorParamMaps(self, value): ...
    def getEstimatorParamMaps(self): ...
    def setEvaluator(self, value): ...
    def getEvaluator(self): ...

class CrossValidator(Estimator, ValidatorParams):
    numFolds = ...  # type: Any
    def __init__(self, estimator: Optional[Any] = ..., estimatorParamMaps: Optional[Any] = ..., evaluator: Optional[Any] = ..., numFolds: int = ..., seed: Optional[Any] = ...) -> None: ...
    def setParams(self, estimator: Optional[Any] = ..., estimatorParamMaps: Optional[Any] = ..., evaluator: Optional[Any] = ..., numFolds: int = ..., seed: Optional[Any] = ...): ...
    def setNumFolds(self, value): ...
    def getNumFolds(self): ...
    def copy(self, extra: Optional[Any] = ...): ...

class CrossValidatorModel(Model, ValidatorParams):
    bestModel = ...  # type: Any
    avgMetrics = ...  # type: Any
    def __init__(self, bestModel, avgMetrics: Any = ...) -> None: ...
    def copy(self, extra: Optional[Any] = ...): ...

class TrainValidationSplit(Estimator, ValidatorParams):
    trainRatio = ...  # type: Any
    def __init__(self, estimator: Optional[Any] = ..., estimatorParamMaps: Optional[Any] = ..., evaluator: Optional[Any] = ..., trainRatio: float = ..., seed: Optional[Any] = ...) -> None: ...
    def setParams(self, estimator: Optional[Any] = ..., estimatorParamMaps: Optional[Any] = ..., evaluator: Optional[Any] = ..., trainRatio: float = ..., seed: Optional[Any] = ...): ...
    def setTrainRatio(self, value): ...
    def getTrainRatio(self): ...
    def copy(self, extra: Optional[Any] = ...): ...

class TrainValidationSplitModel(Model, ValidatorParams):
    bestModel = ...  # type: Any
    validationMetrics = ...  # type: Any
    def __init__(self, bestModel, validationMetrics: Any = ...) -> None: ...
    def copy(self, extra: Optional[Any] = ...): ...
