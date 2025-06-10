# -*- coding: utf-8 -*-
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
# Este script crea un modelo de árbol de decisión para clasificar flores del conjunto de datos Iris
# Importa las librerías necesarias:
iris = (
    load_iris()
)  # Carga el famoso conjunto de datos Iris (información sobre 150 flores)
x = iris.data  # Guarda las características de las flores (como el largo del pétalo, ancho del sépalo, etc.)
y = iris.target  # Guarda el tipo de flor (hay 3 especies diferentes)
# Divide los datos en dos grupos: uno para entrenar el modelo y otro para probarlo
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42
)  # Esta línea divide todos los datos en dos grupos:
# 70% para entrenar el modelo (X_train, y_train),
# 30% para probar qué tan bien funciona (X_test, y_test),
# random_state=42 asegura que siempre obtengamos la misma división aleatoria,
# Crear el modelo de árbol de decisión,
clf = DecisionTreeClassifier(
    random_state=42
)  # Crea un clasificador de árbol de decisión vacio
clf.fit(
    x_train, y_train
)  # Entrena el clasificador con los datos de entrenamiento (X_train, y_train)
# Ahora el modelo ya sabe cómo clasificar las flores basándose en sus características,
# Predecir el tipo de flor en el grupo de prueba,
import numpy as np
# Importa numpy para manejar arreglos y cálculos numéricos,
# Predecir el tipo de flor en el grupo de prueba,

Y_pred = clf.predict(
    x_test
)  # El modelo entrenado ahora predice qué tipo de flor es cada una en el grupo de prueba.
# Y_pred es un arreglo con las predicciones del modelo,
accuracy = (Y_pred == y_test).mean()
print(f"Precision del arbol de decision: {accuracy:.2f}")
# Imprime la precisión del modelo, que es la proporción de predicciones correctas,
# Dibuja el árbol de decisión,
# Importa matplotlib para crear gráficos,
plt.figure(figsize=(12, 8))
plot_tree(
    clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True
)
plt.show()
# Dibuja el árbol de decisión usando plot_tree,
# feature_names muestra los nombres de las características de las flores,
filled=True  # colorea los nodos del árbol según la clase predicha,
# class_names muestra los nombres de las especies de flores,
# y
# plt.figure(figsize=(12, 8)) establece el tamaño del gráfico,
plt.show() # Muestra el gráfico del árbol de decisión,
# El árbol de decisión es una herramienta visual que ayuda a entender cómo el modelo toma decisiones,