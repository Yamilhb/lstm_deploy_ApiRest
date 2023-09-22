# lstm_deploy_ApiRest
Se realiza el deploy vía API REST del modelo LSTM visto en la Repo **basic-sklearn-pipeline**.

### 1.construccion
Primero se realiza el proceso de desarrollo en la carpeta *1.construcción*, donde el criterio de éxito es la correcta ejecucón de *tox -e train* y *tox -e test_package*.

### 2.packaging
Se crea el paquete en la carpeta *packaging*, donde todo estará un poco más limpio y con los paquetes distribuibles. Se sube a PyPI.

### 3.api
Se crea la aplicación con FastAPI y se 'productiviza' con Railway (PaaS).

### 4.api_docker
Se 'conteneriza' la aplicación con Docker.
