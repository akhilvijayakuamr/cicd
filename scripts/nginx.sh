sudo systemctl daemon-reload
sudo rm -rf /etc/nginx/sites-enabled/default
sudo cp /home/ubuntu/cicd/nginx/nginx.conf /etc/nginx/site-available/Game
sudo ln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled/
sudo gpasswd -a www-data ubuntu
sudo systemctl restart nginx 