import pkg_resources
import pymongo
import starflyer

from jinja2 import Environment, PackageLoader, PrefixLoader
from logbook import Logger

def setup(**kw):
    """initialize the setup"""
    settings = starflyer.AttributeMapper()
    
    settings.dbname = "quantumcast"
    settings.log_name = "quantumcast"
    settings.static_file_path = pkg_resources.resource_filename(__name__, 'static')

    # cookie related
    settings.cookie_secret = "czcds7z878cdsgsdhcdjsbhccscsc87csds76876ds"
    settings.session_cookie_name = "s"
    settings.message_cookie_name = "m"
    settings.update(kw)

    settings.log = Logger(settings.log_name)

    settings.templates = Environment(loader=PrefixLoader({
        "framework" : PackageLoader("starflyer","templates"),
        "master" : PackageLoader("showplanner","templates"),
    }))

    settings.db = pymongo.Connection()[settings.dbname]
    settings.logdb = settings.db.logging
    return settings

