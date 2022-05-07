from flask import Flask, jsonify
from dataclasses import dataclass
from nika.domain.usecase.get_all_listing_candidates import *
from nika.domain.usecase.add_listing_candidate import *
from nika.ports.repository.sqlite_listing_repository import *
from nika.domain.entity.listing_candidate import *

app = Flask(__name__)

@app.route("/listings")
def get_all_listings():
    return jsonify([])

@app.route("/listings/candidates")
def get_all_listing_candidates():
    usecase = GetAllListingCandidates(__build_listing_repository())
    candidates = usecase.run()
    return __serialize_candidates(candidates)

@app.route("/listings/candidates/create")
def create_listing_candidate():
    candidate = None
    usecase = AddListingCandidate(__build_listing_repository())
    candidates = usecase.run(candidate)
    return { "result": "success" }

def __serialize_candidates(candidates):
    return jsonify(candidates)

def __build_listing_repository():
    return SqliteListingRepository("db/db.sqlite")