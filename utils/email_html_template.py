def get_email_html_template(unsubscribe_link):
    return '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Stori</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
    body {
    font-family: "Roboto", sans-serif;
    margin: 0;
    padding: 0;
    }

    h1 {
    font-size: 24px;
    font-weight: 500;
    margin: 0 0 16px 0;
    color: #000000;
    }

    p {
    font-size: 16px;
    font-weight: 300;
    margin: 0 0 16px 0;
    color: #000000;
    }

    img {
    max-width: 100%;
    display: block;
    }

    a {
    text-decoration: none;
    color: #000000;
    }

    .unsubscribe {
    background-color: #FF0000;
    color: #FFFFFF;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    }
    </style>
    </head>
    <body>
    <h1>Stori</h1>
    <img src="https://www.kindpng.com/picc/m/49-495765_email-newsletter-png-clipart-newsletter-icon-png-transparent.png" alt="Stori newsletter">
    <p>¡Hola! Aquí te dejo la información del nuevo artículo:</p>
    <p>Si quieres darte de baja, haz click aquí: </p>
    <a href= ''' + unsubscribe_link + '''>Dar de baja</a>
    <br>
    <br>
    <p>Nos vemos! </p>
    </body>
    </html>
    '''
