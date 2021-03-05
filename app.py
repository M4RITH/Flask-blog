from blog import create_app
from dotenv import load_dotenv
import os

load_dotenv()

app = create_app()

if __name__ == "__main__":
    app.run(host=os.environ.get('HOST'), port=os.environ.get('PORT'), debug=os.environ.get('DEBUG'))
