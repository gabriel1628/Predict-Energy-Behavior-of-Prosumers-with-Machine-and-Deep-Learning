# Deploy with Docker

To deploy the model with Docker :

1) Install Docker

2) Open a terminal and clone the repo : 
```
git clone https://github.com/gabriel1628/Predict-Energy-Behavior-of-Prosumers-with-Machine-and-Deep-Learning.git
```

3) go to the *deployment* directory :
````
cd Predict-Energy-Behavior-of-Prosumers-with-Machine-and-Deep-Learning/deployment
````

4) Build a Docker image called `enefit-model` :
```
docker build -t enefit-model .
```

5) Run the image in a container :
```
docker run -p 5000:5000 enefit-model
```
The above commands uses -p flag to map port 5000 of the local system to the port 5000 of the docker container for the redirection of traffic on local port 5000 to port 5000 of the container.


And here you are, the application is now deployed at the address displayed in your terminal (it should be something like [127.0.0.1:5000](http://127.0.0.1:5000)).
If you tap this address in your browser, you should see the message **Welcome to the homepage ! To get your energy forecasts, send your data to the /predict endpoint**.
You can test the application using the ``call-model`` notebook.

# Deploy with Python

To deploy the model with Python :

1) install python > 3.10 if it's not already installed (add the executable to your PATH)

2) Open a terminal and clone the repo : 
```
git clone https://github.com/gabriel1628/Predict-Energy-Behavior-of-Prosumers-with-Machine-and-Deep-Learning.git
```

3) go to the *deployment* directory :
````
cd Predict-Energy-Behavior-of-Prosumers-with-Machine-and-Deep-Learning/deployment
````

4) create python virtual environment :
````
python -m venv .venv
````
If you get an error, try ``python3`` instead of ``python``.

5) activate the virtual environment :
	- On Linux/MacOS :
    ````
    source .venv/bin/activate
    ````
	- On Windows :
    ````
    .venv\Scripts\activate
    ````

6) install the required packages :
````
pip install -r requirements.txt
````

7) launch the flask application :
````
python model_deployment.py
````
