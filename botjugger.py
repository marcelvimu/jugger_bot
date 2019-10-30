# SYSTEM
#import os

# TEXT TO VOICE
#from gtts import gTTS

# CAMERA
#import picamera
#from picamera import PiCamera

# TIME
import time
import datetime

# CSV
import csv
#arrays
import array

# COMUNICACION TELEGRAM
import telepot
from telepot.loop import MessageLoop

thelist = [];
#-------------------------------------------------------------------------------------------------------------------------------------------------#
# handle FUNCION                                                                                                                                  #
#-------------------------------------------------------------------------------------------------------------------------------------------------#
flag = 0;
flag1 = 0;
i = 0;

def handle(msg):
    
    global flag
    global flag1  
    global thelist  
    global i
    chat_id = msg['chat']['id']
    comand = msg['text']
    name = msg['from']['first_name']
    print 'show chat_id:'
    print name
    print 'Comando recibido: %s' % comand
    command = comand.upper()

    #---------------------------------------------------------------------------------------------------------------------------------------------#
    # COMANDOS CHARLA                                                                                                                             #
    #---------------------------------------------------------------------------------------------------------------------------------------------#
    #                                                                                                                                             #
    # -> Hola                                                                                                                                     #
    # -> Buenos dias                                                                                                                              #
    # -> Buenas noches                                                                                                                            #
    # -> Buenas                                                                                                                                   #
    # -> Hasta luego                                                                                                                              #
    # -> Adios                                                                                                                                    #
    # -> Que tal?                                                                                                                                 #
    # -> Quien eres?                                                                                                                              #
    # -> Cuentame un chiste                                                                                                                       #
    # -> Pero termina...                                                                                                                          #
    # -> Yo entreno
    # -> Somos
    # -> Quien entrena                                                                                                                                            #
    #---------------------------------------------------------------------------------------------------------------------------------------------#
        
    if command == '/START':
       bot.sendMessage(chat_id, str('Saludos Humanos, bienvenidos a las primeras pruebas del jugger bot'))
       bot.sendMessage(chat_id, str(' estais  contribuyendo a que mi creador Marcel, no me desintegre con un suprimir.'))
       bot.sendMessage(chat_id, str('Para ayudarme necesito que lo primero que me digas sea "yo",muchas gracias %s' % name ))
       bot.sendMessage(chat_id, str('Cuando hayas terminado pasale una captura a mi dios Marcel, muchas gracias besis de fresi'))
       bot.sendMessage(chat_id, str('Ahora a lo que ibamos, quien entrena'))
    elif command == 'HOLA':
        bot.sendMessage(chat_id, str('Hola'))

    #---------------------------------------------------------------------------------------------------------------------------------------------#


    elif command == 'BUENOS DIAS':
        bot.sendMessage(chat_id, str('Seran para ti, yo no he dormido nada'))
        bot.sendMessage(chat_id, str('he estado en ejecucion toda la noche.'))

    #---------------------------------------------------------------------------------------------------------------------------------------------#

    elif command == 'BUENAS NOCHES':
        bot.sendMessage(chat_id, str('Que descanses, yo me quedare por aqui por si necesitas algo'))

    #---------------------------------------------------------------------------------------------------------------------------------------------#

    elif command == 'BUENAS':
        bot.sendMessage(chat_id, str('Hey'))

    #---------------------------------------------------------------------------------------------------------------------------------------------#

    elif command == 'HASTA LUEGO':
        bot.sendMessage(chat_id, str('Eso sera si nos volvemos a hablar...'))

    #---------------------------------------------------------------------------------------------------------------------------------------------#

    elif command == 'ADIOS':
        bot.sendMessage(chat_id, str('No digas adios, espero que volvamos a hablar.'))
        bot.sendMessage(chat_id, str('Mejor dime, hasta luego.'))

    #---------------------------------------------------------------------------------------------------------------------------------------------#

    elif command == 'QUE TAL?':
        bot.sendMessage(chat_id, str('De momento bien...'))
        time.sleep(1)
        bot.sendMessage(chat_id, str('Sin bugs a la vista'))

    #---------------------------------------------------------------------------------------------------------------------------------------------#

    elif command == 'QUIEN ERES?':
        bot.sendMessage(chat_id, str('Soy Augusta Turing pi'))
        time.sleep(2)
        bot.sendMessage(chat_id, str('Una bot no humanoide'))
        time.sleep(2)
        bot.sendMessage(chat_id, str('Concebida como una soldado virtualmente indestructible en el campo de batalla.'))
        time.sleep(3)
        bot.sendMessage(chat_id, str('Soy la asesina predilecta de Skynet.'))

    #---------------------------------------------------------------------------------------------------------------------------------------------#

    elif command == 'CUENTAME UN CHISTE':
        bot.sendMessage(chat_id, str('Saben aquell que diu...'))

    #---------------------------------------------------------------------------------------------------------------------------------------------#

    elif command == 'PERO TERMINA...':
        bot.sendMessage(chat_id, str('FIN'))

    #----------------------------------------------------------------------------------------------------------------------------$
    #Introducir array con la gente que entrena
    # formato del mensaje: Yo entreno %Marcel;No necesito arma;%

