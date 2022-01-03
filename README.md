python3 main.py --site example.com --fpm 7.4

this will generate host in 

/etc/nginx/sites-available 
/etc/nginx/sites-enabled
and will ln -s the file.

will add php-fpm7.4 as your fpm

config paths in class config

    ETC_NGINX_PATH = '/etc/nginx/' #where sites-available and sites-enabled are located
    ETC_HOSTS_PATH = '/etc/hosts' #where your hosts are located
    VAR_WWW_PATH = '/var/www/' #where your sites are located
    INDEX_FILES = 'index.html index.html index.php'
    PHP_FPM_PATH = '/var/run/php/' #where your php-fpm pools are located
