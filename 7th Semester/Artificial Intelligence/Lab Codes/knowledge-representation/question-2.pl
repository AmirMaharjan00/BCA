animal(elephant).
animal(horse).
animal(dog).
animal(cat).

bigger_than(elephant, horse).
bigger_than(horse, dog).
bigger_than(dog, cat).

is_bigger(X, Y) :- bigger_than(X, Y).
is_bigger(X, Y) :- bigger_than(X, Z), is_bigger(Z, Y).