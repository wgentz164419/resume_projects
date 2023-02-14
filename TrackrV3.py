import tkinter as tk
from tkinter import *
import csv
from datetime import date

app = tk.Tk()
today = date.today()
today = today.strftime("%Y-%m-%d")
app.title("Trackr")
i = 0
inning = 1
side = 'Top'
balls = 0
strikes = 0
outs = 0
lastPitcher = ''
awayLineup = ['', '', '', '', '', '', '', '','']
homeLineup = ['', '', '', '', '', '', '', '','']
awayPos = 0
homePos = 0
KorBB = ''
def ButtonAction():
    global i, strikes, balls, outs, inning, side, lastPitcher, awayPos, homePos, awayLineup, homeLineup, KorBB
    KorBB = ''
    #GET PITCH DETAILS
    pitcher = entryPitcher.get()
    pitcherTeam = entryPTeam.get()
    pitcherHand = pHand.get()
    date = entryDate.get()
    batter = entryBatter.get()
    batterTeam = entryBTeam.get()
    batterHand = bHand.get()
    pitch = taggedPitch.get()
    velo = entryVelo.get()
    pitchCall = pitchResult.get()
    result = hitResult.get()
    hit = hitType.get()
    note = entryNote.get()
    taggedPitch.set('')
    entryVelo.delete(0, 'end')
    pitchResult.set('')
    hitResult.set('')
    hitType.set('')
    entryNote.delete(0, 'end')
    if strikes == 2 and (pitchCall == 'StrikeCalled' or pitchCall == 'StrikeSwinging'):
        KorBB = 'Strikeout'
    if balls == 3 and pitchCall == 'BallCalled':
        KorBB = 'Walk'
    #CREATE/WRITE TO CSV
    if i == 0:
        with open(str(today + "pitching.csv"), 'w', newline='') as f:
            colnames = ['Pitcher', 'PitcherTeam', 'PitcherSide', 'Batter', 'BatterTeam', 'BatterSide', 'Date', 'TaggedPitchType',
            'RelSpeed', 'Balls', 'Strikes', 'PitchCall', 'PlayResult', 'HitType', 'PlateLocSide', 'PlateLocHeight', 'Note', 'KorBB']
            w = csv.DictWriter(f, fieldnames=colnames)
            w.writeheader()
            w.writerow({'Pitcher':pitcher, 'PitcherTeam':pitcherTeam, 'PitcherSide':pitcherHand, 'Batter':batter, 'BatterTeam':batterTeam, 'BatterSide':batterHand,
            'Date':date, 'TaggedPitchType':pitch, 'RelSpeed':velo, 'Balls':balls, 'Strikes':strikes, 'PitchCall':pitchCall, 'PlayResult':result, 'HitType':hit,
            'PlateLocSide':PlateLocSide, 'PlateLocHeight':PlateLocHeight, 'Note':note, 'KorBB':KorBB})
            i = i + 1
    else:
        with open(str(today + "pitching.csv"), 'a') as q:
            nWriter = csv.writer(q)
            nWriter.writerow([pitcher, pitcherTeam, pitcherHand, batter, batterTeam, batterHand, date, pitch, velo, balls, strikes, pitchCall,
            result, hit, PlateLocSide, PlateLocHeight, note, KorBB])
            i = i + 1
    #COUNT CHANGES
    if pitchCall == 'StrikeCalled' or pitchCall == 'StrikeSwinging':
        strikes = strikes + 1
    if pitchCall == 'FoulBall' and strikes < 2:
        strikes = strikes + 1
    if pitchCall == 'BallCalled':
        balls = balls + 1
    #STRIKEOUT/WALK CHECK
    if strikes == 3:
        KorBB = 'Strikeout'
        outs = outs + 1
        strikes = 0
        balls = 0
        if side == "Top":
            awayLineup[awayPos] = batter
            awayPos = awayPos + 1
            if awayPos == 9:
                awayPos = 0
            entryBatter.delete(0,'end')
            entryBatter.insert(0, awayLineup[awayPos])
        if side == 'Bottom':
            homeLineup[homePos] = batter
            homePos = homePos + 1
            if homePos == 9:
                homePos = 0
            entryBatter.delete(0,'end')
            entryBatter.insert(0, homeLineup[homePos])
        bHand.set('')
    if balls == 4:
        KorBB = 'Walk'
        strikes = 0
        balls = 0
        if side == "Top":
            awayLineup[awayPos] = batter
            awayPos = awayPos + 1
            if awayPos == 9:
                awayPos = 0
            entryBatter.delete(0,'end')
            entryBatter.insert(0, awayLineup[awayPos])
        if side == 'Bottom':
            homeLineup[homePos] = batter
            homePos = homePos + 1
            if homePos == 9:
                homePos = 0
            entryBatter.delete(0,'end')
            entryBatter.insert(0, homeLineup[homePos])
        bHand.set('')
    #HBP OPTION
    if pitchCall == 'HitByPitch':
        strikes = 0
        balls = 0
        if side == "Top":
            awayLineup[awayPos] = batter
            awayPos = awayPos + 1
            if awayPos == 9:
                awayPos = 0
            entryBatter.delete(0,'end')
            entryBatter.insert(0, awayLineup[awayPos])
        if side == 'Bottom':
            homeLineup[homePos] = batter
            homePos = homePos + 1
            if homePos == 9:
                homePos = 0
            entryBatter.delete(0,'end')
            entryBatter.insert(0, homeLineup[homePos])
        bHand.set('')
    #BALL IN PLAY CHANGES
    if pitchCall == "InPlay":
        strikes = 0
        balls = 0
        if side == "Top":
            awayLineup[awayPos] = batter
            awayPos = awayPos + 1
            if awayPos == 9:
                awayPos = 0
            entryBatter.delete(0,'end')
            entryBatter.insert(0, awayLineup[awayPos])
        if side == 'Bottom':
            homeLineup[homePos] = batter
            homePos = homePos + 1
            if homePos == 9:
                homePos = 0
            entryBatter.delete(0,'end')
            entryBatter.insert(0, homeLineup[homePos])
        bHand.set('')
    #OUT(S) CHANGES
    if result == 'Out' or result == 'FieldersChoice':
        outs = outs + 1
    if result == 'DoublePlay':
        outs = outs + 2
    if result == 'TriplePlay':
        outs = outs + 3
    #INNING CHANGES (TOP)
    if outs > 2 and side == 'Top':
        strikes = 0
        balls = 0
        if inning == 1 and side == "Top":
            lastPitcher = entryPitcher.get()
        else:
            finishedInningPitcher = entryPitcher.get()
            entryPitcher.insert(0, lastPitcher)
            lastPitcher = finishedInningPitcher
        entryPitcher.delete(0, 'end')
        pTeam = entryPTeam.get()
        entryPTeam.delete(0, 'end')
        entryPTeam.insert(0, entryBTeam.get())
        entryBTeam.delete(0, 'end')
        entryBTeam.insert(0, pTeam)
        entryBatter.delete(0, 'end')
        pHand.set('')
        outs = 0
        side = 'Bottom'
    #INNING CHANGE (BOTTOM)
    if outs > 2 and side == 'Bottom':
        balls = 0
        strikes = 0
        finishedInningPitcher = entryPitcher.get()
        entryPitcher.insert(0, lastPitcher)
        lastPitcher = finishedInningPitcher
        entryPitcher.delete(0, 'end')
        pTeam = entryPTeam.get()
        entryPTeam.delete(0, 'end')
        entryPTeam.insert(0, entryBTeam.get())
        entryBTeam.delete(0, 'end')
        entryBTeam.insert(0, pTeam)
        entryBatter.delete(0, 'end')
        pHand.set('')
        outs = 0
        side = 'Top'
        inning = inning + 1
    labelCount.config(text = str('Balls: ' + str(balls) + " | Strikes: " + str(strikes)))
    labelOuts.config(text = str("Outs: " + str(outs)))
    labelInning.config(text = str("Inning: " + side + " of the " + str(inning)))

