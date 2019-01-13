from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import forms
from .models import Shift



def initial_page(request):
    return render(request, 'shifts/initial_page.html')


@login_required
def index(request):

    users = User.objects.all()
    form = forms.ShiftForm()
    shifts = Shift.objects.all()

    context = {
        'shifts': shifts,
        'users': users,
        'form': form,
        'title': 'index'
    }

    return render(request, 'shifts/index.html', context)


@login_required
def create_shift(request):
    
    if request.method == 'POST':
        form = forms.ShiftForm(request.POST)

        if form.is_valid():  

            clock_in = str(form.cleaned_data['date'])+ ' ' + str(form.cleaned_data['clock_in'])  
            clock_out = str(form.cleaned_data['date'])+ ' ' + str(form.cleaned_data['clock_out'])

            clock_in_formated = datetime.strptime(clock_in, '%Y-%d-%m %H:%M:%S'  )
            clock_out_formated = datetime.strptime(clock_out, '%Y-%d-%m %H:%M:%S')

            Shift.objects.create(name=form.cleaned_data['name'],
                                 clock_in=clock_in_formated,
                                 clock_out=clock_out_formated,
                                 break_time=form.cleaned_data['break_time'],
                                 date=form.cleaned_data['date'],
                                 description=form.cleaned_data['description'])
        
    return redirect(index)


@login_required       
def remove_shift(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    shift.delete()
    messages.success(request, f'Your shift has been removed')
    return redirect(index)


@login_required
def filter_shifts_by_date(request, dt="2000-01-01", df="2000-01-01" ): # juntar selectDate com select_periods

    users = User.objects.all()
    select_date_form = forms.SelectDateForm()
    shifts = Shift.objects.select_related('name').order_by('name')

    if request.method == 'POST':
        select_date_form = forms.SelectDateForm(request.POST)

        if select_date_form.is_valid():

            print("VALIDATION SUCCESS!")
            print("date_from: ", select_date_form.cleaned_data['date_from'])
            print("date_to: ", select_date_form.cleaned_data['date_to'])

            df = select_date_form.cleaned_data['date_from']
            dt = select_date_form.cleaned_data['date_to']
            
            shifts = Shift.objects.select_related('name').filter(date__gte=df, date__lte=dt).order_by('name')

    context = {
        'select_date_form': select_date_form,
        'users': users,
        'shifts': shifts,
        'title': 'Select Dates'
    }

    return render(request, 'shifts/select_dates.html', context)

    
@login_required
def select_payment_period(request, date_from, date_to): #do it so this function is not needed, change to filter
    users = User.objects.all()
    shifts = Shift.objects.filter(date__gte=date_from).filter(date__lte=date_to)

    context = {
        'users': users,
        'shifts': shifts,
        'title': 'Select Period'
    }

    return render(request, 'shifts/select_dates.html', context)


@login_required
def update_shift(request, pk): #needs more work on this one (make it so I don't need a update, only a create shift)
    
    shift = get_object_or_404(Shift, pk=pk)
   
    if request.method == 'POST':
        shift_form = forms.ShiftUpdateForm(request.POST)

        if shift_form.is_valid():  

            clock_in_cleaned = str(shift_form.cleaned_data['date'])+ ' ' + str(shift_form.cleaned_data['clock_in'])  
            clock_out_cleaned = str(shift_form.cleaned_data['date'])+ ' ' + str(shift_form.cleaned_data['clock_out'])

            clock_in_formated = datetime.strptime(clock_in_cleaned, '%Y-%d-%m %H:%M:%S'  )
            clock_out_formated = datetime.strptime(clock_out_cleaned, '%Y-%d-%m %H:%M:%S')

            shift.clock_in = clock_in_formated
            shift.clock_out = clock_out_formated
            shift.break_time = shift_form.cleaned_data['break_time']
            shift.date = shift_form.cleaned_data['date']

            shift.save()

            messages.success(request, f'Your shift has been updated!')

            return redirect(index)

    else:
        shift_form = forms.ShiftUpdateForm(initial={'clock_in': shift.clock_in,
                                                    'clock_out': shift.clock_out,
                                                    'date': shift.date,
                                                    'duration': shift.duration,
                                                    'break_time': shift.break_time,
                                                    'description': shift.description,
                                                    })

    context = {
        'shift_form': shift_form,
        'title': 'Update Shift'
    }

    return render(request, 'shifts/update_shift.html', context)

@login_required
def shift_detail(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    return render(request, 'shifts/shift_detail.html', {'shift': shift})

