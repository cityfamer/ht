# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from typing import (
    Optional,
    Union,
)


def Chen_Bennett(
    m: float,
    x: float,
    D: float,
    rhol: int,
    rhog: float,
    mul: float,
    mug: float,
    kl: float,
    Cpl: int,
    Hvap: float,
    sigma: float,
    dPsat: float,
    Te: int
) -> float: ...


def Chen_Edelstein(
    m: float,
    x: float,
    D: float,
    rhol: int,
    rhog: float,
    mul: float,
    mug: float,
    kl: float,
    Cpl: int,
    Hvap: float,
    sigma: float,
    dPsat: float,
    Te: int
) -> float: ...


def Lazarek_Black(
    m: int,
    D: float,
    mul: float,
    kl: float,
    Hvap: float,
    q: Optional[float] = ...,
    Te: Optional[float] = ...
) -> float: ...


def Li_Wu(
    m: int,
    x: float,
    D: float,
    rhol: float,
    rhog: float,
    mul: float,
    kl: float,
    Hvap: float,
    sigma: float,
    q: Optional[float] = ...,
    Te: Optional[float] = ...
) -> float: ...


def Liu_Winterton(
    m: int,
    x: float,
    D: float,
    rhol: float,
    rhog: float,
    mul: float,
    kl: float,
    Cpl: int,
    MW: float,
    P: float,
    Pc: float,
    Te: int
) -> float: ...


def Sun_Mishima(
    m: int,
    D: float,
    rhol: float,
    rhog: float,
    mul: float,
    kl: float,
    Hvap: float,
    sigma: float,
    q: Optional[float] = ...,
    Te: Optional[float] = ...
) -> float: ...


def Thome(
    m: int,
    x: float,
    D: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    kl: float,
    kg: float,
    Cpl: int,
    Cpg: int,
    Hvap: float,
    sigma: float,
    Psat: float,
    Pc: float,
    q: Optional[float] = ...,
    Te: Optional[float] = ...
) -> float: ...


def Yun_Heo_Kim(
    m: int,
    x: float,
    D: float,
    rhol: float,
    mul: float,
    Hvap: float,
    sigma: float,
    q: Optional[float] = ...,
    Te: Optional[float] = ...
) -> float: ...


def to_solve_q_Thome(
    q: float,
    m: int,
    x: float,
    D: float,
    rhol: float,
    rhog: float,
    kl: float,
    kg: float,
    mul: float,
    mug: float,
    Cpl: int,
    Cpg: int,
    sigma: float,
    Hvap: float,
    Psat: float,
    Pc: float,
    Te: float
) -> float: ...

__all__: List[str]