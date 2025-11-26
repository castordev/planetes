from skyfield.api import load, Topos    #topos crea un punto en la tierra con lat y lon
import datetime                         #load carga las efemérides


ts = load.timescale()           #convertimos la fecha y hora a un formato que skyfield entienda
bodies = load("de440.bsp")      #cargamos las efemérides

#latitud y longitud de vigo
lat = 42.2406
lon = -8.7207


#seleccionamos el planeta tierra y luego le decimos nuestra posición
earth = bodies["earth"]
location = earth + Topos(latitude_degrees=lat, longitude_degrees=lon)



def distance_body(name):      #funcion que recibe el nombre del planeta
    
    t = ts.now()                    #fecha y hora actual
    body = bodies[name]           #seleccionamos planeta


    astrom = location.at(t).observe(body)      #calcula la posicion desde tu lat y lon en ese instante

    distance = astrom.distance().km            #funcion de skyfield para devolver distancia en km

    return distance



#funciones para los planetas

def mercury_distance():
    return distance_body("mercury")

def venus_distance():
    return distance_body("venus")

def earth_distance():
    return 0        

def mars_distance():
    return distance_body("mars barycenter")

def jupiter_distance():
    return distance_body("jupiter barycenter")

def saturn_distance():
    return distance_body("saturn barycenter")

def uranus_distance():
    return distance_body("uranus barycenter")

def neptune_distance():
    return distance_body("neptune barycenter")

def pluto_distance():
    return distance_body("pluto barycenter")


#alias para no tener que poner barycenter, etc.
aliases = {
    "mercury":  "mercury",
    "venus":    "venus",
    "earth":    0,
    "mars":     "mars barycenter",
    "jupiter":  "jupiter barycenter",
    "saturn":   "saturn barycenter",
    "uranus":   "uranus barycenter",
    "neptune":  "neptune barycenter",
    "pluto":    "pluto barycenter"
}

                                                        

#Pedimos el nombre del planeta que queremos
planet_input = input("Planet name: ").strip().lower()       #strip quita espacios y lower pone todo en minusculas
    

try:
    planet_name = aliases[planet_input]                 #planet_name es la variable que recibe el alias del planeta que escribimos
                                                        #por ejemplo, nosotros por consola le decimos que nos diga la distancia desde jupiter
                                                        #pero como la API quiere que le mandemos un jupiter varicenter , planet_name busca en alias
                                                        #cual es el de jupiter y la variable planet_name queda como jupiter varicenter en vez de jupiter

    if planet_name == 0:        #para el caso especial de la tierra
        distance = 0

    else:

        distance = distance_body(planet_name)           #aqui la variable distance recibe de la funcion con el nombre de aliases


    friendly_distance = f"{int(distance):,}"            #hacemos una variable para que el resultado sea mas legible
                                                        #ponemos int(distance) para que no ponga decimales y le añadimos :, para que separe los numeros de 3 en 3
                                                        #usamos f-string para simplificar el añadido :, . si no tendriamos que poner "{:,}".format(int(distance))

    print(f"Distance to {planet_input.capitalize()}: {friendly_distance} km")


except KeyError:
    print("Sorry, that planet is not in the ephemeris")