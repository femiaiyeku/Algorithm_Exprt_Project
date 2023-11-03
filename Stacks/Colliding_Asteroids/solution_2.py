"""
You're given an array of integers asteroids, where each Integer represents the size of an asterold. The sign of
the integer represents the direction the asteroid is moving (positive-right, negative=left). All asteroids move at
the same speed, meaning that two asteroids moving in the same direction can never collide.
For example, the integer 4 represents an asterold of size 4 moving to the right. Similarly, -7 represents an
asteroid of size 7 moving to the left.
If two asteroids collide, the smaller asterold (based on absolute value) explodes. If two colliding asterolds are the
same size, they both explode.
Write a function that takes in this array of asterolds and returns an array of Integers representing the asterolds
after all collisions occur.


Sample Input:
asteroids = [-5, 10, -15]

Sample Output:
[-5, 10]

Explanation:
-5 and 10 never collide because they move in the same direction.
-15 collides with 10, and -15 explodes.
10 collides with -5, and -5 explodes.

Sample Input:
asteroids = [-5, -5, -5, -5]

Sample Output:
[]
Explanation:
All asteroids collide and explode.



"""

def collidingAsteroids(asteroids):
    resultStack = []
    for asteroid in asteroids:
        if asteroid > 0:
            resultStack.append(asteroid)
            continue

        while len(resultStack) > 0 and resultStack[-1] > 0 and resultStack[-1] < abs(asteroid):
            resultStack.pop()

        if len(resultStack) == 0 or resultStack[-1] < 0:
            resultStack.append(asteroid)
            continue

        if resultStack[-1] == abs(asteroid):
            resultStack.pop()

    return resultStack