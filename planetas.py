from skyfield.api import load, Topos    #topos crea un punto en la tierra con lat y long
import datetime                         #load carga las efemérides


ts = load.timescale()           #convertimos la fecha y hora a un formato que skyfield entienda
planets = load("de440.bsp")    #cargamos las efemérides

#latitud y longitud de vigo
lat = 42.2406
lon = -8.7207


#seleccionamos el planeta tierra y luego le decimos nuestra posición
earth = planets["earth"]
ubicacion = earth + Topos(latitude_degrees=lat, longitude_degrees=lon)



def distancia_planeta(nombre):      #funcion que recibe el nombre del planeta
    
    t = ts.now()                    #fecha y hora actual
    planeta = planets[nombre]       #seleccionamos planeta


    astrom = ubicacion.at(t).observe(planeta)   #calcula la posicion desde tu lat y lon en ese instante

    _, _, distancia = astrom.radec()            # .radec() devuelve ascension recta, declinacion y distancia en unidades astronomicas
                                                # ponemos _ en ascension recta y declinacion porque no nos interesan ahora, solo la distancia

    AU_KM = 149_597_870.7           #conversion unidades astronomicas a kilometros
    
    return distancia.au * AU_KM     #devolvemos la distancia en kilometros     



#funcion para los planetas
def distancia_mercurio():
    return distancia_planeta("mercury")

def distancia_venus():
    return distancia_planeta("venus")

def distancia_tierra():
    return 0             # hehe

def distancia_marte():
    return distancia_planeta("mars")

def distancia_jupiter():
    return distancia_planeta("jupiter barycenter")

def distancia_saturno():
    return distancia_planeta("saturn barycenter")

def distancia_urano():
    return distancia_planeta("uranus barycenter")

def distancia_neptuno():
    return distancia_planeta("neptune barycenter")

def distancia_pluton():
    return distancia_planeta("pluto barycenter")

                                                        



