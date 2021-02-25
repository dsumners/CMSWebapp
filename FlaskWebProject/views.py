from FlaskWebProject.models import User, Post
import msal
import uuid
import logging

imageSourceUrl = 'https://'+ app.config['BLOB_ACCOUNT']  + '.blob.core.windows.net/' + app.config['BLOB_CONTAINER']  + '/'

@@ -21,6 +22,7 @@
def home():
    user = User.query.filter_by(username=current_user.username).first_or_404()
    posts = Post.query.all()

    return render_template(
        'index.html',
        title='Home Page',
@@ -66,12 +68,11 @@ def login():
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            app.logger.warning('Invalid username or password')
            flash('Invalid username or password')
            app.logger.error('Invalid login attempt')
            return redirect(url_for('login'))
        else:
            app.logger.error('{} logged in successfully'.format( user.username))
        login_user(user, remember=form.remember_me.data)
        app.logger.warning('Successful User Login')
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
@@ -88,7 +89,7 @@ def authorized():
        return render_template("auth_error.html", result=request.args)
    if request.args.get('code'):
        cache = _load_cache()
        # Acquire a token from a built msal app, along with the appropriate redirect URI
        # TODO: Acquire a token from a built msal app, along with the appropriate redirect URI
        result = _build_msal_app(cache=cache).acquire_token_by_authorization_code(
            request.args['code'],
            scopes=Config.SCOPE,
@@ -106,6 +107,7 @@ def authorized():
@app.route('/logout')
def logout():
    logout_user()
    app.logger.warning('Successful User logout!')
    if session.get("user"): # Used MS Login
        # Wipe out user and its token cache from session
        session.clear()
@@ -116,24 +118,28 @@ def logout():

    return redirect(url_for('login'))

#Sources for below: Examples from the Udacity module on Security and Monitoring Basics
def _load_cache():
    # TODO: Load the cache from `msal`, if it exists
    cache = msal.SerializableTokenCache()
    if session.get('token_cache'):
        cache.deserialize(session['token_cache'])
    return cache

def _save_cache(cache):
    # TODO: Save the cache, if it has changed
    if cache.has_state_changed:
        session['token_cache'] = cache.serialize()

def _build_msal_app(cache=None, authority=None):
    # TODO: Return a ConfidentialClientApplication
    return msal.ConfidentialClientApplication(
        Config.CLIENT_ID, authority=authority or Config.AUTHORITY,
        client_credential=Config.CLIENT_SECRET, token_cache=cache)

def _build_auth_url(authority=None, scopes=None, state=None):
    # TODO: Return the full Auth Request URL with appropriate Redirect URI
    return _build_msal_app(authority=authority).get_authorization_request_url(
        scopes or [],
        state=state or str(uuid.uuid4()),
        redirect_uri=url_for('authorized', _external=True, _scheme='https'))
