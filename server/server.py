import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def update():
    
    if os.path.exists('data/total_values.txt'):
        file = open('data/total_values.txt', 'r')

        total_values = ""
        for line in file.readlines():
            total_values += line.strip() + "\n"

        return total_values
    
    else:
        return "Nothing to display here folks!"

if __name__ == "__main__":
    app.run()

    