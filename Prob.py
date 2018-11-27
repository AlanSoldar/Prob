# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:20:55 2018

@author: alansoledar
"""
from math import sqrt
from math import exp
from math import factorial
from math import pi

def calc_freq(lista):
    '''recebe uma lista de valores e gera um dicionário com a frequência de cada valor'''
    dc = {}    
    for x in lista:
        if x in dc:
            dc[x] += 1
        else:
            dc[x] = 1
        
    '''retorna um dicionario'''
    return dc
            
def media_aritimetica(dc):
    '''recebe o dicionário de frequências e faz a media aritimetica'''
    
    media = 0
    n = 0
    for x, f in dc.items():
        media += x*f
        n += f
    media = media/n
            
    '''retorna um float'''
    return media
            
def media_geometrica(dc):
    '''recebe o dicionário de frequências e faz a media geometrica'''
    
    media = 1
    n = 0
    for x, f in dc.items():
        media = media*pow(x,f)
        n += f
    media = pow(media,1/n)
    
    '''retorna um float'''        
    return media
            
def media_harmonica(dc):
    '''recebe o dicionário de frequências e faz a media harmonica'''
    
    media = 0
    n = 0
    for x, f in dc.items():
        media += f/x
        n += f
    media = n/media
        
    '''retorna um float'''
    return media
           
def var(dc):
    '''recebe o dicionário de frequências e calcula a variancia'''
    
    SS = 0
    n = 0
    media = media_aritimetica(dc)
    for x, f in dc.items():
        SS += (x-media)**2
        n += f
    SS = SS/(n-1)
    
    '''retorna um float'''
    return SS
       
def C(h,l):
    return factorial(h)/(factorial(l)*factorial(h-l))
    
def binomial(n, p, l, *h):
    '''*resultados podem ser apenas binarios (falha ou sucesso)
       *a probabilidade é a mesma para toda tentativa
       n: número de tentativas
       p: chance de sucesso
       l: número de sucessos desejados
       h: usado se quiser a soma de probabilidades de l à h'''
    resultado = 0
    if h != ():    
        high = h[0]
    else:
        high = l+1
    for x in range(l,high+1):
        resultado += C(n,x)*pow(p,x)*pow((1-p),n-x)
    
    '''retorna um float'''
    return resultado
    
def poisson(media, t, l, *h):
    '''*calcula quantas vezes um evento ocorre em um intervalo de tempo
       *a probabilidade é a mesma para toda tentativa
       *o número de ocorrencias de um intervalo independe do outro
       media: media de ocorrências
       t: em quanto tempo a probabilidade deve ser medida
       l: número de sucessos desejados
       h: usado se quiser a soma de probabilidades de l à h'''
    resultado = 0
    if h != ():    
        high = h[0]
    else:
        high = l+1
    for x in range(l,high+1):
        resultado += exp(-media*t)*pow(media*t,x)/factorial(x)
    
    '''retorna um float'''
    return resultado

def hipergeometrica(N, k, n, l, *h):
    '''*resultados podem ser apenas binarios (falha ou sucesso)
       *a probabilidade é a mesma para toda tentativa
       *sem reposição
       N: número total de elementos
       k: elementos desejados
       n: número de tentativas
       l: número de sucessos desejados
       h: usado se quiser a soma de probabilidades de l à h'''
    resultado = 0
    if h != ():    
        high = h[0]
    else:
        high = l+1
    for x in range(l,high+1):
        resultado += (C(k,x)*C(N-k, n-x))/C(N, n)
    
    '''retorna um float'''
    return resultado
    
def norma_area_bi(px):
    file_tab = open("Tab_NBI.txt", "r")
    tab = []
    while True:
        line = file_tab.readline()
        if line == '':
            break
        tab.append(list(map(float, line.rstrip().split(' '))))
    
    if px < 0.5 and px > 0:
        return tab[int(px*100-1)][int(px*1000)-int(px*100)*10]
        
def IC(media, dp, n, confiança):
    '''determina um intervalo em que a média tem x(confiança) chance de estar
        media: média
        dp: desvio padrão
        n: tamanho da amostra
        confiança: chance da media estar no intervalo retornado'''
    erro = norma_area_bi(1-confiança)*dp/sqrt(n)
    
    '''retorna uma tupla'''
    return (media-erro, media+erro)
    


file = open("teste.txt", "r")
lista = list(map(float, file.readline().rstrip().split(' ')))
dict_freq = calc_freq(lista)
m_aritimetica = media_aritimetica(dict_freq)
m_geometrica = media_geometrica(dict_freq)
m_harmonica = media_harmonica(dict_freq)
SS = var(dict_freq)
S = sqrt(SS)
CV = (S/m_aritimetica)*100
print("media aritimetica: ", m_aritimetica)
print("media geometrica: ", m_geometrica)
print("media harmonica: ", m_harmonica)
print("variancia: ", SS)
print("desvio padrão: ", S)
print("Coeficiente de variação:  ", CV)
print("binomial:  ", binomial(20,0.05, 0,2))
print("poisson:  ", poisson(30,1, 0,4))
print("hipergeometrica:  ", hipergeometrica(60, 7, 6, 5))
print("IC: ", IC(19.92, 0.04, 100, 0.90))
