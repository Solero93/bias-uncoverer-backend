from flask import jsonify


def create_json_api_response(*contents):
    return jsonify({
        'data': [
            {'attributes': content} for content in contents
        ]
    })
