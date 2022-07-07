def auth1():
    try:
        import google.auth
        from google.oauth2 import id_token
        from google.oauth2 import service_account
        import google.auth.transport.requests
        from google.auth.transport.requests import AuthorizedSession
        target_audience = 'https://your-cloud-run-app.a.run.app'
        url = 'https://your-cloud-run-app.a.run.app'
        creds = service_account.IDTokenCredentials.from_service_account_file('C:\Program Files\Google\Chrome\Application\\103.0.5060.114\default_apps\external_extensions.json', target_audience=target_audience)
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


auth1()
