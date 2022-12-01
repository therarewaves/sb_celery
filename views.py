from typing import Dict, Optional

from flask import render_template, request, abort, send_file, Blueprint

import config
from storage import load_from_json_file
from tasks import request_report_and_send_to_email

__all__ = [
    'create_report_page',
    'download_report_page',
]

create_report_page = Blueprint('create_report_page', __name__, template_folder='templates')


@create_report_page.route('/', methods=['GET', 'POST'])
def create_report():
    if request.method == 'POST':
        user_email = request.form['email']
        request_report_and_send_to_email.delay(user_email)

    emails = load_from_json_file(config.EMAILS_JSON_DUMP_FILE)
    return render_template('homepage.html', test_email=config.TEST_USER_EMAIL, emails=emails)


download_report_page = Blueprint('download_report_page', __name__, template_folder='templates')


@download_report_page.route('/download_report/<int:report_id>/', methods=['GET', 'POST'])
def download_report(report_id):
    reports = load_from_json_file(config.REPORTS_JSON_DUMP_FILE)
    report: Optional[Dict] = list(filter(lambda r: r['id'] == report_id, reports))[0]

    if not report or not report.get('creator_email') == config.TEST_USER_EMAIL:
        abort(404, description="Report not found")

    if request.method == 'POST':
        return send_file(report.get('path'), as_attachment=True)

    return render_template('download_report.html', report=report)
