# google-cloud-app-engine-pyramid

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
pip install -t lib -r requirements.txt
```

## Running the App

### Locally

Run:
```
python main.py
```

And preview through the console.


### Deploying the app

```
gcloud app deploy
```

Browse the app:
```
gcloud app browse -s <service_name_in_yaml_file>
```
