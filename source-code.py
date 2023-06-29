
m flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
            host="localhost",
                user="your_username",
                    password="your_password",
                        database="your_database"
                        )

# Define a route for the home page
@app.route("/")
def home():
        return "Welcome"

    # Define a route for handling user input
    @app.route("/prompt", methods=["POST"])
    def prompt():
            data = request.get_json()
                prompt = data["prompt"]

                    if prompt == "How are you doing today?":
                                return "I'm doing great, thank you!"
                                else:
                                            return "Invalid prompt"

                                        if __name__ == "__main__":
                                                app.run()

