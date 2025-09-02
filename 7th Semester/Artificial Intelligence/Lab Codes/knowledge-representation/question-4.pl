loves(likesh, lumanti).
loves(lumanti, likesh).
man(likesh).
woman(lumanti).
likes(om, yomari).
likes(puza, samebaji).
parent(om, sangita).
parent(puza, sangita).
parent(anish, om).

father(X, Y) :- parent(X, Y), man(X).
mother(X, Y) :- parent(X, Y), woman(X).
lovers(X, Y) :- loves(X, Y), loves(Y, X).