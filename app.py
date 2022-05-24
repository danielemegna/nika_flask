from flask import Flask, jsonify
from dataclasses import dataclass
from nika.domain.usecase.get_all_listing_candidates import *
from nika.domain.usecase.add_listing_candidate import *
from nika.ports.repository.sqlite_listing_repository import *
from nika.domain.entity.listing_candidate import *
import db.init_db
import db.write_fixtures
import os

app = Flask(__name__)

@app.route("/listings")
def get_all_listings():
    return jsonify([])

@app.route("/listings/candidates")
def get_all_listing_candidates():
    usecase = GetAllListingCandidates(__build_listing_repository())
    candidates = usecase.run()
    return __serialize_candidates(candidates)

@app.cli.command("init-db")
def init_db_command():
    db.init_db.run(__sqlite_filepath())

@app.cli.command("write-fixtures")
def write_fixtures_command():
    db.write_fixtures.run(__sqlite_filepath())

def __sqlite_filepath():
    flask_env = os.getenv('FLASK_ENV', 'development')
    return f'db/{flask_env}.sqlite'

def __serialize_candidates(candidates):
    return jsonify(candidates)

def __build_listing_repository():
    return SqliteListingRepository(__sqlite_filepath())
