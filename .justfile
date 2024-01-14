set windows-shell := ["powershell.exe", "-c"]

alias v := venv
alias r := run
alias mm := makemigrations
alias m := migrate
alias d := django

default: venv run

venv:
  .\venv\Scripts\Activate.ps1

run:
  python .\manage.py runserver

makemigrations:
  python .\manage.py makemigrations IW

migrate:
  python .\manage.py migrate

django command:
  python .\manage.py {{command}}

pandoc:
  wsl docker run --rm --volume ".:/data" --user "root" pandoc/extra ./README.md -o pdf.pdf -N --template="eisvogel" --listin>

deploy:
  @echo git stash
  @git stash > /dev/null

  @echo git pull
  @git pull > /dev/null

  @echo ./venv/bin/python ./manage.py compilemessages
  @./venv/bin/python ./manage.py compilemessages > /dev/null

  @echo ./venv/bin/python ./manage.py collectstatic --noinput
  @./venv/bin/python ./manage.py collectstatic --noinput > /dev/null

  @echo chmod o+w db.sqlite3 .
  @chmod o+w db.sqlite3 . > /dev/null

  @echo Deactivate DEBUG
  @sed -i 's/DEBUG = True/DEBUG = False/' IW/settings.py

  @echo sudo apachectl restart
  @sudo apachectl restart 2> /dev/null

  @echo Done
