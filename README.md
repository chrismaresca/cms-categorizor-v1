# FastAPI Lambda Test Deploy

This is a test project to deploy a FastAPI application to AWS Lambda.

## Setup

1. Install Python 3.12
2. Install Serverless
3. Install AWS CLI
4. Create a virtual environment with `virtualenv -p python3.12 venv`
5. Activate the virtual environment with `source venv/bin/activate`
6. Install the dependencies with `pip install -r requirements.txt`

## Deploy

```bash
serverless deploy --stage production  
```

The stage can be `development`, `staging`, or `production`. It defaults to `development`.


