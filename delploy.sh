echo "Deploy this server"
gunicorn main:app -bind 0.0.0.0 -timeout 600
cd /var/www/html/ 
git pull origin main
echo "done" 


