from bottle import run, route, template, static_file


@route('/')
@route('/hello/<name>')
def hello(name='Stranger'):
	return template('hello', name=name)


@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='./static')

run(host = "localhost", port = 8888, debug = True)
