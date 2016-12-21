"""
    I don't understand... this looks like straight up inheritance to me.

    Both classes inherit from RequestHandler.

    No, the composition portion comes into play at the WSGIApplication() function
    call. The classes are being passed to the WSGIApplication function, whichs
    allows us to avoid instantiating the classes on our own.

    This code is an example of inheritance and composition working in tandem. 
"""

from myappengine import webfunc, run_app

class MainPage(webfunc.RequestHandler): #inheritance
    def get(self):
        self.response.headers["Content-Type"] = "text/plain"
        self.response.out.write("Welcome to the Greatest Website on the Web")

class FAQPage(webfunc.RequestHandler): #inheritance
    def get(self):
        self.response.headers("Content-Type") = "text/plain"
        self.response.out.write("Welcome to the Greatest FAQ on the Web")

application = webfunc.WSGIApplication( #composition
    [("/", MainPage),
     ("/info", FAQPage)],
     debug = True
     )

def main():
    run_app(application) #composition

main()
