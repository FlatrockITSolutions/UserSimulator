'''
Skippy Flatrock
User Simulator
    Designed to simulate user input via mouse and keyboard control. 
'''
import time, mouse, keyboard, datetime,os,pyautogui,clipboard

def createLogFolder(folderPath):
    try:
        os.mkdir(folderPath)
    except:
        t=1#print("Folder already exists:",folderPath)
    return folderPath+'/' 
def createFile(folderPath,fileName,ext):
    folderPath = createLogFolder(folderPath)
    timeName = str(datetime.datetime.now().replace(microsecond=0,)) # a new file is not going to be created in less than a second so the micro second numbers is not needed.
    timeName = timeName.replace(':',';')
    #filePath=folderPath+fileName+logFileName+".txt"
    filePath=folderPath+fileName+ext
    logEntry=filePath
    if os.path.exists(filePath):
        os.rename (filePath,filePath+" ("+timeName+")"+ext)
        #logEntry = "\n"+str(logEntry)
    else:
        log = open(filePath, 'a')
        log.write(logEntry)
        log.close()
    return filePath
def newEntry(logEntry,filePath): #Default Bot Log
    log = open(filePath, 'a')
    log.write("\n"+logEntry)
    log.close()
def readFile (filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    return lines

keyLog = False
if keyLog:
    filePath= createFile("KeyLog","Logged_Key_Presses",".txt")
while keyLog:
    tempp = ""
    if mouse.is_pressed("right"):
        tempp = "Right Click at: " + str(mouse.get_position())
        print (tempp)
        newEntry(tempp,filePath)        
    if mouse.is_pressed("left"):
        tempp = "Left Click at: "+ str(mouse.get_position())
        print (tempp)
        newEntry(tempp,filePath)        
    if mouse.is_pressed("middle"):
        tempp = "Middle Click at: "+ str(mouse.get_position())
        print (tempp)
        newEntry(tempp,filePath)    
    time.sleep(.1) # in seconds
if not keyLog:
    time.sleep(.5)
    movment = readFile("Source/Logged_Key_Presses.txt")
    textInput = readFile("Source/Source.csv")
    textOutput = createFile("Source","Output",".csv")
    #input check to see if link exists
    for stream in textInput:
        streamInfo = stream.split(",")
        
        print ("~~~~StreamInfo~~~~")
        print (streamInfo)
        link = ""
        if streamInfo[0].__contains__("/") and streamInfo[2].__contains__("/"):
        #print (movment[1])
            for line in movment:
                if line.__contains__("("):
                    lineSegments = line.split("(")
                    temp = lineSegments[1].split(")")
                    lineSegments[1]=temp[0]
                    lineSegments.append(temp[1])
                    position = lineSegments[1]
                    position = position.split(',')
                else:
                    lineSegments[0] = line
                    position  = [0,0] # place holder so there is no errors for position
                #print (line)
                #print ("liseSegments",lineSegments)        
                #print ("position", position)
                if lineSegments[0].__contains__("break"):
                    break
                if lineSegments[0].__contains__("Right Click"):
                    mouse.move(int(position[0]),int(position[1]),duration=0.5)
                    mouse.click('right')
                    print ("Right Click at: "+ str(mouse.get_position()))
                if lineSegments[0].__contains__("Left Click"):
                    mouse.move(int(position[0]),int(position[1]),duration=0.5)
                    mouse.click('left')
                    print ("Left Click at: "+ str(mouse.get_position()))
                if lineSegments[0].__contains__("Ctrl+A"):
                    #time.sleep(.5)
                    pyautogui.keyDown("ctrl")# Holds down key
                    pyautogui.press("a")# Presses the key once
                    pyautogui.keyUp("ctrl")# Lets go of the key    
                    print ("Ctrl+A")            
                if lineSegments[0].__contains__("Title"):
                    pyautogui.typewrite(streamInfo[2])
                    print ("Title",streamInfo[2])        
                if lineSegments[0].__contains__("Date"):
                    pyautogui.typewrite(streamInfo[0])
                    print ("Date",streamInfo[0])
                if lineSegments[0].__contains__("Time"):
                    temp = lineSegments[0].split("=")
                    pyautogui.typewrite(temp[1])
                    print ("Time",temp[1])
                if lineSegments[0].__contains__("Link Copied"):
                    link = clipboard.paste() # one cliboard entry behind (so have to copy twice)
                    print ("link: ",link)
                    info = streamInfo[0]+","+link+","+streamInfo[2].strip()
                    newEntry(info,textOutput)                    
                if lineSegments[0].__contains__("Pause"):
                    temp = lineSegments[0].split("=")
                    time.sleep(int(temp[1]))
                    print ("Pauseing:",temp[1],"seconds")
        else:
            print ("~~~~StreamInfo blank~~~~")
'''  syntax for mouse
# whether the right button is clicked
In [25]: mouse.is_pressed("right")
Out[25]: False
# move 100 right & 100 down
mouse.move(100, 100, absolute=False, duration=0.2)
# scroll down
mouse.wheel(-1)
# scroll upr
mouse.wheel(1)
'''