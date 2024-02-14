# `016` Array Border

## 📝 Instrucciones:

1. Crea una matriz con todos los valores iguales a uno (1).

2. Agrega cero (0) a todos los valores que se encuentran en el centro de la matriz.

3. Imprime la matriz en la consola.

## 💻 Resultado Esperado

```bash
[[1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]]
```

## 💡 Pistas:

+ El método `np.ones()` Crea una matriz con todos los valores igual a uno (1). Puedes aprender más sobre este método en este link: https://numpy.org/doc/stable/reference/generated/numpy.ones.html.

+ Si quieres modificar todos los valores del centro (Es decir, todos menos los bordes), puedes hacerlo de esta manera: `matrix[1:-1,1:-1] = "new_value"`
