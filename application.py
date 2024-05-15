from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return 'Hello, World! This is a basic Flask app.'

@app.route('/health')
def health():
    return 'machine is ok.'



if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
