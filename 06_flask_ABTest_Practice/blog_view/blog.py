from flask import Flask, Blueprint, render_template, request

blog_abtest = Blueprint('blog', __name__)


@blog_abtest.route('/test')
def test():
    return render_template('index.html')
