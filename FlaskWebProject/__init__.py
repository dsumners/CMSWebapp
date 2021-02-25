app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
app.logger.setLevel(logging.WARNING)
#SOURCE: Solution: Monitoring and Logging in Azure
app.logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)
app.logger.addHandler(streamHandler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
import FlaskWebProject.views
