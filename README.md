# google-cloud-app-engine-pyramid

Basic example on how to build a [Pyramid framewrok](https://docs.pylonsproject.org/projects/pyramid/en/latest/) application with Google Cloud 

## Installation

1. Clone repository 
```
git clone https://github.com/joangro/google-cloud-app-engine-pyramid.git
cd google-cloud-app-engine-pyramid
```

2. Set up Python environment:
```
virtualenv env
source env/bin/activate
```

3. Install libraries to environment and to lib folder:
```
mkdir lib
pip install -r requirements.txt
pip install -t lib -r requirements.txt
```

## Running the App

### Locally

Run:
```
python main.py
```

And [preview through Cloud Shell](https://cloud.google.com/shell/docs/features#web_preview).


### Deploying the app

```
gcloud app deploy
```

Browse the app:
```
gcloud app browse -s default
```
