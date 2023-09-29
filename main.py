from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret_id = os.getenv("CLIENT_SECRET_ID")

print(client_id, client_secret_id)


