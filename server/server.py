
import pandas as pd
from flask import Flask, request, render_template

log_path = 'server/data/total_values.csv'

app = Flask(__name__)

happy_idx = 0
sad_idx = 1
angry_idx = 2
fear_idx = 3

def update():
    try:
        df = pd.read_csv(log_path)
        kwargs = {
                'happy_total': df['total'][happy_idx],
                'sad_total': df['total'][sad_idx],
                'angry_total': df['total'][angry_idx],
                'fear_total': df['total'][fear_idx],

                'happy_current': df['current'][happy_idx],
                'sad_current': df['current'][sad_idx],
                'angry_current': df['current'][angry_idx],
                'fear_current': df['current'][fear_idx]
            }
        return kwargs
    except Exception as e:
        return e

@app.route('/')
def index():
    kwargs = update()

    if type(kwargs) == type({}):
        return render_template('index.html', **kwargs)
    else:
        return "Sorry folks, we're having some technical difficulties! <br>" + str(kwargs)

if __name__ == "__main__":
    app.run()

    