# -*- coding: utf-8 -*-
"""BP_decisionTree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17iClaatBBN0QzINuOZOVPzP4PEYlgeiP

Lien vers le dataset : https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction

# Bibliothèque
"""

from google.colab import drive # pour importer le dataset depuis drive
import pandas as pd # pr manipuler les dataframes
import numpy as np # pour créer des matrices
import matplotlib.pyplot as plt # pour tracer des graphiques
import seaborn as sns # pour la visualisation de la data

"""# Chargement du dataset"""

drive.mount('/content/drive')
dataset = pd.read_csv('/content/drive/MyDrive/Projet-MachineLearning/dataset.csv') # chemin vers le dataset
#print(dataset.head())
print(dataset.shape)
print(dataset.columns)
#print(dataset.columns)

X = dataset.drop('Bankrupt?', axis=1)

y = dataset['Bankrupt?']
import seaborn as sns
sns.countplot(x=y)
plt.figure(figsize=(15, 4))

plt.scatter(X.iloc[:, 0], y, c=y)
# plt.scatter(X['column_name1'], X['column_name2'], c=y)

"""# Arbre de décision

# Impureté de Gini
"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
# séparation des données de test et train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
clf = DecisionTreeClassifier()
# %time
clf.fit(X_train, y_train)

# profondeur de l'arbre
max_depth = clf.get_depth()
print(max_depth) # on a 20 niveaux : noeud racine + 19 couches

"""# Evaluation"""

y_pred = clf.predict(X_test)
from sklearn import metrics
# rapport de classification
print(metrics.classification_report(y_test, y_pred))
# matrice de confusion
confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
cm_diplay = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=clf.classes_)
cm_diplay.plot()
plt.show()

from sklearn import tree
tree.plot_tree(clf, rounded=True, filled=True)
plt.show

"""# Entropie"""

# Commented out IPython magic to ensure Python compatibility.
clf = DecisionTreeClassifier(criterion='entropy')
# %time
clf.fit(X_train, y_train)

max_depth = clf.get_depth()
print(max_depth) # on a 20 niveaux : noeud racine + 19 couches

tree.plot_tree(clf, rounded=True, filled=True)
plt.show

"""# Remarque
L'entrainement est plus court en utilisant l'impureté de Gini

# Evaluation
"""

y_pred = clf.predict(X_test)
print(metrics.classification_report(y_test, y_pred))
confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix)

cm_display.plot()
plt.show()