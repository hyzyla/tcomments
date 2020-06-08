from app import setup

app = setup.prepare_app()
db = setup.prepare_db(app)
migration = setup.prepare_migration(app, db)
dispatcher = setup.prepare_dispatcher(app)
login_manager = setup.prepare_login(app)


from . import models
from . import handlers

setup.prepare_handlers(dispatcher)
