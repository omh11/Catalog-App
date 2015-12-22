from flask import Flask, render_template, request
from flask import redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, SportCategory, SportItem
from datetime import datetime
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']

engine = create_engine('sqlite:///catalogapp.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Login Page route


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

# CONNECT - Obtain current user's token and create login_session


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = json.loads(answer.text)

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px; border-radius: 150px;\
    -webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    credentials = login_session.get('credentials')
    access_token = credentials
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    if access_token is None:
        print 'Access Token is None'
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return redirect(url_for('mainPage'))
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# Main Page


@app.route('/')
def mainPage():
    sport_categories = session.query(SportCategory).all()
    sport_items = session.query(SportItem).order_by(desc(SportItem.time)).all()
    credentials = login_session.get('credentials')
    return render_template('mainpage.html', sport_categories=sport_categories,
                           sport_items=sport_items, credentials=credentials)

# Sport Category Items Page


@app.route('/catalog/<sport_category_name>/Items/')
def sportCategory(sport_category_name):
    sport_category = session.query(SportCategory).filter_by(
                     name=sport_category_name).one()
    sport_item = session.query(SportItem).filter_by(
                 sport_category_name=sport_category_name)
    no_of_items = sport_item.count()
    sport_categories = session.query(SportCategory).all()
    credentials = login_session.get('credentials')
    return render_template('sportcategoryitemspage.html',
                           sport_category=sport_category,
                           sport_item=sport_item,
                           no_of_items=no_of_items,
                           sport_categories=sport_categories,
                           credentials=credentials)

# Sport Item Description Page


@app.route('/catalog/<sport_category_name>/<sport_item_name>/')
def sportItemDescription(sport_category_name, sport_item_name):
    credentials = login_session.get('credentials')
    sport_item = session.query(SportItem).filter_by(
        sport_category_name=sport_category_name, name=sport_item_name).one()
    return render_template('ItemDescriptionPage.html',
                           sport_item=sport_item,
                           credentials=credentials)

# Add Sport Item Page


@app.route('/catalog/add/', methods=['GET', 'POST'])
def newSportItem():
    credentials = login_session.get('credentials')
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        addSportItem = SportItem(name=request.form['name'],
                                 description=request.form['description'],
                                 sport_category_name=request.form['category'],
                                 time=datetime.utcnow())
        session.add(addSportItem)
        session.commit()
        flash("New Sport Item Created!")
        return redirect(url_for('newSportItem'))
    else:
        option_list = session.query(SportCategory).all()
        return render_template('additempage.html',
                               option_list=option_list,
                               credentials=credentials)

# Edit Sport Item Page


@app.route('/catalog/<sport_category_name>/<sport_item_name>/edit/',
           methods=['GET', 'POST'])
def editSportItem(sport_category_name, sport_item_name):
    credentials = login_session.get('credentials')
    if 'username' not in login_session:
        return redirect('/login')
    editItem = session.query(SportItem).filter_by(
                sport_category_name=sport_category_name,
                name=sport_item_name).one()
    if request.method == 'POST':
        if request.form['name']:
            editItem.name = request.form['name']
        if request.form['description']:
            editItem.description = request.form['description']
        if request.form['category']:
            editItem.sport_category_name = request.form['category']
        session.add(editItem)
        session.commit()
        flash("Sport Item Edited!")
        return redirect(url_for('mainPage'))
    else:
        option_list = session.query(SportCategory).all()
        return render_template('edititempage.html',
                               editItem=editItem,
                               option_list=option_list,
                               credentials=credentials)

# Delete Sport Item Page


@app.route('/catalog/<sport_category_name>/<sport_item_name>/delete/',
           methods=['GET', 'POST'])
def deleteSportItem(sport_item_name, sport_category_name):
    credentials = login_session.get('credentials')
    if 'username' not in login_session:
        return redirect('/login')
    itemToDelete = session.query(SportItem).filter_by(
                    sport_category_name=sport_category_name,
                    name=sport_item_name).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('mainPage'))
    else:
        return render_template('deleteitempage.html',
                               sport_category_name=sport_category_name,
                               sport_item_name=sport_item_name,
                               itemToDelete=itemToDelete,
                               credentials=credentials)

# Sport Category JSON Generator


@app.route('/catalog/<sport_category_name>/json/')
def jsonOutput(sport_category_name):
    items = session.query(SportItem).filter_by(
            sport_category_name=sport_category_name).all()
    return jsonify(Items=[i.serialize for i in items])

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
