from flask import jsonify, Response


def create_json_api_response(*contents) -> Response:
    return jsonify({
        'data': [
            {'attributes': content} for content in contents
        ]
    })
