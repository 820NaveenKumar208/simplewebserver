from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
 <html>
<head>
<title align="centre">TOP SOFTWARE COMPANIES WITH REVENUE TABLE </title>
</head>
<body>
  


<table border="3" cellspacing="6" cellpadding="5" height="100" width="400">
<caption >TOP FIVE REVENUE GENERATING SOFTWARE COMPANY</caption>
<tr>
			<th>COMPANY NAME</th>
			<th>POSITION</th>
			<th>GOOD RATING</th>
         <TH>REVENUE</TH>
         <th>COUNTRY</th>
		</tr>
		<tr>
			<td bgcolor="yellow">APPLE</td>
			<td bgcolor="yellow"> 3rd</td>
			<td bgcolor="yellow">9.9</td>
         <td bgcolor="yellow">$385.70 B</td>
         <td bgcolor="yellow">USA</TD>



		</tr>

		<tr>
			<td bgcolor="red">JIO</td>
			<td bgcolor="red">6th</td>
			<td bgcolor="red">9.4</td>
         <td bgcolor="red">$7.52 B</TD>
            <td bgcolor="red"> INDIA</TD>
		</tr>

		<tr>
			<td bgcolor="navy">ORACLE</td>
			<td bgcolor="navy">5th</td>
			<td bgcolor="navy">9.7</td>
         <td bgcolor="navy">$51.62 B </TD>
            <td bgcolor="navy">USA </TD>
		</tr>
<tr>
   <td bgcolor="cyan">GOOGLE</td>
   <td bgcolor="cyan">9th</td>
   <td bgcolor="cyan">9.8</td>
   <td bgcolor="cyan"> 305.6 B</td>
   <td bgcolor="cyan">USA</td>

		</tr>

		<tr>
			<td bgcolor="grey">IBM</td>
			<td bgcolor="grey">2nd</td>
            <td bgcolor="grey">9.7</td>
         <td bgcolor="grey">$61.85 B</td>
            <td bgcolor="grey">USA</td>
		</tr>
      <tr>
			<td bgcolor="pink">ZOOM</td>
			<td bgcolor="pink">14th</td>
			<td bgcolor="pink">8.1</td>
         <td bgcolor="pink">$4.52 B</td>
         <td bgcolor="pink">USA</td>
      </tr>
	</table>
	</body>
</html>
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()