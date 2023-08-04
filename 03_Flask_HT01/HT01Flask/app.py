from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/cart", methods=["GET", "PUT"])
def cart():
    return "Ok"


@app.route("/cart/order", methods=["POST"])
def cart_order():
    return "Ok"


@app.route("/cart/add", methods=["POST", "PUT"])
def cart_add():
    return "Ok"


@app.route("/user", methods=["GET", "POST", "DELETE"])
def user():
    return "Ok"


@app.route("/user/register", methods=["POST"])
def user_register():
    return "Ok"


@app.route("/user/sign_in", methods=["POST"])
def user_sign_in():
    return "Ok"


@app.route("/user/logout", methods=["GET", "POST"])
def user_logout():
    return "Ok"


@app.route("/user/restore", methods=["POST"])
def user_pass_reset():
    return "Ok"


@app.route("/user/history", methods=["GET"])
def user_history():
    return "Ok"


@app.route("/user/history/<id>", methods=["GET"])
def user_history_by_id(id: int):
    return "Ok"


@app.route("/user/address/", methods=["GET", "POST"])
def user_address():
    return "Ok"


@app.route("/user/address/<id>", methods=["GET", "PUT", "DELETE"])
def user_address_by_id(id: int):
    return "Ok"


@app.route("/menu", methods=["GET"])
def menu():
    return "Ok"


@app.route("/menu/<cat_name>", methods=["GET"])
def menu_by_cat_name(cat_name: str):
    return "Ok"


@app.route("/menu/<cat_name>/<dish>", methods=["GET", "PUT"])
def menu_by_catname_by_dishname(cat_name: str, dish_name: str):
    return "Ok"


@app.route("/menu/<cat_name>/<dish>/review", methods=["POST"])
def menu_review(cat_name: str, dish_name: str):
    return "Ok"


@app.route("/menu/search", methods=["GET", "POST"])
def menu_search(data_to_search: str):
    return "Ok"


if __name__ == '__main__':
    app.run()