#PICKOFF/CAUGHT STEALING BUTTON
def Pickoff():
    global outs, strikes, balls, inning, side, lastPitcher
    outs = outs + 1
    #INNING CHANGES (TOP)
    if outs > 2 and side == 'Top':
        strikes = 0
        balls = 0
        if inning == 1 and side == "Top":
            lastPitcher = entryPitcher.get()
        else:
            finishedInningPitcher = entryPitcher.get()
            entryPitcher.insert(0, lastPitcher)
            lastPitcher = finishedInningPitcher
        entryPitcher.delete(0, 'end')
        pTeam = entryPTeam.get()
        entryPTeam.delete(0, 'end')
        entryPTeam.insert(0, entryBTeam.get())
        entryBTeam.delete(0, 'end')
        entryBTeam.insert(0, pTeam)
        entryBatter.delete(0, 'end')
        pHand.set('')
        outs = 0
        side = 'Bottom'
    #INNING CHANGE (BOTTOM)
    if outs > 2 and side == 'Bottom':
        balls = 0
        strikes = 0
        finishedInningPitcher = entryPitcher.get()
        entryPitcher.insert(0, lastPitcher)
        lastPitcher = finishedInningPitcher
        entryPitcher.delete(0, 'end')
        pTeam = entryPTeam.get()
        entryPTeam.delete(0, 'end')
        entryPTeam.insert(0, entryBTeam.get())
        entryBTeam.delete(0, 'end')
        entryBTeam.insert(0, pTeam)
        entryBatter.delete(0, 'end')
        pHand.set('')
        outs = 0
        side = 'Top'
        inning = inning + 1
    labelCount.config(text = str('Balls: ' + str(balls) + " | Strikes: " + str(strikes)))
    labelOuts.config(text = str("Outs: " + str(outs)))
    labelInning.config(text = str("Inning: " + side + " of the " + str(inning)))

