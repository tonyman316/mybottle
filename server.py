from bottle import get, route, run, template, view, static_file

@get('/')
def news():
    return template("news_template")


run(reloader=True, host='localhost', port=8080)

