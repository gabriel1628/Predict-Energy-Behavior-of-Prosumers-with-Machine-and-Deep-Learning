# Local deployment

To deploy the model locally :

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

8) launch the flask application :
````
python model_deployment.py
````

And here you are, the application is now deployed at this address displayed in your terminal (it should be something like [127.0.0.1:5000](http://127.0.0.1:5000)).
If you tap this address in your browser, you should see the message **Welcome to the homepage ! To get your energy forecasts, send your data to the /predict endpoint**.
You can test the application using the ``call-model`` notebook.