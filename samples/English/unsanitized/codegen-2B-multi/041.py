

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
    assert 0 <= n <= 1000

    # Initialize car positions and speeds.
    car1_pos = 0
    car2_pos = n
    max_speed = 20

    # While speed difference is not zero, continue iteratively.
    while max_speed > 0:
        # Determine position of both cars.
        car1_pos += max_speed * n
        car2_pos -= max_speed * n

        max_speed *= 0.5

        # Check if car1 collides with car2.
        if car1_pos >= n and car2_pos >= car1_pos:
            car1_pos -= n
            break

    # If either car collides, the function returns 1.
    return car1_pos >= car2_pos


# Driver function (main).
