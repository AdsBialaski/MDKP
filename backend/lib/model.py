from pydantic import BaseModel


class ParameterCostFunction(BaseModel):
    storage: str
    memory: str
    cpu_time: str
    worker_time: str


class ProjectInfo(BaseModel):
    storage: int
    memory: int
    cpu_time: int
    worker_time: int
    value: int


class RunParams(BaseModel):
    config: ParameterCostFunction
    projects: list[ProjectInfo]
