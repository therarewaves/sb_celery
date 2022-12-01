from flask import Flask

app = Flask(__name__, static_url_path='/static/')

from views import create_report_page, download_report_page

app.config.from_object('config')

for bp in [create_report_page, download_report_page]:
    app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()
