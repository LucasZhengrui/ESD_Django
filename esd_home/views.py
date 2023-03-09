from django.shortcuts import render
from faker import Faker

# Create your views here.

def story():
    fake = Faker()
    mystory = (
                f"In a(n) {fake.company()} a young {fake.language_name()} " 
                f"stumbles across a(n) {fake.domain_word()} which spurs him into conflict with {fake.name() }"
                f"an {fake.catch_phrase()} with the help of a(n) {fake.job()} and her {fake.file_name()}"
                f" culminating in a struggle at {fake.company()} where someone shouts: '{fake.bs()}'"
            )
    return mystory

def index(request):
    mystory = story()
    converted_t = None
    temp = None
    if request.method== "POST":
        temp = int(request.POST.get('temp',''))
        converted_t = (temp-32)*0.5556
    return render(request, 'esd_home/index.html', {'story': mystory, 'converted_t': converted_t, 'temp': temp})