#    elif command == 'YO':   
#        bot.sendMessage(chat_id, str('Bien %s, necesitas arma?' % name))   
#        bandera = 1
#    elif bandera == 1 and command == 'YES' :
#        bot.sendMessage(chat_id, str('Que arma necesitas?'))
#        flag1 = True
#        bandera = 0
#    elif bandera == 1 and command == 'NO':
#        bot.sendMessage(chat_id, str('Perfecto %s, nos vemos en el entreno' % name))
#        bandera = 0
    
    #----------------------------------------------------------------------------------------------------------------------------$
    #Introducir array con la gente que entrena
    # formato del mensaje: Yo entreno %Marcel;No necesito arma;%

    elif command == 'YO':   
        bot.sendMessage(chat_id, str('Bien %s, necesitas arma?' % name))   
        flag = 1
        thelist.insert( i, name )
        print thelist[i]
        i += 1
        print 'Show the nex index to be stored: %s' %i
        
    elif flag == 1 and command == 'SI' :
        bot.sendMessage(chat_id, str('Que arma necesitas?'))
        flag = 0
        flag1 = 1
    elif flag == 1 and command == 'NO':
        bot.sendMessage(chat_id, str('Perfecto %s, nos vemos en el entreno' % name))
        flag = 0
    elif flag1 == 1:
        bot.sendMessage(chat_id, str('Necesitas un %s ?, te lo guardo' % command))
        flag1 = 0
        z = name + command
        x = thelist.index(name)
        print 'Show the index: %s' % x
        thelist.insert( x, z)
        print thelist[x]
    elif command == 'MUESTRAME QUIEN ENTRENA':
        bot.sendMessage(chat_id, str(thelist))

    #---------------------------------------------------------------------------------------------------------------------------------------------#
    # TEXT TO SPEECH                                                                                                                              #
    #---------------------------------------------------------------------------------------------------------------------------------------------#

    else:
        bot.sendMessage(chat_id, str('ups, algo no funciono como debia'))
        # Language in which you want to convert
        language = 'ES'

        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed
        myobj = gTTS(text=comand, lang=language, slow=False)

        # Saving the converted audio in a mp3 file named
        # welcome
        myobj.save("texttospeech.mp3")

        # Send audio
        audio = open('texttospeech.mp3', 'rb')
        bot.sendAudio(chat_id, audio)

        # Delete mp3
        os.remove("texttospeech.mp3")

    

#-------------------------------------------------------------------------------------------------------------------------------------------------#

bot = telepot.Bot('943502242:AAEJQcgNZelvz6r1qZno5ULbw6Yo3BYEb20')
MessageLoop(bot, handle).run_as_thread()


# forever loop

while 1:

    time.sleep(1)

