# app.py
import requests
import flask
import django
import cryptography
import urllib3

print("Hello from a potentially vulnerable app!")
print(f"Requests version: {requests.__version__}")
print(f"Flask version: {flask.__version__}")
