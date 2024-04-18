# python_runner

docker build -t python_runner .  
docker run -p 5000:5000 python_runner

It should give you something like this
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.3:5000

Take the last one (172.) and put in the chatbot code at line 189 of app/backend/app.py container_url = 'http://172.17.0.3:5000/runplot'
