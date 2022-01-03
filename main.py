import os, argparse, sys

class config:
    IP = '123'
    ETC_NGINX_PATH = '/etc/nginx/' #where sites-available and sites-enabled are located
    ETC_HOSTS_PATH = '/etc/hosts' #where your hosts are located
    VAR_WWW_PATH = '/var/www/' #where your sites are located
    INDEX_FILES = 'index.html index.html index.php'
    PHP_FPM_PATH = '/var/run/php/' #where your php-fpm pools are located


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

site_template = """
server {
    server_name #siteaddress# www.#siteaddress#;
    root /var/www/#siteaddress#/public;

    index index.html index.htm index.php;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php#fpm#-fpm.sock;
     }

    location ~ /\.ht {
        deny all;
    }
}
"""


def main():

    clearConsole()

    parser=argparse.ArgumentParser()
    parser.add_argument('--site', help='Ex: example.com')
    parser.add_argument('--fpm', help='Ex: 7.4')

    args=parser.parse_args()

    _site_available_ = site_template.replace('#siteaddress#', args.site)
    _site_available_ = _site_available_.replace('#fpm#', args.fpm)
    # print(_site_available_)

    site_available_path = config.ETC_NGINX_PATH + "sites-available/" + args.site
    site_enabled_path = config.ETC_NGINX_PATH + "sites-enabled/" + args.site
    f = open(site_available_path,"w+")
    f.write(_site_available_)
    f.close()
    # os.system('cp ' + site_available_path + ' ' + site_enabled_path)
    os.system('ln -s ' + site_available_path + ' ' + site_enabled_path)


    print(f"{bcolors.OKGREEN}nginX host manager{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}Created " + args.site)
    print(f"{bcolors.OKGREEN} in " + site_available_path)

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

if __name__ == "__main__":
    main()






