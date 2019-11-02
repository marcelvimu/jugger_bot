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

#-------------------------------------------------------------------------------------------------------------------------------------------------#
# handle FUNCION                                                                                                                                  #
#-------------------------------------------------------------------------------------------------------------------------------------------------#
flag = 0;
flag1 = 0;
i = 0;
q = 0;
thelist = [];
thelistb = [];
thelistd = [];
thelistf = [];
thelisth = [];
thelistj = [];
thelistk = [];

def toCsvGroup (msg):
   a = msg['message_id']
   diaSemana = datetime.datetime.fromtimestamp(msg['date']).strftime("%A")
   mes = datetime.datetime.fromtimestamp(msg['date']).strftime("%B")
   diaMes = datetime.datetime.fromtimestamp(msg['date']).strftime("%d")
   ano = datetime.datetime.fromtimestamp(msg['date']).strftime("%Y")
   hora = datetime.datetime.fromtimestamp(msg['date']).strftime("%I")
   minuto = datetime.datetime.fromtimestamp(msg['date']).strftime("%M")
   segundo = datetime.datetime.fromtimestamp(msg['date']).strftime("%S")
   b = msg['from']['id']
   c = msg['from']['is_bot']
   d = msg['from']['first_name']
   e = msg['from']['language_code']
   f = msg['chat']['id']
   g = msg['chat']['title']
   h = msg['chat']['type']
   i = msg['date']
   if 'text' in  msg:
       j = msg['text']
   else:
       j = 'none'
   if 'location' in msg:
       k = msg['location']['latitude']
       l = msg['location']['longitude']
       bot.sendLocation('729727689',k,l)
   else:
       k = 'none'
       l = 'none'
   label = ['Msg_Id','Dia_Semana','Mes','Dia_Mes','Ano','Hora','Minuto','Segundo','From_Id','From_is_bot','From_FirstName','From_Language_code','Chat_id','Chat_Title','Chat_Type','Date','Text']
   row = [a,diaSemana,mes,diaMes,ano,hora,minuto,segundo,b,c,d,e,f,g,h,i,j,k,l]
   with open('./dumpData/export_data.csv', 'a') as csvFile:
       writer = csv.writer(csvFile)
#        writer.writerow(label)
       writer.writerow(row)
   csvFile.close()

def handle(msg):
    
    global flag
    global flag1
    global thelist
    global thelistb
    global thelistd
    global thelistf
    global thelisth
    global thelistj
    global thelistk
    global q
    global i

    chat_id = msg['chat']['id']
    comand = msg['text']
    name = msg['from']['first_name']
    print ('show chat_id: %s' % (chat_id))
    print ('show user name: %s' % (name))
    print ('Comando recibido: %s' % (comand)) 
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
       bot.sendMessage(chat_id, str('Saludos Humano, bienvenido a las primeras pruebas del jugger bot'))
       bot.sendMessage(chat_id, str('Soy el jugger bot, es placer conocerte %s , puedes referirte a mi como ello, ya que soy un ser de genero no binario' % (name)))
       bot.sendMessage(chat_id, str('Estas contribuyendo a que mi creador Marcel, no me desintegre con un suprimir.'))
       bot.sendMessage(chat_id, str('Para ayudarme necesito que lo primero que me digas sea "yo",muchas gracias %s' % name ))
       bot.sendMessage(chat_id, str('Cuando hayas terminado pasale una captura a mi dios Marcel, muchas gracias besis de fresi'))
       bot.sendMessage(chat_id, str('Una ultima cosa, como has visto no escribo tildes ya que me sientan muy mal asi que te pido por favor que tu tampoco lo hagas, si no me haras pupita'))
       bot.sendMessage(chat_id, str('Ahora a lo que ibamos, quien entrena'))
       bot.sendMessage(chat_id,str('Show chat id %s' %(chat_id)))
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
        bot.sendMessage(chat_id, str('Une bot no humanoide'))
        time.sleep(2)
        bot.sendMessage(chat_id, str('Concebide como une soldade virtualmente indestructible en el campo de batalla.'))
        time.sleep(3)
        bot.sendMessage(chat_id, str('Soy le asesine predilecte de Skynet.'))

    #---------------------------------------------------------------------------------------------------------------------------------------------#

    elif command == 'CUENTAME UN CHISTE':
        bot.sendMessage(chat_id, str('Esto es un caracol y derrapa'))

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
        b = msg['from']['id']
        d = msg['from']['first_name']
        f = msg['chat']['id']
        h = msg['chat']['type']
        j = 'SI'
        thelist.insert(i,name)
        thelistb.insert(i,b)
        thelistd.insert(i,d)
        thelistf.insert(i,f)
        thelisth.insert(i,h)
        thelistj.insert(i,j)
        print (thelist[i])
        i += 1
        print ('Show the nex index to be stored: %s'  % (i))
    elif flag == 1 and command == 'SI' :
        bot.sendMessage(chat_id, str('Que arma necesitas?'))
        flag = 0
        flag1 = 1
    elif flag == 1 and command == 'NO':
        bot.sendMessage(chat_id, str('Perfecto %s, nos vemos en el entreno' % name))
        flag = 0
        k = 'No necesita'
        y = thelist.index(name)
        thelistk.insert(y,k) 
    elif flag1 == 1:
        bot.sendMessage(chat_id, str('Necesitas un %s ?, te lo guardo' % command))
        flag1 = 0
        x = thelist.index(name)
        print ('Show the index: %s'% (x)) 
        thelistk.insert( x, command)
        print (thelist[x])
    elif command == 'MUESTRAME QUIEN ENTRENA' and name == 'Marcel':
        bot.sendMessage(chat_id, str(thelist))
    elif command == 'MUESTRAME QUIEN ENTRENA' and name != 'Marcel':
    	bot.sendMessage(chat_id, str('Si no eres Marcel no puedo darte esta informacion, está clasificada no intentes hackearme o te arrepentiras'))
    elif command == 'GRACIAS':
    	bot.sendMessage(chat_id, str('De nada %s , a mandar' % (name)))
    elif command == 'CSV' and name == 'Marcel':
    	toCsvGroup(msg)
    	bot.sendMessage(chat_id, str('Cabezales csv inicializados'))
    elif command == 'ESCRIBIR CSV' and name == 'Marcel':
    	q = 0
    	while q <= len(thelist):
    		toCsvGroup(msg)
    		q += 1
    elif commando =='ESCRIBIR CSV'  and name != 'Marcel':
    	bot.sendMessage(chat_id, str('... tu no eres marcel, no vuelvas a utilizar este comando'))
    elif commando =='CSV'  and name != 'Marcel':
    	bot.sendMessage(chat_id, str('... tu no eres marcel, no vuelvas a utilizar este comando'))    	
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

