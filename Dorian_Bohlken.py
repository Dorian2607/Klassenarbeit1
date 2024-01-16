# -------------------------------------------
# Letze Änderung: 19.12.2023
# Version v1.0
# Aufgabe: Dieses Programm fragt den Sensor AHT10 Temperatur ab und gibt die Werte in der Kommandozeile aus.
#          Wenn die Temperatur unter 22 Grad ist sind alle LED´s aus. Ab 22 Grad geht eine led an und für jedes weitere Grad schaltet sich eine weitere LED dazu.
#          LED´s gehen von Grün über Gelb bis Rot. Von jeder LED Frabe gibt es 2 LED´s. DIe LED´s sind per Knopf an und ausschaltbar.
#          Beim Starten des Programm leuchten alle LED´s einmal für 1 Sekunde auf und gehen danach wieder aus.
# Hardware:ESP32-S3
#          AHT10 Temperatursensor SCL=9 / SDA=8
#           ledgn1 = Pin 15
#           ledgn2 = Pin 16
#           ledge1 = Pin 6
#           ledge2 = Pin 7
#           ledrt1 = Pin 4
#           ledrt2 = Pin 5
#           taster = Pin 17
# -------------------------------------------


#----------Bibliotheken----------
from time import sleep
from machine import Pin, I2C
import ahtx0

#----------AHT10 Pin----------
i2c = I2C(scl=Pin(9), sda=Pin(8))

#----------LED Pinbelegung----------
ledgn1 = Pin(15,Pin.OUT) 
ledgn2 = Pin(16,Pin.OUT) 
ledge1 = Pin(6,Pin.OUT) 
ledge2 = Pin(7,Pin.OUT) 
ledrt1 = Pin(4,Pin.OUT) 
ledrt2 = Pin(5,Pin.OUT)

#---------AHT10 Objekterzeugung---------
sensor = ahtx0.AHT10(i2c)

#----------Taster Variablen und Pin Belegung----------
taster = Pin(17,Pin.IN)
tastervorheraus = True
eingeschaltet = False

#----------Programmstart----------

# Alle LED´s einmal für 1 Sekunde einschalten um Systemtest zu Signalisieren
ledgn1.on()
ledgn2.on()
ledge1.on()
ledge2.on()
ledrt1.on()
ledrt2.on()
sleep(1)
ledgn1.off()
ledgn2.off()
ledge1.off()
ledge2.off()
ledrt1.off()
ledrt2.off()


#----------While Schleife----------
while True:
    # Unendliche Schleife zum fortlaufenden Überprüfen des Tasterzustands
    eingang1 = taster.value() # Variable setzen

    # Vergleichen ob Variable eingang1 und Variable tastervorheraus bedingung erfüllen
    if eingang1 == 1 and tastervorheraus == True:
        # Variable eingeschaltet umkehren
        eingeschaltet = not eingeschaltet
        tastervorheraus = False
        
    if eingang1 == 0:
        tastervorheraus = True
    # Wenn Messung aktiv ist also eingetastet wurde
    if eingeschaltet == True:
        # Sensortemperatur mit Grenzwert vergleichen und passende LED´s schalten
        if sensor.temperature < 22:
            ledgn1.off()
            ledgn2.off()
            ledge1.off()
            ledge2.off()
            ledrt1.off()
            ledrt2.off()
        # Sensortemperatur mit Grenzwert vergleichen und passende LED´s schalten
        elif 22 <= sensor.temperature < 23:
            ledgn1.off()
            ledgn2.off()
            ledge1.off()
            ledge2.off()
            ledrt1.off()
            ledrt2.off()
            ledgn1.on()
        # Sensortemperatur mit Grenzwert vergleichen und passende LED´s schalten
        elif 23 <= sensor.temperature < 24:
            ledgn1.off()
            ledgn2.off()
            ledge1.off()
            ledge2.off()
            ledrt1.off()
            ledrt2.off()
            ledgn1.on()
            ledgn2.on()
        # Sensortemperatur mit Grenzwert vergleichen und passende LED´s schalten
        elif 24 <= sensor.temperature < 25:
            ledgn1.off()
            ledgn2.off()
            ledge1.off()
            ledge2.off()
            ledrt1.off()
            ledrt2.off()
            ledgn1.on()
            ledgn2.on()
            ledge1.on()
        # Sensortemperatur mit Grenzwert vergleichen und passende LED´s schalten
        elif 25 <= sensor.temperature < 26:
            ledgn1.off()
            ledgn2.off()
            ledge1.off()
            ledge2.off()
            ledrt1.off()
            ledrt2.off()
            ledgn1.on()
            ledgn2.on()
            ledge1.on()
            ledge2.on()
        # Sensortemperatur mit Grenzwert vergleichen und passende LED´s schalten
        elif 26 <= sensor.temperature < 27:
            ledgn1.off()
            ledgn2.off()
            ledge1.off()
            ledge2.off()
            ledrt1.off()
            ledrt2.off()
            ledgn1.on()
            ledgn2.on()
            ledge1.on()
            ledge2.on()
            ledrt1.on()
        # Sensortemperatur mit Grenzwert vergleichen und passende LED´s schalten
        elif sensor.temperature >= 27:
            ledgn1.off()
            ledgn2.off()
            ledge1.off()
            ledge2.off()
            ledrt1.off()
            ledrt2.off()
            ledgn1.on()
            ledgn2.on()
            ledge1.on()
            ledge2.on()
            ledrt1.on()
            ledrt2.on()
    # Wenn Messung nicht aktiv ist also ausgetastet wurde
    else:
        ledgn1.off()
        ledgn2.off()
        ledge1.off()
        ledge2.off()
        ledrt1.off()
        ledrt2.off()
    # Temperaturwerte von Sensor in Kommandozeile ausgeben
    print("\nTemperatur: %0.0f C" % sensor.temperature)
    # Schalfen um taster zu entprellen
    sleep(0.2)
