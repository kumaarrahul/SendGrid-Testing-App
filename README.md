# Flask Email App with SendGrid

A Python Flask web application that sends emails using SendGrid API, deployed on Azure App Service.

## Features
- Email form with to, subject, and message fields
- SendGrid integration for reliable email delivery
- Azure App Service hosting

## Setup
1. Clone repository
2. Install Python 3.12
3. Create virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
4. Configure `.env`:
```
SENDGRID_API_KEY=your_key
FROM_EMAIL=your_email
```

## Run Locally
```bash
python app.py
```
Visit http://localhost:5000

## Deploy to Azure
1. Create App Service
2. Configure environment variables
3. Deploy code via Azure CLI
```bash
az webapp up --runtime "PYTHON:3.12" --name your-app-name --resource-group your-group
```

## Technologies
- Python 3.12
- Flask
- SendGrid
- Azure App Service

  
