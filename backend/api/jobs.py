from flask import Blueprint, jsonify, request
from core.scraper import scrape_indeed

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/indeed', methods=['GET'])
def get_indeed_jobs():
    keyword = request.args.get('keyword')
    location = request.args.get('location', "")
    if not keyword:
        return jsonify({'error': 'Keyword is required'}), 400

    job_listings = scrape_indeed(keyword, location)
    return jsonify(job_listings)
