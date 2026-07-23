import urllib.request

url = 'http://127.0.0.1:8000/login/?next=/'
try:
    with urllib.request.urlopen(url, timeout=10) as response:
        html = response.read().decode('utf-8', errors='ignore')
        print('LENGTH', len(html))
        keys = [
            'Sales and Reporting System',
            'Welcome back',
            'brand-panel',
            'caps-hint',
            'Forgot password?',
            'name="next"',
            'toggle-password',
            'Real-time sales analytics',
            'btn-login',
        ]
        for key in keys:
            print(key, key in html)
        print('\nFIRST 400 CHARACTERS:\n')
        print(html[:400])
except Exception as e:
    print('ERROR', type(e).__name__, e)
