import json
from typing import Dict, List, Tuple

from sympy import Symbol, Poly

from . import variables as v


class Tdbx(object):
    """QuesTek's TDBX format class."""

    def __init__(self, tdbx_file: str, elements: List[str]):
        self.filename: str = tdbx_file
        self.uq_traces: Dict[str, Dict[Tuple, List[float]]] = {}
        self.uq_size: int = 0
        self.parameters: List[Dict[str, str]] = []

        self.read_tdbx()
        v.tdbx_file = tdbx_file
        v.elements = elements
        self.get_parameters()

    def read_tdbx(self) -> None:
        """Read and parse a TDBX file."""
        with open(self.filename) as f:
            lines = f.readlines()

        uq_traces = {}
        trace_sizes = []

        for line in lines:
            if line[0] != '$':
                continue

            pieces = line.split()

            if len(pieces) < 4 or pieces[1] != 'UQ':
                continue

            parameter = pieces[2]

            traces = json.loads(' '.join(pieces[3:]))
            new_traces = {}
            for monom, trace in traces.items():
                trace_sizes.append(len(trace))
                new_traces[monom] = trace

            uq_traces[parameter] = new_traces

        uq_size = trace_sizes[0]
        if not all(x == uq_size for x in trace_sizes):
            raise ValueError(f'UQ parameters do not have the same length!\n{trace_sizes}')

        self.uq_size = uq_size
        self.uq_traces = uq_traces

    def get_parameters(self) -> None:
        """Convert UQ traces to Calphad strings."""
        parameters = []
        for index in range(self.uq_size):
            parameter_dict = {}
            for parameter in self.uq_traces.keys():
                poly_exprs = []
                for monom, trace in self.uq_traces[parameter].items():
                    poly_exprs.append(f'{monom} * {trace[index]}')
                expr = Poly('+'.join(poly_exprs), Symbol('T'), domain='RR').as_expr()
                parameter_dict[parameter] = str(expr)
            parameters.append(parameter_dict)
        self.parameters = parameters
