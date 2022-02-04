import random
from flask import Flask, render_template, request
from helpers import summarize_with_gpt3


app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


@app.route("/")
def base_page():

  return render_template(
    "base.html"
  )


@app.route('/', methods = ['POST'])
def summary_result():

  inp = request.form['Text']

  resp = summarize_with_gpt3(inp)
  result = resp["choices"][0]['text']

  return render_template(
    "summary_result.html",
    inp=inp,
    result=result
  )



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)