#UNDO BUTTON
def Undo():
    f = open(str(today + "pitching.csv"), 'w')
    lines = f.readlines()
    lines = lines[:-1]
    cWriter = csv.writer(f, newline = '')
    for line in lines:
        cWriter.writerow(line)

pHand = tk.StringVar(app)
bHand = tk.StringVar(app)
taggedPitch = tk.StringVar(app)
pitchResult = tk.StringVar(app)
hitResult = tk.StringVar(app)
hitType = tk.StringVar(app)

#APP FRAME CREATION
canvas = tk.Canvas(app,height = 1400, width = 700 )
canvas.pack()

frame = tk.Frame(app, bg = 'steel blue')
frame.place(relwidth=1, relheight=1)

#LABEL/MENUS/ENTRY BOX CREATION
labelCount = tk.Label(frame, text = str('Balls: ' + str(balls) + " | Strikes: " + str(strikes)), bg = 'steel blue')
labelCount.pack()
labelOuts = tk.Label(frame, text = str("Outs: " + str(outs)), bg = 'steel blue')
labelOuts.pack()
labelInning = tk.Label(frame, text = str("Inning: " + side + " of the " + str(inning)), bg = 'steel blue')
labelInning.pack()

labelPitcher = tk.Label(frame, text = "Pitcher Name", bg = "steel blue")
labelPitcher.pack()
entryPitcher = tk.Entry(frame, bg = 'gray')
entryPitcher.pack()

labelPitcherTeam = tk.Label(frame, text = "Pitcher's Team", bg = "steel blue")
labelPitcherTeam.pack()
entryPTeam = tk.Entry(frame, bg = 'gray')
entryPTeam.pack()

labelPitcherHand = tk.Label(frame, text = "Pitcher's Handedness", bg = "steel blue")
labelPitcherHand.pack()
entryPHand = tk.OptionMenu(frame, pHand, *['Right', 'Left'])
entryPHand.pack()

