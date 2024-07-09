
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    
    return b > a and b < c


if __name__ == "__main__":
    c = [1,4,7,10]
    res = right_angle_triangle(3, 4, c[0]) == True
    print(res)
    c = [1,2,3,5,8,7]
    res = right_angle_triangle(3, 4, c[0]) == True
    print(res)
    res = right_angle_triangle(3, 4, c[1]) == False
    print(res)

```

## 参考

  * [https://www.jianshu.com/p/d6ce8de8d966](https://www.jianshu.com/p/d6ce8de8d966)
  * [专门制作好函数与函数的运算符号的革命](http://www.ruanyifeng.com/blog/2017/06/coding_revolution.html)
  * [https://www.reddit.com/r/functions/comments/6r4x5d/coding_revolution_explains_function/](https://www.reddit.com/r/functions/comments/6r4x5d/coding_revolution_explains_function/)

