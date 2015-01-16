from livereload import Server
server = Server()

server.watch('content', 'pelican')
server.serve(root='output', open_url=True)
