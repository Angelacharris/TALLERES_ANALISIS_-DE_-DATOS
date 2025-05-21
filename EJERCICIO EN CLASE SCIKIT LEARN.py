import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer


# 1. Crear un conjunto de datos ficticio
np.random.seed(42)  # Para reproducibilidad

n_samples = 200

# Características
frecuencia = np.random.randint(1, 100, size=n_samples)  # días desde última compra
monto_gastado = np.random.uniform(10, 1000, size=n_samples)  # USD
visitas = np.random.randint(1, 50, size=n_samples)  # número de visitas
# Crear etiquetas basadas en reglas simples
# Por ejemplo, clientes frecuentes: frecuencia < 30, monto > 300, visitas > 10
labels = []
for f, m, v in zip(frecuencia, monto_gastado, visitas):
    if f < 30 and m > 300 and v > 10:
        labels.append('Frecuente')
    elif f > 60 and m < 200 and v < 10:
        labels.append('Nuevo')
    else:
        labels.append('Ocasional')
# Crear DataFrame
data = pd.DataFrame({
    'Frecuencia': frecuencia,
    'Monto': monto_gastado,
    'Visitas': visitas,
    'Clase': labels
})
# Convertir etiquetas a números
label_mapping = {'Frecuente':1, 'Ocasional': 2, 'Nuevo': 2}
data['Clase_num'] = data['Clase'].map(label_mapping)

# 2. Dividir en conjunto de entrenamiento y prueba
X = data[['Frecuencia', 'Monto', 'Visitas']]
y = data['Clase_num']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Entrenar un modelo KNN con n_neighbors=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 4. Realizar predicciones sobre el conjunto de prueba
y_pred = knn.predict(X_test)

# 5. Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

# 6. Generar y visualizar la matriz de confusión
cm = confusion_matrix(y_test, y_pred)

# Mapear etiquetas para la visualización
labels = ['Frecuente', 'Ocasional', 'Nuevo']

plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.xlabel('Predicción')
plt.ylabel('Real')
plt.title('Matriz de Confusión')
plt.show()

