from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def Bayonetta(request):
    return render(request, 'personajes/Bayonetta.html')
def Bowser(request):
    return render(request, 'personajes/Bowser.html')
def Daisy(request):
    return render(request, 'personajes/Daisy.html')
def Dark_samus(request):
    return render(request, 'personajes/Dark_samus.html')
def Diddy_kong(request):
    return render(request, 'personajes/Diddy_kong.html')
def Donkey_kong(request):
    return render(request, 'personajes/Donkey_kong.html')
def Dr_mario(request):
    return render(request, 'personajes/Dr_mario.html')
def Duck_hunt(request):
    return render(request, 'personajes/Duck_hunt.html')
def falco(request):
    return render(request, 'personajes/falco.html')
def fox(request):
    return render(request, 'personajes/fox.html')
def ganondorf(request):
    return render(request, 'personajes/ganondorf.html')
def greninja(request):
    return render(request, 'personajes/greninja.html')
def hero(request):
    return render(request, 'personajes/hero.html')
def ice_climbers(request):
    return render(request, 'personajes/ice_climbers.html')
def incineroar(request):
    return render(request, 'personajes/incineroar.html')
def isabelle(request):
    return render(request, 'personajes/isabelle.html')
def jigglypuff(request):
    return render(request, 'personajes/jigglypuff.html')
def ken(request):
    return render(request, 'personajes/ken.html')
def king_dedede(request):
    return render(request, 'personajes/king_dedede.html')
def king_k_rool(request):
    return render(request, 'personajes/king_k_rool.html')
def kirby(request):
    return render(request, 'personajes/kirby.html')
def little_mac(request):
    return render(request, 'personajes/little_mac.html')
def lucario(request):
    return render(request, 'personajes/lucario.html')
def lucas(request):
    return render(request, 'personajes/lucas.html')
def luigi(request):
    return render(request, 'personajes/luigi.html')
def mario(request):
    return render(request, 'personajes/mario.html')
def mega_man(request):
    return render(request, 'personajes/mega_man.html') 
def meta_knight(request):
    return render(request, 'personajes/meta_knight.html') 
def mewtwo(request):
    return render(request, 'personajes/mewtwo.html') 
def mr_game_and_watch(request):
    return render(request, 'personajes/mr_game_and_watch.html') 
def ness(request):
    return render(request, 'personajes/ness.html') 
def olimar(request):
    return render(request, 'personajes/olimar.html') 
def pac_man(request):
    return render(request, 'personajes/pac_man.html') 
def palutena(request):
    return render(request, 'personajes/palutena.html') 
def peach(request):
    return render(request, 'personajes/peach.html') 
def pichu(request):
    return render(request, 'personajes/pichu.html') 
def pikachu(request):
    return render(request, 'personajes/pikachu.html') 
def piranha_plant(request):
    return render(request, 'personajes/piranha_plant.html') 
def pt_charizard(request):
    return render(request, 'personajes/pt_charizard.html') 
def pt_ivysaur(request):
    return render(request, 'personajes/pt_ivysaur.html') 
def pt_squirtle(request):
    return render(request, 'personajes/pt_squirtle.html') 
def richter(request):
    return render(request, 'personajes/richter.html') 
def ridley(request):
    return render(request, 'personajes/ridley.html') 
def ryu(request):
    return render(request, 'personajes/ryu.html') 
def samus(request):
    return render(request, 'personajes/samus.html') 
def simon(request):
    return render(request, 'personajes/simon.html') 
def snake(request):
    return render(request, 'personajes/snake.html') 
def sonic(request):
    return render(request, 'personajes/sonic.html') 
def terry(request):
    return render(request, 'personajes/terry.html') 
def wolf(request):
    return render(request, 'personajes/wolf.html') 
def young_link(request):
    return render(request, 'personajes/young_link.html') 
def cloud(request):
    return render(request, 'personajes/Cloud.html')
def corrin(request):
    return render(request, 'personajes/Corrin.html')
def ike(request):
    return render(request, 'personajes/Ike.html')
def inkling(request):
    return render(request, 'personajes/Inkling.html')
def joker(request):
    return render(request, 'personajes/Joker.html')
def lucina(request):
    return render(request, 'personajes/Lucina.html')
def marth(request):
    return render(request, 'personajes/Marth.html')
def pit(request):
    return render(request, 'personajes/Pit.html')
def roy(request):
    return render(request, 'personajes/Roy.html')
def chrom(request):
    return render(request, 'personajes/Chrom.html')
def robin(request):
    return render(request, 'personajes/Robin.html')