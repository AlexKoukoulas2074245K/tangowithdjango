import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings');

import django;
django.setup();

from rango.models import Category, Page;

def populate():
    python_cat = add_cat('Python', 128, 64);

    add_page(cat=python_cat,
             title = 'Official Python Tutorial',
             url = 'http://docs.python.org/2/tutorial/', 
             views = 4800);

    add_page(cat=python_cat,
             title = 'How to think like a Computer Scientist',
             url = 'http://www.greenteapress.com/thinkpython/', 
             views = 2300);

    add_page(cat=python_cat,
             title = 'Learn Python in 10 Minutes',
             url = 'http://www.korokithakis.net/tutorials/python', 
             views = 535);

    django_cat = add_cat('Django', 64, 32);

    add_page(cat=django_cat,
             title = 'Official Django Tutorial',
             url = 'https://docs.djangoproject.com/en/1.5/intro/tutorial01/',
             views = 1230);

    add_page(cat=django_cat,
             title='Django Rocks',
             url = 'http://www.djangorocks.com/',
             views = 69);

    add_page(cat=django_cat,
             title='How to Tango with Django',
             url='http://www.tangowithdjango.com/',
             views = 2);

    frame_cat = add_cat("Other Frameworks", 32, 16);

    add_page(cat=frame_cat,
             title = 'Bottle',
             url = 'http://bottlepy.org/docs/dev',
             views = 843);

    add_page(cat=frame_cat,
             title="Flask",
             url = 'http://flask.pocoo.org',
             views = 123);

    student_cat = add_cat("Alexios Koukoulas", 24, 10);

    add_page(cat=student_cat,
             title="Github Page",
             url="https://github.com/AlexKoukoulas2074245K",
             views = 2410);

    add_page(cat=student_cat,
             title="Python Anywhere page",
             url="https://www.pythonanywhere.com/user/AlexKoukoulas2074245K/consoles/",
             views = 24);
    
    #Print out what we have added to the user
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p));

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title, url = url, views=views)[0];
    p.views = views;
    return p;

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name = name, views = views, likes = likes)[0];
    c.views = views;
    c.likes = likes;
    return c;

#Start exectuion here!
if __name__ == '__main__':
    print "Starting Rango population script...";
    populate();
