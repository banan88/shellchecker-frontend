import SimpleHTTPServer
import SocketServer
import cgi
from urlparse import urlparse
from pygments import highlight
from pygments.lexers.shell import BashLexer
from pygments.formatters import HtmlFormatter


class DefaultHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        request = urlparse(self.path)
        print 'GET %s' % (request.path)

        requested_file = request.path.replace("/", "", 1)

        if requested_file == "":
            file_to_open = 'index.html'
        elif requested_file == 'favicon.ico':
            return
        else:
            file_to_open = requested_file

        file = open(file_to_open, 'r')
        self.respond(file.read())

    def do_POST(self):
        print 'POST %s' % (self.path)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
            })
        print dir(form)
        if form.has_key('source'):
            source_script = form['source'].value
        else:
            source_script = ''
            
        #TODO: add shellcheck call here
        content = highlight(source_script, BashLexer(), HtmlFormatter(noclasses=True))
        self.respond(content)

    def respond(self, content):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content)
        self.wfile.close()


port = 8000
httpd = SocketServer.TCPServer(("", port), DefaultHandler)

print 'serving on %s...' % (port)
httpd.serve_forever()