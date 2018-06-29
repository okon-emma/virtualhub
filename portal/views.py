from django.shortcuts import render
from .models import Leaque, Match, Week
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def base(request):
    if 'match' in request.GET:
        match = request.GET['match']
        if not match:
            context = {
                'error':'MATCH is empty',
            }
            return render(request, 'portal/base.html', context)
        else:
            matches = Match.objects.filter(match_id__iexact=match).reverse()
            return render(request, 'portal/base.html', {'filter': matches})

    elif 'leaque' in request.GET:
        leaque = request.GET['leaque']
        if not leaque:
            context = {
                'error':'LEAQUE is empty',
            }
            return render(request, 'portal/base.html', context)
        else:
            leaques = Leaque.objects.filter(leaque_id__iexact=leaque)
            return render(request, 'portal/base.html', {'leaque': leaques})

    else:
        return render(request, 'portal/base.html')

def leaque_detail(request, pk):
    w = Week.objects.filter(leaque__id=pk)
    return render(request, 'portal/leaque_detail.html', {'w': w})

def match_detail(request, pk):
    m = Match.objects.filter(week__id=pk)
    return render(request, 'portal/match_detail.html', {'m': m})

def che_15(request):
    user_list = Match.objects.filter(match_id__icontains='che')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def ars_15(request):
    user_list = Match.objects.filter(match_id__icontains='ars')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def liv_15(request):
    user_list = Match.objects.filter(match_id__icontains='liv')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def mnu_15(request):
    user_list = Match.objects.filter(match_id__icontains='mnu')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def mnc_15(request):
    user_list = Match.objects.filter(match_id__icontains='mnc')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def eve_15(request):
    user_list = Match.objects.filter(match_id__icontains='eve')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def tot_15(request):
    user_list = Match.objects.filter(match_id__icontains='tot')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def lei_15(request):
    user_list = Match.objects.filter(match_id__icontains='lei')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def bri_15(request):
    user_list = Match.objects.filter(match_id__icontains='bri')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def wat_15(request):
    user_list = Match.objects.filter(match_id__icontains='wat')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def whu_15(request):
    user_list = Match.objects.filter(match_id__icontains='whu')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def stc_15(request):
    user_list = Match.objects.filter(match_id__icontains='stc')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def hud_15(request):
    user_list = Match.objects.filter(match_id__icontains='hud')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def bur_15(request):
    user_list = Match.objects.filter(match_id__icontains='bur')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def cry_15(request):
    user_list = Match.objects.filter(match_id__icontains='cry')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def sou_15(request):
    user_list = Match.objects.filter(match_id__icontains='sou')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def wba_15(request):
    user_list = Match.objects.filter(match_id__icontains='wba')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def bou_15(request):
    user_list = Match.objects.filter(match_id__icontains='bou')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def nwc_15(request):
    user_list = Match.objects.filter(match_id__icontains='nwc')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })

def swa_15(request):
    user_list = Match.objects.filter(match_id__icontains='swa')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_15.html', { 'users': users })





















def che_45(request):
    user_list = Match.objects.filter(match_id__icontains='che')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def ars_45(request):
    user_list = Match.objects.filter(match_id__icontains='ars')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def liv_45(request):
    user_list = Match.objects.filter(match_id__icontains='liv')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def mnu_45(request):
    user_list = Match.objects.filter(match_id__icontains='mnu')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def mnc_45(request):
    user_list = Match.objects.filter(match_id__icontains='mnc')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def eve_45(request):
    user_list = Match.objects.filter(match_id__icontains='eve')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def tot_45(request):
    user_list = Match.objects.filter(match_id__icontains='tot')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def lei_45(request):
    user_list = Match.objects.filter(match_id__icontains='lei')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def bri_45(request):
    user_list = Match.objects.filter(match_id__icontains='bri')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def wat_45(request):
    user_list = Match.objects.filter(match_id__icontains='wat')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def whu_45(request):
    user_list = Match.objects.filter(match_id__icontains='whu')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def stc_45(request):
    user_list = Match.objects.filter(match_id__icontains='stc')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def hud_45(request):
    user_list = Match.objects.filter(match_id__icontains='hud')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def bur_45(request):
    user_list = Match.objects.filter(match_id__icontains='bur')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def cry_45(request):
    user_list = Match.objects.filter(match_id__icontains='cry')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def sou_45(request):
    user_list = Match.objects.filter(match_id__icontains='sou')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def wba_45(request):
    user_list = Match.objects.filter(match_id__icontains='wba')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def bou_45(request):
    user_list = Match.objects.filter(match_id__icontains='bou')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def nwc_45(request):
    user_list = Match.objects.filter(match_id__icontains='nwc')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })

def swa_45(request):
    user_list = Match.objects.filter(match_id__icontains='swa')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 38)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'portal/result_45.html', { 'users': users })
