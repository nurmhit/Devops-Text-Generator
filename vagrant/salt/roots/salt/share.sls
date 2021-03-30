vim:
  pkg.installed

python-pip:
  pkg.installed:
    - pkgs:
      - python-pip

python3-pip:
  pkg.installed:
    - pkgs:
      - python3-pip

install lots from pip:
   pip.installed:
     - names:
       - paramiko

numpy:
  pip.installed:
    - name: numpy
    - bin_env: '/usr/bin/pip3'

scipy:
  pip.installed:
    - name: scipy
    - bin_env: '/usr/bin/pip3'

pandas:
  pip.installed:
    - name: pandas
    - bin_env: '/usr/bin/pip3'
