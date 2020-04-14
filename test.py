import json
from flask import Flask, Blueprint, jsonify


test = Blueprint('test_bp', __name__, url_prefix='/test')


@test.route('/', methods=['POST'])
def get():
    a = 11
    b = 22
    return jsonify(username=a,
                   password=b)
