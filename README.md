Tutorial sobre scikit-learn
===========================


Este repositorio contiene una serie de material sobre un breve tutorial sobre scikit-learn en Python.


Conseguir el material para el tutorial
------------------

Si tienes una cuenta de Github, la forma más conveniente de bajar el material es realizar un clone del repositorio GitHub o hacer un fork. Puedes clonar el repositorio con el comando:
```bash
git clone https://github.com/pagutierrez/tutorial-sklearn.git

```

Si no estás familiarizado con GitHub o no tienes cuenta, también puedes bajar todo el repositorio como un archivo `.zip`, accediendo a ``Clone or download`` en la cabecera del repositorio (https://github.com/pagutierrez/tutorial-sklearn) y pulsando sobre ``Download ZIP``.

![](images/download-repo.png)

Por favor, ten en cuenta que los contenidos del repositorio pueden cambiar a última hora, así que recomendamos que intentes actualizar los contenidos antes de cada sesión. Si tienes una cuenta de GitHub y has clonado el repositorio, solo tienes que usar el comando:
```bash
git pull origin master
```
En otro caso, tendrás que descargar de nuevo el `.zip` cada vez que quieras actualizar los ficheros.


Notas de instalación
--------------------

Este tutorial requiere tener instalaciones lo más recientes posibles de:

- [NumPy](http://www.numpy.org)
- [SciPy](http://www.scipy.org)
- [matplotlib](http://matplotlib.org)
- [pandas](http://pandas.pydata.org)
- [pillow](https://python-pillow.org)
- [scikit-learn](http://scikit-learn.org/stable/)
- [IPython](http://ipython.readthedocs.org/en/stable/)
- [Jupyter Notebook](http://jupyter.org)


Este último es importante. Si lo tienes correctamente instalado, deberías poder teclear:
```bash
    jupyter notebook
```
en tu terminal de comandos y ver el panel de carga de libros de notas en tu navegador web. Intenta abrir y ejecutar cualquiera de los libros que contiene este curso, para ver si funciona todo correctamente.

Para aquellos usuarios que no tengan las dependencias instaladas, una forma relativamente sencilla de conseguirlas es utilizar una distribución de Python como [Anaconda CE](http://store.continuum.io/ "Anaconda CE"), que incluye los paquetes de Python más relevantes para ciencia, matemáticas, ingeniería y análisis de datos. Anaconda puede descargarse e instalarse de forma libre, incluyendo el uso comercial y la redistribución. Los códigos incluidos en este tutorial deberían ser compatibles con Python 2.7 y Python 3.4-3.6. Suponiendo que tengas Anaconda instalado, los siguientes comandos crean un entorno nuevo llamado `sklearn-env` e instalan todas las dependencias:
```bash
conda update conda
conda update anaconda
conda create --prefix ~/sklearn-env scikit-learn
source activate sklearn-env
conda install matplotlib
conda install ipython
conda install pandas
conda install Pillow
```

Tras obtener el material, **recomendamos encarecidamente** abrir y ejecutar el libro de notas ``check_env.ipynb``, que se encuentra en la raíz del repositorio. Para ello, ejecuta el comando:
```bash
jupyter notebook check_env.ipynb
```
Una vez dentro del libro, ejecuta la única celda de código pulsando sobre el botón "Run Cells", tal y como muestra esta figura:

![](images/check_env-1.png)

Si tu entorno satisface todos los requisitos para el tutorial, el código ejecutado debería mostrar una salida como la siguiente:

![](images/check_env-2.png)

Aunque no sea un requisito, te recomendamos actualizar los paquetes Python a su ultima versión, para así asegurar la mejor compatibilidad con el material didáctico. Puedes actualizar los paquetes con los comandos:
```bash
pip install [package-name] --upgrade
```


Descarga de las bases de datos
--------------

Los datos para este tutorial no están incluidos en el repositorio. Vamos a utilizar varios datasets: muchos vienen en scikit-learn, el cuál descarga y guarda los datos.

Debido a que la red puede fallar, sería una buena idea descargar algunos de los datasets (los más pesados) antes de las clases. Por favor, ejecuta:
```bash
python fetch_data.py
```
para descargar estos datasets.

El tamaño de la descarga de los ficheros es, aproximadamente, 280MB y, una vez extraídos en disco ocuparán unos 480MB de tu disco duro.


Temas
=======


- 01. Introducción a aprendizaje automático en Python [[notebook](notebooks-spanish/01-introduccion_aprendizaje_automatico.ipynb)][[html](notebooks-spanish/01-introduccion_aprendizaje_automatico.html)]
- 02. Herramientas científicas en Python [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 03. Representación y visualización de datos [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 04. Aprendizaje supervisado: entrenamiento y test [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 05. Aprendizaje supervisado: clasificación [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 06. Aprendizaje supervisado: regresión [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 07. Aprendizaje no supervisado: transformación [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 08. Aprendizaje no supervisado: agrupamiento [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 09. Un resumen de la interfaz Estimator de scikit-learn [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 10. Caso de estudio - Supervivencia en el Titanic [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 11. Extracción de características de un texto mediante Bag-of-Words (bolsas de palabras) [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 12. Caso de estudio - Clasificación de texto para detección de spam en SMS [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 13. Validación cruzada y métodos de evaluación de rendimiento [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 14. Selección de parámetros, validación y test [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 15. Encadenamiento con tuberías [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 16. Aprendizaje supervisado: evaluación de modelos, métricas de puntuación y manejo de conjuntos de datos no balanceados [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 17. Aprendizaje supervisado: modelos lineales [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 18. Aprendizaje supervisado: árboles de decisión y bosques aleatorios [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 19. Selección de características [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 20. Aprendizaje no supervisado: agrupamiento jerárquico y métodos basados en densidades [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 21. Aprendizaje no supervisado: reducción de la dimensionalidad no lineal [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 22. Aprendizaje no supervisado: detección de anomalías [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
- 23. *Out-of-core learning* [[notebook](notebooks-spanish/)][[html](notebooks-spanish/)]
