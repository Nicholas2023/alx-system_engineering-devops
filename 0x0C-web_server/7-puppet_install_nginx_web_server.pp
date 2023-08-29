# web_server_config.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Allow Nginx HTTP traffic
firewall { '100 allow nginx access':
  port   => 80,
  proto  => tcp,
  action => accept,
}

# Create Nginx virtual host configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    
    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        rewrite ^ https://www.example.com permanent;
    }
}
  ",
}

# Enable the virtual host configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Create web root directory
file { '/var/www/html':
  ensure => directory,
}

# Create the "Hello World!" index page
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}
