import wsgi_01

def application(func):
    func(123)


application(wsgi_01.test)