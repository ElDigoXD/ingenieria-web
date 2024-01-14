set shell := ["powershell.exe", "-c"]

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
  wsl docker run --rm --volume ".:/data" --user "root" pandoc/extra ./README.md -o pdf.pdf -N --template="eisvogel" --listings