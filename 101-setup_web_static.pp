# Define a class for setting up web servers
class profile::web_server {
  package { 'nginx':
    ensure => installed,
  }

  $dir_1 = '/data/web_static/releases/test/'
  $symlink = '/data/web_static/current'
  $dir_2 = '/data/web_static/shared/'

  file { $dir_1:
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { "${dir_1}index.html":
    ensure  => file,
    content => '<html><head></head><body>Holberton School</body></html>',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0644',
  }

  file { $dir_2:
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { $symlink:
    ensure  => link,
    target  => $dir_1,
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('profile/web_server/nginx_config.erb'),
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    hasstatus => true,
    hasrestart => true,
  }
}

# Define an ERB template for the Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('profile/web_server/nginx_config.erb'),
  notify  => Service['nginx'],
}
