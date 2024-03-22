import datetime
import pandas as pd
from django.shortcuts import redirect, render
import json
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.conf import settings  
from django.contrib import messages  # Import the messages module
from .forms  import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm  # Assuming you have a form for login

from dataGraph.forms import LoginForm
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the index view upon successful login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()  # Instantiate the form

    return render(request, 'login.html', {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to the index view upon successful registration
    else:
        form = RegisterForm()  # Instantiate the form

    return render(request, 'register.html', {"form": form})


def index(request):
    return render(request, 'index.html')

@login_required
def mobile(request):
    df = pd.read_csv(r'C:\Users\HP\Desktop\dataset_graph\DisplayGraph\Sales.csv')

    # Group by 'Brands' and get the maximum selling price for each group
    df_unique = df.groupby('Brands')['Selling Price'].max().reset_index()

    # Extracting data from the unique DataFrame
    brands = df_unique['Brands']
    selling_price = df_unique['Selling Price']

    # Convert data to JSON format
    data = json.dumps({
        'brands': list(brands),
        'selling_price': list(selling_price)
    })

    context = {
        'data': data
    }

    return render(request, 'mobile.html', context)
@login_required
def youtube(request):
    df = pd.read_csv(r'C:\Users\HP\Desktop\dataset_graph\DisplayGraph\yt_sports_channels_stats.csv')

    data_list = df.to_dict('records')

    subscriber_counts = [entry['subscriber_count'] for entry in data_list]
    view_counts = [entry['view_count'] for entry in data_list]
    channel_title = [entry['channel_title'] for entry in data_list]

    context = {
        'subscriber_counts': subscriber_counts,
        'view_counts': view_counts,
        'channel_title': channel_title
    }

    return render(request, 'youtube.html', context)
@login_required
def metro(request):
    metro_data = pd.read_csv(r'C:\Users\HP\Desktop\dataset_graph\DisplayGraph\Delhi-Metro-Network.csv')

    # Convert 'Opening Date' to datetime and extract the year
    metro_data['Opening Date'] = pd.to_datetime(metro_data['Opening Date'])
    metro_data['Opening Year'] = metro_data['Opening Date'].dt.year

    # Count the number of stations opened each year
    stations_per_year = metro_data['Opening Year'].value_counts().sort_index()

    # Reset index to get it as DataFrame
    stations_per_year_df = stations_per_year.reset_index()
    stations_per_year_df.columns = ['Year', 'Number of Stations']

    # Convert DataFrame columns to lists
    years = stations_per_year_df['Year'].tolist()
    num_stations = stations_per_year_df['Number of Stations'].tolist()

    # Pass data to the template
    return render(request, 'metro.html', {'years': years, 'num_stations': num_stations})

def stock(request):
    return render(request, 'stock.html')  # Assuming you have a template named stock.html

@login_required
def worldcup(request):
    # Read the cricket data CSV file
    df = pd.read_csv(r'C:\Users\HP\Desktop\dataset_graph\DisplayGraph\worldcup.csv')

    # Calculate the total number of wins for each team
    team_wins = df['winner'].value_counts()

    # Convert the Series to a dictionary for easier manipulation
    team_wins_dict = team_wins.to_dict()
    # Sort the dictionary by team name
    team_wins_dict_sorted = dict(sorted(team_wins_dict.items()))

    # Render the template with the sorted data
    return render(request, 'worldcup.html', {'team_wins_dict': team_wins_dict_sorted})

















