import os
from flask import Flask

log_name = 'total_values.txt'

app = Flask(__name__)

def get_display_values():
    if os.path.exists('data/'+log_name):
        file = open('data/'+log_name, 'r')

        total_values = ""
        for line in file.readlines():
            total_values += line.strip()
            total_values += "<br>"

        return total_values
    
    else:
        False

@app.route('/')
def update():
    total_values = get_display_values()
    return total_values if total_values else "Nothing to display here folks!"
    

if __name__ == "__main__":
    app.run()

    