# Ensure Nginx is installed
package { 'nginx':
  ensure => 'installed',
}

# Create the necessary directories and index.html file
file { ['/data/web_static/releases/test/', '/data/web_static/shared/']:
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'Alx-school Rocks',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test/',
  force   => true,
  require => File['/data/web_static/releases/test/'],
}

# Set ownership
file { '/data/':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('your_module/default_nginx_config.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define Nginx service
service { 'nginx':
  ensure => 'running',
  enable => true,
}
