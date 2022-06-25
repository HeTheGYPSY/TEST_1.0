import google.auth
from google.oauth2 import id_token
from google.oauth2 import service_account
import google.auth
import google.auth.transport.requests
from google.auth.transport.requests import AuthorizedSession
target_audience = 'https://your-cloud-run-app.a.run.app'
url = 'https://your-cloud-run-app.a.run.app'
creds = service_account.IDTokenCredentials.from_service_account_file('/path/to/svc.json', target_audience=target_audience)
authed_session = AuthorizedSession(creds)
resp = authed_session.get(url)
print(resp.status_code)
print(resp.text)
request = google.auth.transport.requests.Request()
token = creds.token
print(token)
print(id_token.verify_token(token,request))
