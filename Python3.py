def auth1():
    try:
        import google.auth
        from google.oauth2 import id_token
        from google.oauth2 import service_account
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
        print(id_token.verify_token(token, request))
    except Exception as err_msg:
        print(err_msg)
    finally:
        print("**Execution Complete!**")


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
np.random.seed(19680801)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(100*np.random.rand(20))
formatter = ticker.FormatStrFormatter('$%1.2f')
ax.yaxis.set_major_formatter(formatter)
for tick in ax.yaxis.get_major_ticks():
    tick.label1On = False
    tick.label2On = True
    tick.label2.set_color('green')
plt.show()
