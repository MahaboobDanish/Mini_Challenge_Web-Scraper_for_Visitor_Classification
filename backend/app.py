from flask import Flask, request, jsonify
from flask_cors import CORS
from services.scraper import scrape_content
from services.classifier import classify_content
from config import Config
# from services.models import db, ClassificationResult, UserSelection

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, origins="*", allow_headers=["Content-Type", "Authorization"])

@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    url = data.get('url')
    print("HELLO")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        content = scrape_content(url)
        classification = classify_content(content)

        # Ensure 'questions' is returned as an array
        if isinstance(classification["question"], str):
            # print("***HIIIII*****")
            classification["question"] = [classification["question"]]  # Wrap the question in an array
        print("Classification data: ", classification)
        return jsonify({
            "questions": classification["question"],
            "options": classification["options"]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)


# ------------ With Database ----------------------------

# app = Flask(__name__)
# app.config.from_object(Config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<postgres>:<postgresdb>@localhost/classification_app'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)
# CORS(app, origins="*", allow_headers=["Content-Type", "Authorization"])

# @app.before_first_request
# def create_tables():
#     db.create_all()

# @app.route('/classify', methods=['POST'])
# def classify():
#     data = request.json
#     url = data.get('url')
    
#     if not url:
#         return jsonify({"error": "URL is required"}), 400

#     try:
#         # Scrape content and classify
#         content = scrape_content(url)
#         classification = classify_content(content)

#         # Ensure 'questions' is returned as an array
#         if isinstance(classification["question"], str):
#             classification["question"] = [classification["question"]]  # Wrap in array

#         # Save the result to the database
#         classification_result = ClassificationResult(
#             url=url,
#             questions=classification["question"],
#             options=classification["options"]
#         )
#         db.session.add(classification_result)
#         db.session.commit()

#         return jsonify({
#             "questions": classification["question"],
#             "options": classification["options"]
#         }), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/user-selections', methods=['POST'])
# def save_user_selection():
#     data = request.json
#     user_id = data.get('user_id')
#     selected_options = data.get('selected_options')

#     if not user_id or not selected_options:
#         return jsonify({"error": "User ID and selected options are required"}), 400

#     try:
#         # Save user selections to the database
#         user_selection = UserSelection(
#             user_id=user_id,
#             selected_options=selected_options
#         )
#         db.session.add(user_selection)
#         db.session.commit()

#         return jsonify({"message": "User selection saved successfully"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
