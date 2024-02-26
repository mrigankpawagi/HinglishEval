

def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    cars = { (car[0], car[1], car[2]) : True for car in zip(*n)}
    accumulator = 0

    # We have to iterate over every pair of cars in the matrix.   Any collisions occur
    # when each pair of cars is left-to-right and right-to-left, or vice versa.
    for car0, car1 in itertools.combinations(range(n, 0, -1), 2):
        # A car goes right if it is the even-index (row) car, because it starts
        # after the other car.  We can get there with if statements after reversing,
        # but this will do it much faster when it looks like this.
        if car0 % 2 ^ car1 % 2:
            cars[(car0, car1)] = False

    # now scan through every pair of car positions to see if they collide
    for car0, car1 in cars.keys():
        if not cars[(car0, car1)]:
            # there are no collisions for this pair so go on
            continue
        # now we know we have to check the position of those car.  But we might
        # have to flip order in case they move the other way, and check again.
        # we remember that we can flip the left car, do the scan, then flip it back
        # back to the right pair.  Repeat until we find a direction that produces no
        # new collisions.
        pairs = []
        while True:
            # flip the left car,