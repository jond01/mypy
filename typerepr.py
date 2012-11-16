"""Representation classes for Typ subclasses and TypeVars.

These are used for source-source transformation that preserves original
formatting and comments.
"""

from lex import Token


class CommonTypeRepr:
    """Representation of UnboundType, Instance and Callable."""
    void __init__(self, list<Token> components,  langle, list<Token> commas,
                  any rangle):
        # Note: langle and rangle may be empty.
        self.components = components
        self.langle = langle
        self.commas = commas
        self.rangle = rangle


class AnyRepr:
    """Representation of Any."""
    void __init__(self, any any_tok):
        self.any_tok = any_tok


class VoidRepr:
    """Representation of Void."""
    void __init__(self, any void):
        self.void = void


class TypeVarRepr:
    """Representation of TypeVar."""
    void __init__(self, any name):
        self.name = name


class TypeVarsRepr:
    """Representation of TypeVars."""
    void __init__(self, any langle, list<Token> commas, any rangle):
        self.langle = langle
        self.commas = commas
        self.rangle = rangle


class TypeVarDefRepr:
    """Representation of TypeVarDef."""
    void __init__(self, any name, any is_tok):
        # TODO remove is_tok
        self.name = name
        self.is_tok = is_tok
