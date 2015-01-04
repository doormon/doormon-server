from website import app

@app.route('/')
def root():
	  return "Doormon server"

