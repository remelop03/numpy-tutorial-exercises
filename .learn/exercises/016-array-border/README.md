# `016` Array Border

## 📝 Instructions:

1. Create a matrix with all its values equal to one (1).

2. Add zero (0) to the values that are in the center of the matrix.

3. Print the matrix in the console.

## 💻 Expected Output:

```bash
[[1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]]
```

## 💡 Hints:

+ The `np.ones()` method creates a matrix with all the values equal to one (1). You can read more about this method here: https://numpy.org/doc/stable/reference/generated/numpy.ones.html

+ If you want to modify all the values except for the borders, you should do it this way: `matrix[1:-1,1:-1] = "new_value"`
