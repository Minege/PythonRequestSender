import socket
import random


CRLF = "\r\n\r\n"
uagent=[]
uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")


def avaible_agents(): return uagent


def send_request(website, direction='/', type='GET', agent=random.choice(uagent), port=80):
    """

    A function for sending GET, POST, etc, request, with specific user agent, on port 80, and with a URL arguments of /
    Default type : GET
    Default port : 80
    Default UserAgent : Random UserAgent
    Default URL-Args : /

    :param website:
    :param direction:
    :param type:
    :param agent:
    :param port:
    :return data:
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((website, port))
    s.send(str(type + " " + direction + " HTTP/1.1"+CRLF).encode())
    s.send(str("Host: " + website+CRLF).encode())
    s.send(str("User-Agent: " + agent+CRLF).encode())
    data = s.recv(999999999)
    s.shutdown(1)
    s.close()
    return data.decode()
