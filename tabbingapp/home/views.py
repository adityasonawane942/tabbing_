from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView
from .models import Tournament, Adjudicator, Team, Institution
from .forms import UserForm


class Homepage(generic.ListView):
    template_name = 'home/homepage.html'
    context_object_name = 'all_tournaments'

    def get_queryset(self):
        return Tournament.objects.all()


class DetailView(generic.DetailView):
    model = Tournament
    template_name = 'home/detail.html'


class WelcomePage(generic.ListView):
    model = Tournament
    template_name = 'home/welcome_page.html'


class TournamentCreate(CreateView):
    model = Tournament
    fields = ['tournament_name', 'dates', 'speaker_score_range', 'adjudicator_score_range', 'number_of_rounds', 'number_of_break_rounds', 'tournament_venue']


class Participants(generic.DetailView):
    model = Tournament
    template_name = 'home/participants.html'


class Rounds(generic.DetailView):
    model = Tournament
    template_name = 'home/rounds.html'


class Breaks(generic.DetailView):
    model = Tournament
    template_name = 'home/breaks.html'


class BreakRounds(generic.DetailView):
    model = Tournament
    template_name = 'home/breakrounds.html'


class Motions(generic.DetailView):
    model = Tournament
    template_name = 'home/motions.html'


class Settings(generic.DetailView):
    model = Tournament
    template_name = 'home/settings.html'


class Standings(generic.DetailView):
    model = Tournament
    template_name = 'home/standings.html'


class UserFormView(View):
    form_class = UserForm
    template_name = 'home/registration_form.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('home:login')

        return render(request, self.template_name, {'form': form})
