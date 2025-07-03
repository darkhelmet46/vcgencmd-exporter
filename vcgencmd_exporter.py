#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            temp_output = subprocess.getoutput("vcgencmd measure_temp")
            temp_c = float(temp_output.split('=')[1].split("'")[0])
            temp_f = (temp_c * 9/5) + 32

            throttled_output = subprocess.getoutput("vcgencmd get_throttled")
            throttled_hex = throttled_output.strip().split('=')[1]
            throttled_val = int(throttled_hex, 16)

            self.send_response(200)
            self.send_header('Content-type', 'text/plain; version=0.0.4')
            self.end_headers()
            self.wfile.write(f"# HELP rpi_temp Temperature in Celsius\n".encode())
            self.wfile.write(f"# TYPE rpi_temp gauge\n".encode())
            self.wfile.write(f"rpi_temp {temp_c}\n".encode())

            self.wfile.write(f"# HELP rpi_temp_f Temperature in Fahrenheit\n".encode())
            self.wfile.write(f"# TYPE rpi_temp_f gauge\n".encode())
            self.wfile.write(f"rpi_temp_f {temp_f:.2f}\n".encode())

            self.wfile.write(f"# HELP rpi_throttled_status Bitmask from get_throttled\n".encode())
            self.wfile.write(f"# TYPE rpi_throttled_status gauge\n".encode())
            self.wfile.write(f"rpi_throttled_status {throttled_val}\n".encode())

        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=MetricsHandler):
    server_address = ('', 9101)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
