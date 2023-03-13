#!/usr/bin /env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Wed Apr 26 08:10:22 2017
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""




from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding
import random 

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'auditory'  # from the Builder filename that created this script
expInfo = {u'starget': u'', u'ttarget': u'', u'PartID': u''} # starget: SSL target. ttarget: ASL target (third stimulus in the triplet)
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['Run'] = "1"
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['PartID'], expName, expInfo['Run'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='grey', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess



# Initialize components for Routine "instr3_5"
instr3_5Clock = core.Clock()
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text="Are you ready for the game? Let's get started. Remember to press the button when you hear the alien's favorite word or note.",    font='Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_15 = visual.ImageStim(win=win, name='image_15',
    image='Alien21.png', mask=None,
    ori=0, pos=[.5, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "sreminder"
sreminderClock = core.Clock()
sreminder_sound = sound.Sound('reminder_%s.wav' % str(expInfo['starget']), secs=-1)
sreminder_sound.setVolume(1)

# Initialize components for Routine "first_TA"
first_TAClock = core.Clock()
TA_first = visual.TextStim(win=win, ori=0, name='TA_first',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "fam_trials"
fam_trialsClock = core.Clock()
fam_trials_sound = sound.Sound('A', secs=-1)
fam_trials_sound.setVolume(1)
fam_trials_image = visual.ImageStim(win=win, name='fam_trials_image',
    image=u'Alien21.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "trial"
trialClock = core.Clock()
tone = sound.Sound('A', secs=-1)
tone.setVolume(1)
alien = visual.ImageStim(win=win, name='alien',
    image='Alien24.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "treminder"
#treminderClock = core.Clock()
#treminder_text = visual.TextStim(win=win, ori=0, name='treminder_text',
#    text='Now press the button when you hear this!',    font='Arial',
#    pos=[0, 0], height=0.1, wrapWidth=None,
#    color='black', colorSpace='rgb', opacity=1,
#    depth=0.0)
#treminder_sound = sound.Sound('reminder_%s.wav' % str(expInfo['ttarget']), secs=-1)
#treminder_sound.setVolume(1)
#
blockList = ['1','2','3','4','5','6']
random.shuffle(blockList)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instr3_5"-------
t = 0
instr3_5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_13 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_13.status = NOT_STARTED
# keep track of which components have finished
instr3_5Components = []
instr3_5Components.append(text_11)
instr3_5Components.append(key_resp_13)
instr3_5Components.append(image_15)
for thisComponent in instr3_5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3_5"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3_5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if t >= 0.0 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t  # underestimates by a little under one frame
        text_11.frameNStart = frameN  # exact frame index
        text_11.setAutoDraw(True)
    
    # *key_resp_13* updates
    if t >= 0.0 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t  # underestimates by a little under one frame
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_5', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_15* updates
    if t >= 0.0 and image_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_15.tStart = t  # underestimates by a little under one frame
        image_15.frameNStart = frameN  # exact frame index
        image_15.setAutoDraw(True)

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3_5"-------
for thisComponent in instr3_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr3_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


for fileName in blockList:
        if (int(fileName[-1:])%2 == 0):
#            #------Prepare to start Routine "treminder"-------
#            t = 0
#            treminderClock.reset()  # clock 
#            frameN = -1
#            routineTimer.add(4.0000)
#            
#            # update component parameters for each repeat
#            treminder_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
#            treminder_key_resp.status = NOT_STARTED
#            # keep track of which components have finished
#            treminderComponents = []
#            treminderComponents.append(treminder_sound)
#            
#            for thisComponent in treminderComponents:
#                if hasattr(thisComponent, 'status'):
#                    thisComponent.status = NOT_STARTED
#            
#            #-------Start Routine "treminder"-------
#            continueRoutine = True
#            while continueRoutine and routineTimer.getTime() > 0:
#                # get current time
#                t = treminderClock.getTime()
#                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
#                # update/draw components on each frame
#                
#                 
#                    
#                # start/stop treminder_sound
#                if t >= 0.0 and treminder_sound.status == NOT_STARTED:
#                    # keep track of start time/frame for later
#                    treminder_sound.tStart = t  # underestimates by a little under one frame
#                    treminder_sound.frameNStart = frameN  # exact frame index
#                    treminder_sound.play()  # start the sound (it finishes automatically)
#                # check if all components have finished
#                if not continueRoutine:  # a component has requested a forced-end of Routine
#                    break
#                continueRoutine = False  # will revert to True if at least one component still running
#                for thisComponent in treminderComponents:
#                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#                        continueRoutine = True
#                        break  # at least one component has not yet finished
#                
#                # check for quit (the Esc key)
#                if endExpNow or event.getKeys(keyList=["escape"]):
#                    core.quit()
#                
#                # refresh the screen
#                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
#                    win.flip()
#            
#            #-------Ending Routine "treminder"-------
#            for thisComponent in treminderComponents:
#                if hasattr(thisComponent, "setAutoDraw"):
#                    thisComponent.setAutoDraw(False)
#            treminxder_sound.stop() #ensure sound has stopped at end of routine
#            # the Routine "treminder" was not non-slip safe, so reset the non-slip timer
#            routineTimer.reset()
            
            
            # set up handler to look after randomisation of conditions etc
            trials_1 = data.TrialHandler(nReps=1, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions(u'auditory_run1_%s.csv'%(str(fileName))),
                seed=None, name='trials_1')
            thisExp.addLoop(trials_1)  # add the loop to the experiment
            thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb=thisTrial_1.rgb)
            if thisTrial_1 != None:
                for paramName in thisTrial_1.keys():
                    exec(paramName + '= thisTrial_1.' + paramName)
            
            for thisTrial_1 in trials_1:
                currentLoop = trials_1
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
                if thisTrial_1 != None:
                    for paramName in thisTrial_1.keys():
                        exec(paramName + '= thisTrial_1.' + paramName)
                
                #------Prepare to start Routine "trial"-------
                t = 0
                trialClock.reset()  # clock 
                frameN = -1
                routineTimer.add(0.480000)
                # update component parameters for each repeat
                tone.setSound(soundFile, secs=0.46)
                random_block_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
                random_block_key_resp.status = NOT_STARTED
                # keep track of which components have finished
                trialComponents = []
                trialComponents.append(tone)
                trialComponents.append(alien)
                trialComponents.append(random_block_key_resp)
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                #-------Start Routine "trial"-------
                continueRoutine = True
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = trialClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # start/stop tone
                    if t >= 0.0 and tone.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        tone.tStart = t  # underestimates by a little under one frame
                        tone.frameNStart = frameN  # exact frame index
                        tone.play()  # start the sound (it finishes automatically)
                    if tone.status == STARTED and t >= (0.0 + (0.48-win.monitorFramePeriod*0.75)): #most of one frame period left
                        tone.stop()  # stop the sound (if longer than duration)
                    
                    # *alien* updates
                    if t >= 0.0 and alien.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        alien.tStart = t  # underestimates by a little under one frame
                        alien.frameNStart = frameN  # exact frame index
                        alien.setAutoDraw(True)
                    if alien.status == STARTED and t >= (0.0 + (.48-win.monitorFramePeriod*0.75)): #most of one frame period left
                        alien.setAutoDraw(False)
                    
                    # *random_block_key_resp* updates
                    if t >= 0.0 and random_block_key_resp.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        random_block_key_resp.tStart = t  # underestimates by a little under one frame
                        random_block_key_resp.frameNStart = frameN  # exact frame index
                        random_block_key_resp.status = STARTED
                        # keyboard checking is just starting
                        win.callOnFlip(random_block_key_resp.clock.reset)  # t=0 on next screen flip
                        event.clearEvents(eventType='keyboard')
                    if random_block_key_resp.status == STARTED and t >= (0.0 + (0.48-win.monitorFramePeriod*0.75)): #most of one frame period left
                        random_block_key_resp.status = STOPPED
                    if random_block_key_resp.status == STARTED:
                        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            random_block_key_resp.keys = theseKeys[-1]  # just the last key pressed
                            random_block_key_resp.rt = random_block_key_resp.clock.getTime()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trialComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                #-------Ending Routine "trial"-------
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                tone.stop() #ensure sound has stopped at end of routine
                # check responses
                if random_block_key_resp.keys in ['', [], None]:  # No response was made
                   random_block_key_resp.keys=None
                # store data for trials_1 (TrialHandler)
                trials_1.addData('tone_block_key_resp.keys',random_block_key_resp.keys)
                if random_block_key_resp.keys != None:  # we had a response
                    trials_1.addData('tone_block_key_resp.rt', random_block_key_resp.rt)
                thisExp.nextEntry()
            
        elif (int(fileName[-1:])%2 != 0):
            #------Prepare to start Routine "sreminder"-------
            t = 0
            sreminderClock.reset()  # clock 
            frameN = -1
            routineTimer.add(4.0000)
            
            # update component parameters for each repeat
            sreminder_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            sreminder_key_resp.status = NOT_STARTED
            # keep track of which components have finished
            sreminderComponents = []
            sreminderComponents.append(sreminder_sound)
            
            for thisComponent in sreminderComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "sreminder"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sreminderClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                 
                    
                # start/stop sreminder_sound
                if t >= 0.0 and sreminder_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    sreminder_sound.tStart = t  # underestimates by a little under one frame
                    sreminder_sound.frameNStart = frameN  # exact frame index
                    sreminder_sound.play()  # start the sound (it finishes automatically)
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sreminderComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "sreminder"-------
            for thisComponent in sreminderComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            sreminder_sound.stop() #ensure sound has stopped at end of routine
            # the Routine "sreminder" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            
            # set up handler to look after randomisation of conditions etc
            fam_trials_loop = data.TrialHandler(nReps=1, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions(u'auditory_run1_%s.csv'%(str(fileName))),
                seed=None, name='fam_trials_loop')
            thisExp.addLoop(fam_trials_loop)  # add the loop to the experiment
            thisFam_trials_loop = fam_trials_loop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb=thisFam_trials_loop.rgb)
            if thisFam_trials_loop != None:
                for paramName in thisFam_trials_loop.keys():
                    exec(paramName + '= thisFam_trials_loop.' + paramName)
            
            for thisFam_trials_loop in fam_trials_loop:
                currentLoop = fam_trials_loop
                # abbreviate parameter names if possible (e.g. rgb = thisFam_trials_loop.rgb)
                if thisFam_trials_loop != None:
                    for paramName in thisFam_trials_loop.keys():
                        exec(paramName + '= thisFam_trials_loop.' + paramName)
                
                #------Prepare to start Routine "fam_trials"-------
                t = 0
                fam_trialsClock.reset()  # clock 
                frameN = -1
                routineTimer.add(0.480000)
                # update component parameters for each repeat
                fam_trials_sound.setSound(soundFile, secs=0.46)
                structured_block_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
                structured_block_key_resp.status = NOT_STARTED
                # keep track of which components have finished
                fam_trialsComponents = []
                fam_trialsComponents.append(fam_trials_sound)
                fam_trialsComponents.append(structured_block_key_resp)
                fam_trialsComponents.append(fam_trials_image)
                for thisComponent in fam_trialsComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                #-------Start Routine "fam_trials"-------
                continueRoutine = True
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = fam_trialsClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # start/stop fam_trials_sound
                    if t >= 0.0 and fam_trials_sound.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        fam_trials_sound.tStart = t  # underestimates by a little under one frame
                        fam_trials_sound.frameNStart = frameN  # exact frame index
                        fam_trials_sound.play()  # start the sound (it finishes automatically)
                    if fam_trials_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                        fam_trials_sound.stop()  # stop the sound (if longer than duration)
                    
                    # *structured_block_key_resp* updates
                    if t >= 0.0 and structured_block_key_resp.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        structured_block_key_resp.tStart = t  # underestimates by a little under one frame
                        structured_block_key_resp.frameNStart = frameN  # exact frame index
                        structured_block_key_resp.status = STARTED
                        # keyboard checking is just starting
                        win.callOnFlip(structured_block_key_resp.clock.reset)  # t=0 on next screen flip
                        event.clearEvents(eventType='keyboard')
                    if structured_block_key_resp.status == STARTED and t >= (0.0 + (0.48-win.monitorFramePeriod*0.75)): #most of one frame period left
                        structured_block_key_resp.status = STOPPED
                    if structured_block_key_resp.status == STARTED:
                        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            structured_block_key_resp.keys = theseKeys[-1]  # just the last key pressed
                            structured_block_key_resp.rt = structured_block_key_resp.clock.getTime()
                    
                    # *fam_trials_image* updates
                    if t >= 0.0 and fam_trials_image.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        fam_trials_image.tStart = t  # underestimates by a little under one frame
                        fam_trials_image.frameNStart = frameN  # exact frame index
                        fam_trials_image.setAutoDraw(True)
                    if fam_trials_image.status == STARTED and t >= (0.0 + (0.48-win.monitorFramePeriod*0.75)): #most of one frame period left
                        fam_trials_image.setAutoDraw(False)
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in fam_trialsComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                #-------Ending Routine "fam_trials"-------
                for thisComponent in fam_trialsComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                fam_trials_sound.stop() #ensure sound has stopped at end of routine
                # check responses
                if structured_block_key_resp.keys in ['', [], None]:  # No response was made
                   structured_block_key_resp.keys=None
                # store data for fam_trials_loop (TrialHandler)
                fam_trials_loop.addData('sound_block_key_resp.keys',structured_block_key_resp.keys)
                if structured_block_key_resp.keys != None:  # we had a response
                    fam_trials_loop.addData('sound_block_key_resp.rt', structured_block_key_resp.rt)
                thisExp.nextEntry()
    

    


    
    
    
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
