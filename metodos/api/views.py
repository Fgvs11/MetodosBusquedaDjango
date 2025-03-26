from django.shortcuts import render
from rest_framework.views import APIView
from .Metodos import bfs,dfs,dijkstra,voraz,aEstrella,hillClimbing,get_nodo,getTiempo
from .Nodo import Nodo
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
metodos ={
        'BFS': bfs,
        'DFS': dfs,
        'DIJSKTRA': dijkstra,
        "VORAZ": voraz,
        "A*": aEstrella,
        "HILL": hillClimbing
    }
@method_decorator(csrf_exempt, name='dispatch')
class NodoView(APIView):

    def options(self, request, *args, **kwargs):
        # Explicitly handle OPTIONS request
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
        
    def get(self,request, *args, **kwargs):
        nodo:Nodo = request.args.get('nodo')
        nodo = get_nodo(nodo)
        la = nodo.get_lista_adyacencia()
        adyacentes = []
        while la:
            nodo = la.get_nodo_adyacente()
            adyacentes.append([nodo.informacion, la.peso])
            la = la.get_siguiente_adyacente()
        print(adyacentes)
        return JsonResponse({'nombre': nodo.informacion, "adyacentes":adyacentes})
    
    def post(self,request):
        data = request.data
        print("Received data:", data) 
        metodo = metodos[data['algoritmo']]
        nodoInicial = get_nodo(data['nodoInicial'])
        nodoFinal = get_nodo(data['nodoFinal'])
        print("Hola")
        print(nodoFinal,nodoInicial,metodo)
        # camino = []
        # answer = []
        # peso = []
        camino = metodo(nodoInicial,nodoFinal)
        peso = round(getTiempo(camino.copy()),2)
        answer = []
        for i in range(1,len(camino)):
            answer.append({'id':f"{camino[i-1]}-{camino[i]}", 'source':camino[i-1],'target':camino[i]})
        
        return JsonResponse({'camino':answer, 'peso':peso})