from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group
from django.shortcuts import render, resolve_url
from django_htmx.http import HttpResponseClientRedirect, push_url
from django.views.decorators.http import require_POST, require_http_methods, require_GET
from ..settings import DEBUG
from IW.models import UserData


def nutricionist(request: HttpRequest) -> HttpResponse:
  clients = User.objects.filter(groups__name="Client")
  print(clients)

  context = {
      "clients": clients
  }
  return render(request, "nutricionist.html", context)


def createUser(request: HttpRequest) -> HttpResponse:

  if request.POST:
    form = request.POST.dict()

    user_exists = User.objects.filter(username=form["username"]).first()
    if user_exists:
      return HttpResponse("""
                          <p id="errorContainer" class="d-grid text-center text-danger fw-normal lead">
                          Usuario ya registrado
                          </p>""")

    new_user = User.objects.create_user(
        username=form["username"],  # type: ignore
        password=form["password"],  # type: ignore
        email=form["username"],  # type: ignore
        first_name=form["first_name"],
        last_name=form["last_name"],
    )
    new_user.groups.add(Group.objects.get(name="Client"))
    UserData.objects.create(  # type: ignore
        user=new_user,
        weight=form["weight"],
        height=form["height"],
        activity=form["activity"],
        phone=form["phone"],
    )

    return HttpResponseClientRedirect(resolve_url(to="nutricionist"))

  if DEBUG:
    context = {
        "crud_user": {
            "first_name": "first_name",
            "last_name": "last_name",
            "username": "email@email.com",
            "userdata": {
                "weight": "10",
                "height": "100",
                "activity": "1.55",
                "phone": "111 111 111",
            }
        },
    }
  else:
    context = {}

  return render(request, "user-crud.html", context)


@require_POST
def toggleUser(request: HttpRequest, id: int) -> HttpResponse:
  if user := User.objects.filter(id=id).first():
    user.is_active = not user.is_active
    user.save()

  return HttpResponseClientRedirect(resolve_url(to=f"/profile/{id}"))


@require_http_methods(["DELETE"])
def deleteUser(request: HttpRequest, id: int) -> HttpResponse:
  if user := User.objects.filter(id=id).first():
    user.delete()

  return HttpResponseClientRedirect(resolve_url(to="nutricionist"))


def updateUser(request: HttpRequest, id: int) -> HttpResponse:
  user = User.objects.filter(id=id).first()
  if not user:
    raise Http404()

  if request.method == "GET":
    context = {
        "crud_user": user,
        "update": True,
    }

    return render(request, "user-crud.html", context)

  if request.POST:
    form = request.POST.dict()

    user.first_name = form["first_name"]  # type: ignore
    user.last_name = form["last_name"]  # type: ignore
    user.userdata.weight = form["weight"]  # type: ignore
    user.userdata.height = form["height"]  # type: ignore
    user.userdata.activity = form["activity"]  # type: ignore
    user.userdata.phone = form["phone"]  # type: ignore
    print(form)
    user.userdata.save()  # type: ignore
    user.save()

  return HttpResponseClientRedirect(resolve_url(to=f"/profile/{id}"))


@require_http_methods(["GET"])
def user(request: HttpRequest) -> HttpResponse:
  if request.method == "GET":

    user = User.objects.filter()[2]

    data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "weight": user.userdata.weight,  # type: ignore
        "height": user.userdata.height,  # type: ignore
        "activity": user.userdata.activity,  # type: ignore
        "phone": user.userdata.phone,  # type: ignore
    }

    return JsonResponse(data)
  raise Http404()


@require_http_methods(["GET"])
def user_id(request: HttpRequest, id: int) -> HttpResponse:
  if request.method == "GET":
    user = User.objects.filter(id=id).first()
    if not user or user.groups.get().name != 'Client':
      raise Http404()

    data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "weight": user.userdata.weight,  # type: ignore
        "height": user.userdata.height,  # type: ignore
        "activity": user.userdata.activity,  # type: ignore
        "phone": user.userdata.phone,  # type: ignore
    }

    return JsonResponse(data)
  raise Http404()
