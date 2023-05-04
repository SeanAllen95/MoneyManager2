from flask import Flask, render_template

from controllers.tag_controller import tag_blueprint
from controllers.merchant_controller import merchant_blueprint
from controllers.transaction_controller import transaction_blueprint


app = Flask(__name__)

app.register_blueprint(tag_blueprint)
app.register_blueprint(merchant_blueprint)
app.register_blueprint(transaction_blueprint)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)