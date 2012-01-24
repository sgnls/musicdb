#!/usr/bin/make -f

NAME = musicdb
HOST = scv.lambynet.co.uk
SITE = musicdb.chris-lamb.co.uk

all: test build deploy

test:
	$(NAME)/manage.py test --verbosity=2

build:
	$(NAME)/manage.py build live

deploy:
	rsync -e ssh -avz --delete --exclude-from .rsyncignore ./ jenkins@$(HOST):/srv/$(SITE)
	ssh jenkins@$(HOST) sudo make -C /srv/$(SITE) install

install:
	ln -sf $(CURDIR)/config/gunicorn /etc/gunicorn.d/$(NAME)
	gunicorn-debian restart $(NAME)
	
	ln -sf $(CURDIR)/config/nginx /etc/nginx/sites-enabled/$(NAME)
	invoke-rc.d nginx restart
	
	$(NAME)/manage.py migrate --list
	$(NAME)/manage.py migrate --all
