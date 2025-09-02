add(X, Y, Result) :- Result is X + Y.
subtract(X, Y, Result) :- Result is X - Y.
multiply(X, Y, Result) :- Result is X * Y.
divide(X, Y, Result) :- Y \= 0, Result is X / Y.