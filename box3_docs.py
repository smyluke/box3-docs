from flask import Flask, make_response, request

app = Flask('box3-docs')


@app.route('/<path:url>')
def static_view(url):
    try:
        with open('./static/' + url, 'rb') as f:
            data = f.read()
        res = make_response(data)
        res.headers['Content-Type'] = request.headers.get('Content-Type')
        return res
    except IOError:
        return '404 NOT FOUND !', 404
