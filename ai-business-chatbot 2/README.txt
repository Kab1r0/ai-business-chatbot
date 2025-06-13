Welcome to your AI Business Chatbot project!

======================
How to Upload to GitHub
======================

1. Go to https://github.com and log in or create a new account.

2. Create a new repository named `ai-business-chatbot`.

3. On your computer, unzip this folder if zipped, then open Terminal (or Command Prompt).

4. Navigate to this folder:
   cd path/to/ai-business-chatbot

5. Initialize git and push the project:
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/ai-business-chatbot.git
   git push -u origin master

   Replace YOUR_USERNAME with your GitHub username.

========================
How to Deploy on Render
========================

1. Go to https://render.com and create an account.

2. Click "New" > "Web Service".

3. Connect your GitHub account and select the `ai-business-chatbot` repo.

4. Use these commands:

   Build Command:
       pip install -r requirements.txt

   Start Command:
       python app.py

5. Add an environment variable in Render:

   Key: OPENAI_API_KEY
   Value: your OpenAI API key

6. Click "Create Web Service" and wait for deployment.

7. Visit the URL Render gives you and try the chatbot!

If you want help, just ask me!