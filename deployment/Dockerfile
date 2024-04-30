FROM python:3.11-slim
COPY model_deployment.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./model_test.joblib /deploy/
COPY ./modules.py /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1
EXPOSE 80
CMD ["python", "model_deployment.py"]