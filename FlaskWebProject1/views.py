"""
Routes and views for the flask application.
"""

import os
from datetime import datetime
from flask import jsonify, render_template
import mysql.connector
from FlaskWebProject1 import app


def get_mysql_server_timestamp():
    """Return the current timestamp reported by MySQL."""
    connection_kwargs = {
        'host': os.environ.get('MYSQL_HOST', 'mysql'),
        'user': os.environ.get('MYSQL_USER', 'root'),
        'password': os.environ.get('MYSQL_PASSWORD', 'pass123'),
        'port': int(os.environ.get('MYSQL_PORT', '3308')),
    }
    database = os.environ.get('MYSQL_DATABASE')
    if database:
        connection_kwargs['database'] = database

    connection = mysql.connector.connect(**connection_kwargs)
    try:
        cursor = connection.cursor()
        try:
            cursor.execute('SELECT CURRENT_TIMESTAMP')
            row = cursor.fetchone()
            return row[0] if row else None
        finally:
            cursor.close()
    finally:
        connection.close()


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page - DOcker comopose class',
        year=datetime.now().year,
    )


@app.route('/version')
def version():
    """Returns the application version."""
    return jsonify(version='6.0')


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/timestamp')
def timestamp():
    """Renders the timestamp page."""
    try:
        server_timestamp = get_mysql_server_timestamp()
        message = 'new response'
    except mysql.connector.Error:
        server_timestamp = None
        message = 'new response'
    return render_template(
        'timestamp.html',
        title='Timestamp',
        year=datetime.now().year,
        message=message,
        server_timestamp=server_timestamp,
    )
