import requests

with open('words.txt', 'r') as f:
    words = f.read().split()


def send_req(username):
    r = requests.get("https://t.me/" + username)
    n = open('non_valid.txt', 'a')
    f = open('valid.txt', 'a')
    if "<meta name=\"robots\" content=\"noindex, nofollow\">" in r.text:
        print("send_req -> not taken or invalid")
        f.write('username -> ' + username + ' is not taken or invalid\n')
    else:
        print("send_req -> username taken")
        n.write('username -> ' + username + ' is taken\n')
    n.close
    f.close
    
for word in words:
    if len(word) < 5:
        continue
    send_req(word)