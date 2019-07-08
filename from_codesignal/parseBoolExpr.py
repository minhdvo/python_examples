# Parsing A Boolean Expression
# Return the result of evaluating a given boolean expression, represented as a string.
# An expression can either be:

# "t", evaluating to True;
# "f", evaluating to False;
# "!(expr)", evaluating to the logical NOT of the inner expression expr;
# "&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
# "|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...

# conditions
# 1 <= expression.length <= 20000
# expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f', ','}.
# expression is a valid expression representing a boolean, as given in the description.

# code
from collections import defaultdict
class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        e = expression
        h = 0
        m = defaultdict(list)
        s = []
        for i, c in enumerate(e):
            if c == '(': s.append(i)
            elif c == ')': m[s.pop()].append(i)
            elif c == ',': m[s[-1]].append(i)
        def f(a, b):
            assert a < b
            if a+1 == b: return e[a] == 't'
            assert e[a] in '!&|' and e[a+1] == '(' and e[b-1] == ')'
            assert a+1 in m
            parts = []
            i = a+1
            for j in m[a+1]:
                parts.append(f(i+1,j))
                i = j
            if e[a] == '&': return all(parts)
            if e[a] == '|': return any(parts)
            assert len(parts) == 1
            return not parts[0]
        return f(0, len(e))
