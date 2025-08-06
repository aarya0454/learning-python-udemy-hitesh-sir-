def serve_chai():
    yield "cup1:masala chai"
    yield "cup2:lemon chai"
    yield "cup3: elaichi chai"

cup = serve_chai()

print(next(cup))
print(next(cup))
print(next(cup))
