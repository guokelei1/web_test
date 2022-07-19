# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask

app = Flask(__name__)

@app.route("/test")
def index():
    return "nihao"

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__ == '__main__':
    app.run()