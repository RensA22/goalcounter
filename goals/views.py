from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import DataForm
import sqlite3


def index(request):
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    query_string = """select wed.datum_wedstrijd as 'Datum wedstrijd', wed.seizoen_wedstrijd as 'Seizoen'
    , wed.tegenstander as 'Tegenstander',
        (select count(wedstrijd_id)
        from goals_goal
        where wedstrijd_id=wed.wedstrijd_id
        group by wedstrijd_id) as 'Aantal goals',
        (select count(wedstrijd_id)
        from goals_assist
        where wedstrijd_id=wed.wedstrijd_id
        group by wedstrijd_id) as 'Aantal Assists',
        minuten_gespeeld as 'Minuten gespeeld',
        soort_wedstrijd as 'Soort wedstrijd', wed.thuis_wedstrijd
        from goals_wedstrijd as wed
        ORDER by wed.datum_wedstrijd desc"""

    cursor = cur.execute(query_string)
    result_list = []
    for row in cursor:
        result_list.append(list(row))
    
    for row in result_list:
        for i in range(len(row)):
            if row[i] == None:
                row[i] = 0

    context = {
        'table_names': [description[0] for description in cursor.description],
        'wedstrijden': result_list
    }
    return HttpResponse(loader.get_template('goals/index.html').render(context, request))


def add(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DataForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            cf = form.cleaned_data
            print(cf['soort_wedstrijd'])

            con = sqlite3.connect('db.sqlite3')
            cur = con.cursor()
            query_string = """insert into goals_wedstrijd(tegenstander, datum_wedstrijd, minuten_gespeeld, soort_wedstrijd, seizoen_wedstrijd, thuis_wedstrijd)
                            values ('{}','{}','{}','{}', '{}', '{}')""".format(cf['tegenstander'], cf['datum_wedstrijd'], cf['minuten_gespeeld'], cf['soort_wedstrijd'], cf["seizoen"], cf["thuis_wedstrijd"])

            print(query_string)

            cur.execute(query_string)
            con.commit()
            game_id = cur.lastrowid
            n_goals = cf['aantal_goals']
            n_assists = cf['aantal_assists']

            for i in range(n_goals):
                query_string = """insert into goals_goal(wedstrijd_id)
                                    values({})""".format(game_id)
                cur.execute(query_string)

            for i in range(n_assists):
                query_string = """insert into goals_assist(wedstrijd_id)
                                    values({})""".format(game_id)

                cur.execute(query_string)
            con.commit()

            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DataForm()

    return render(request, 'goals/add.html', {'form': form})
