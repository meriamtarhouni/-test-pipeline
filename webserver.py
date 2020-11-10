from http.server import HTTPServer, BaseHTTPRequestHandler
#import psutil
import urllib.parse as urlparse
from urllib.parse import parse_qs
import timeit



def fact(n):
    
      if n<0:
          return -1
      if n==0: 
          return 1  
      return n*fact(n-1)


def fact_Iterative(n):
    if n<0:
        return -1
    x=1
    for i in range(2,n+1):
        x*=i
    return x

    
class helloHandler(BaseHTTPRequestHandler):
    
    
    def do_GET(self):
            
       if self.path == '/metrics':
            
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            output=""
            output+="<html><body>Memoire</body></html>"
            self.wfile.write(output.encode())
       
       else:
            if '?' in self.path :
                self.send_response(200)
                self.end_headers()
                parsed = urlparse.urlparse(self.path)
                x=parse_qs(parsed.query)['n'][0]
                res=fact(int(x))
                output=""
                output+="<html><body>"+str(res)+"</body></html>"
                self.wfile.write(output.encode())
            else:
                self.send_response(404)
            



def main():
    PORT = 8080
    server = HTTPServer(('localhost',PORT),helloHandler)
    print('Server running on port %s' % PORT)
    #print(str(psutil.virtual_memory()))
    server.serve_forever()
    

if __name__ == '__main__' :
   
    main()
   

    
