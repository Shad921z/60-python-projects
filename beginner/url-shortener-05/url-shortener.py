from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

#empty dictionary for storing urls
shortened_urls = {}

#generate short url funciton whose length is 6 characters
def generate_short_url(length=6):

    chars = string.ascii_letters + string.digits #chars are letters and digits

    short_url =  "".join(random.choice(chars) for _ in range(length)) #generate random characters and digits assigned to chars and it assigns to short_url
    return short_url

#User submits a URL (POST request)
@app.route("/", methods=["GET", "POST"])
def index(): #User opens the website (GET request)
    if request.method == "POST":
        long_url = request.form['long_url'] #Get the long URL from the form
        short_url = generate_short_url() #Generate a short code

        #Avoid duplicate short URLs
        while short_url in shortened_urls:
            short_url = generate_short_url()

        shortened_urls[short_url] = long_url #Store mapping in dictionary
        return f"shortened url: {request.url_root}{short_url}" #Show shortened link to user
    return render_template("index.html")


#function (Redirect logic)
@app.route("/<short_url>")

def redirect_url(short_url):
    long_url = shortened_urls.get(short_url) #Look up the long URL

    if long_url:
        return redirect(long_url) #If URL exists → redirect
    else:
        return "Short URL not found", 404 #If URL does NOT exist

if __name__ == "__main__":
    app.run(debug=True)
