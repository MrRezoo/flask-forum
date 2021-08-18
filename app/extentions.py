from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from kavenegar import KavenegarAPI

db = SQLAlchemy()
migrate = Migrate()

sms_api = KavenegarAPI('336F647455347962732F6D4D3479496B6A3642483473546C6C744D6D31774B77433473746C372B534F79453D')
