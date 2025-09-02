male(rajesh).
male(sunil).
male(prakash).
male(ramesh).

female(anita).
female(sita).
female(gita).
female(laxmi).

parent(rajesh, sita).
parent(rajesh, sunil).
parent(gita, sita).
parent(gita, sunil).
parent(sunil, prakash).
parent(laxmi, prakash).

% Rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).