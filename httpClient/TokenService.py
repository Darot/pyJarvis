import requests
import requests_oauthlib
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


def fetch_token():
    client = BackendApplicationClient(client_id="jhipsterCoreapp")
    oauth = OAuth2Session(client=client)
    oauth.fetch_token(token_url="http://localhost:8080/oauth/token?grant_type=password",
                      client_id="jhipsterCoreapp",
                      client_secret="my-secret-token-to-change-in-production",
                      password="admin",
                      username="admin")
    print oauth.get("http://localhost:8080/api/users?page=0&size=20&sort=id,asc")._content