labelDate = tk.Label(frame, text = "Date (Year-Month-Day)", bg='steel blue')
labelDate.pack()
entryDate = tk.Entry(frame, bg = 'gray')
entryDate.insert(0, str(today))
entryDate.pack()

labelBatter = tk.Label(frame, text = "Batter Name", bg = "steel blue")
labelBatter.pack()
entryBatter = tk.Entry(frame, bg = 'gray')
entryBatter.pack()

labelBatterTeam = tk.Label(frame, text = "Batter's Team", bg = "steel blue")
labelBatterTeam.pack()
entryBTeam = tk.Entry(frame, bg = 'gray')
entryBTeam.pack()

labelBatterHand = tk.Label(frame, text = "Batter's Handedness", bg = "steel blue")
labelBatterHand.pack()
entryBHand = tk.OptionMenu(frame, bHand, *['Right', 'Left'])
entryBHand.pack()

labelPitch = tk.Label(frame, text = "Pitch Type", bg = 'steel blue')
labelPitch.pack()
entryPitch = tk.OptionMenu(frame, taggedPitch,*['Fastball', 'Curveball', 'ChangeUp', 'Slider', 'Cutter', 'Sinker', 'Knuckleball','Other'])
entryPitch.pack()

labelVelo = tk.Label(frame, text = "Release Speed", bg = "steel blue")
labelVelo.pack()
entryVelo = tk.Entry(frame, bg = 'gray')
entryVelo.pack()

labelPitchCall = tk.Label(frame, text = "Pitch Result", bg = 'steel blue')
labelPitchCall.pack()
entryPitchCall = tk.OptionMenu(frame, pitchResult,*['StrikeCalled', 'StrikeSwinging', 'BallCalled', 'FoulBall', 'InPlay', 'HitByPitch', 'Other'])
entryPitchCall.pack()

labelResult = tk.Label(frame, text = "Play Result", bg = "steel blue")
labelResult.pack()
entryResult = tk.OptionMenu(frame, hitResult, *['Single', 'Double', 'Triple', 'HomeRun', 'Out', 'DoublePlay','TriplePlay', 'Error', 'FieldersChoice', 'Other'])
entryResult.pack()

labelHitType = tk.Label(frame, text = "Hit Type", bg = "steel blue")
labelHitType.pack()
entryHitType = tk.OptionMenu(frame, hitType, *['Groundball', 'LineDrive', 'FlyBall', 'PopUp', 'Bunt'])
entryHitType.pack()

labelNote = tk.Label(frame, text = "Notes", bg = 'steel blue')
labelNote.pack()
entryNote = tk.Entry(frame, bg = "gray")
entryNote.pack()

#PITCH LOCATION
zone = tk.PhotoImage(file = "StrikeZoneSAU.png")
labelZone = Label(frame, image = zone)
labelZone.place(x=74, y=70)
pitchLoc = Label(frame, text = "", bg = "steel blue")
pitchLoc.place(x=105, y=625)
def callback(e):
    global PlateLocSide, PlateLocHeight
    horz = e.x
    height = e.y
    if horz < 390 and horz > 70:
        PlateLocSide= round(((horz-229)/52.5), 3)
        PlateLocHeight = round(((438-height)/65.85), 3)
        pitchLoc.config(text="Pitch was located " + str(PlateLocHeight) + "ft. high and " + str(PlateLocSide) + "ft. from " + 
        "the middle of the plate")
app.bind('<Button-3>', callback)

button = tk.Button(frame, text = "Store Pitch", bg = "steel blue", fg = 'black', command = ButtonAction)
button.pack()

pickoff = tk.Button(frame, text = 'Pickoff/Caught Stealing', bg = "steel blue", fg = 'black', command = Pickoff)
pickoff.pack()

undo = tk.Button(frame, text = "Undo Last Pitch", bg = "yellow", fg = 'black', command=Undo)
undo.pack()

app.mainloop()