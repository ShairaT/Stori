from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
from back.core.newsletter_email_service import NewsletterEmailService
from back.core.user_services import UserService
from back.implementations.users_repository_impl import UsersRepositoryImpl
from back.core.newsletter_services import NewsletterService
from back.implementations.newsletters_repository_impl import FirebaseNewsletterRepository
from back.core.article_services import ArticleService
from back.implementations.article_repository_impl import FirebaseArticleRepository
from utils.is_subscribed import is_subscribed

app = Flask(__name__)

users_repository = UsersRepositoryImpl()
user_service = UserService(users_repository)

newsletter_repository = FirebaseNewsletterRepository()
newsletter_service = NewsletterService(newsletter_repository)

article_repository = FirebaseArticleRepository()
article_service = ArticleService(article_repository)

newsletter_email_service = NewsletterEmailService() 

# Clave de encriptación
encryption_key = "suRZHEWszqS6MkT__MjfdvZ7QGYTkAw5U7bV9g0FSFk="
cipher_suite = Fernet(encryption_key)



@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    try:
        user = user_service.login_user(email, password)
        # Lógica adicional después del inicio de sesión exitoso
        return jsonify({"message": 'Inicio de sesión exitoso', 'user': user}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    password = request.json['password']

    try:
        user = user_service.register_user(email, password)
        # Lógica adicional después del registro exitoso
        return jsonify({"message": 'Registro exitoso', 'user': user}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint para crear un nuevo newsletter


@app.route('/newsletters', methods=['POST'])
def create_newsletter():
    try:
        title = request.form.get('title')
        author = request.form.get('author')
        image_file = request.files.get('image_file')
        description = request.form.get('description')
        subscribers = request.form.get('subscribers')

        newsletter_id = newsletter_service.create_newsletter(
            title, author, image_file, description, subscribers)
        return jsonify({"newsletter_id": newsletter_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint para obtener un newsletter por su ID


@app.route('/newsletters/<newsletter_id>', methods=['GET'])
def get_newsletter(newsletter_id):
    newsletter = newsletter_service.get_newsletter(newsletter_id)
    if newsletter:
        return jsonify(newsletter), 200
    else:
        return jsonify({"message": "Newsletter not found"}), 404


@app.route('/newsletters', methods=['GET'])
def get_newsletters():
    newsletters = newsletter_service.get_newsletters()
    if newsletters:
        return jsonify(newsletters), 200
    else:
        return jsonify({"message": "There are not newsletters"}), 404

# Endpoint para actualizar un newsletter por su ID


@app.route('/newsletters/<newsletter_id>', methods=['PUT'])
def update_newsletter(newsletter_id):
    try:
        title = request.json['title']
        author = request.json['author']
        image_file = request.files.get('image_file')
        description = request.json['description']
        subscribers = request.json['subscribers']

        success = newsletter_service.update_newsletter(
            newsletter_id, title, author, image_file, description, subscribers)
        if success:
            return jsonify({"message": "Newsletter updated"}), 200
        else:
            return jsonify({"message": "Newsletter not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint para eliminar un newsletter por su ID


@app.route('/newsletters/<newsletter_id>', methods=['DELETE'])
def delete_newsletter(newsletter_id):
    success = newsletter_service.delete_newsletter(newsletter_id)
    if success:
        return jsonify({"message": "Newsletter deleted"}), 200
    else:
        return jsonify({"message": "Newsletter not found"}), 404

# Endpoint para crear un nuevo article


@app.route('/articles', methods=['POST'])
def create_article():
    try:
        subject = request.form.get('subject')
        newsletter_id = request.form.get('newsletter_id')
        article_file = request.files.get('article_file')
        schedule_time = request.form.get('schedule_time')

        article_id = article_service.create_article(
            subject, article_file, newsletter_id, schedule_time)
        return jsonify({"article_id": article_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint para obtener un article por su ID


@app.route('/articles/<article_id>', methods=['GET'])
def get_article(article_id):
    article = article_service.get_article(article_id)
    if article:
        return jsonify(article), 200
    else:
        return jsonify({"message": "Article not found"}), 404


@app.route('/articles', methods=['GET'])
def get_articles():
    articles = article_service.get_articles()
    if articles:
        return jsonify(articles), 200
    else:
        return jsonify({"message": "There are not articles"}), 404

# Endpoint para actualizar un article por su ID


@app.route('/article/<article_id>', methods=['PUT'])
def update_article(article_id):
    try:
        subject = request.form.get('subject')
        newsletter_id = request.form.get('newsletter_id')
        article_file = request.files.get('article_file')
        schedule_time = request.form.get('schedule_time')

        success = article_service.update_article(
            article_id, subject, article_file, newsletter_id, schedule_time)
        if success:
            return jsonify({"message": "Newsletter updated"}), 200
        else:
            return jsonify({"message": "Newsletter not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint para eliminar un article por su ID


@app.route('/articles/<article_id>', methods=['DELETE'])
def delete_article(article_id):
    success = article_service.delete_article(article_id)
    if success:
        return jsonify({"message": "Article deleted"}), 200
    else:
        return jsonify({"message": "Article not found"}), 404


@app.route('/newsletters/<newsletter_id>/subscribe', methods=['POST'])
def subscribe(newsletter_id):
    try:
        email = request.json['email']
        newsletter = newsletter_service.get_newsletter(newsletter_id)
        if (not newsletter):
            return jsonify({"message": "Newsletter doesn't exists"}), 404
        if not email:
            return jsonify({"message": "Email is required"}), 400

        subscribers = []
        if newsletter.get("subscribers") is not None:
            subscribers = newsletter.get("subscribers")
        print(subscribers)
        if email in subscribers:
            return jsonify({"message": "User is already subscribed"}), 400

        subscribers.append(email)
        success = newsletter_service.update_newsletter(
            newsletter_id, None, None, None, None, subscribers)
        if success:
            return jsonify({"message": "User subscribed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/encrypt/<email>', methods=['GET'])
def encrypt(email):
    try:
        encrypted_email = cipher_suite.encrypt(email.encode()).decode()
        return encrypted_email
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/newsletters/<newsletter_id>/<email>/is-subscribed', methods=['GET'])
def email_is_subscribed(newsletter_id, email):
    try:
        newsletter = newsletter_service.get_newsletter(newsletter_id)
        subscribed = is_subscribed(newsletter, email)
        return jsonify(subscribed=subscribed), 200   
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/newsletters/<newsletter_id>/<encrypted_email>/unsubscribe', methods=['GET'])
def unsubscribe(newsletter_id, encrypted_email):
    try:
        newsletter = newsletter_service.get_newsletter(newsletter_id)
        email = cipher_suite.decrypt(encrypted_email.encode()).decode()

        subscribers = []
        
        if newsletter is not None and newsletter.get("subscribers") is not None:
            subscribers = newsletter.get("subscribers")

        if email not in subscribers:
            return jsonify({"message": "Email is already unsubscribed"}), 304   
        print("subscribers", subscribers)
        subscribers.remove(email)
        print("subscribers", subscribers)
        success = newsletter_service.update_newsletter(
            newsletter_id, None, None, None, None, subscribers)
        if success:
          return jsonify({"message": "Email unsubscribe successfully"}), 200       

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/articles/<article_id>/send', methods=['POST'])
def send_article(article_id):
    article = article_service.get_article(article_id)
    if not article:
        return {'message': "Article doesn't exists"}, 404
    print('article', article)
    newsletter = newsletter_service.get_newsletter(article.get("newsletter_id"))
    print('newsletter', newsletter)
    if not newsletter:
         return {'message': "Unable to send emails"}, 404
    for subscriber_email in newsletter.get("subscribers"):
        newsletter_email_service.send_article_email(subscriber_email, article)

    return {'message': 'Successfully sent emails'}, 200

if __name__ == '__main__':
    app.run(host='localhost', port=9874)
