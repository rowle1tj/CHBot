import ImageGrab
import os, sys, shutil
import time
import cv2, cv
import win32api, win32con
import time
import random
from datetime import datetime, timedelta
import shutil

METHOD = cv.CV_TM_SQDIFF_NORMED

#LEFT_PADDING = 12
LEFT_PADDING = 0
#TOP_PADDING = 36
TOP_PADDING = 21
RIGHT_PADDING = 60
BOTTOM_PADDING = 56

WINDOW_IMAGE_LOCATION = os.getcwd() + '\\current_window.png'

class CHBot:
    def __init__(self):
        self.BOX_LEFT = 0
        self.BOX_RIGHT = 0
        self.BOX_TOP = 0
        self.BOX_BOTTOM = 0

        self.get_current_window()

        self.abilities = {
            'clickstorm' : [605, 165],
            'powersurge' : [605, 220],
            'lucky strikes' : [605, 275],
            'metal detector' : [605, 325],
            'golden clicks' : [605, 375],
            'super clicks' : [605, 475],

            'the dark ritual' : [605, 415],
            'energize' : [605, 515],
            'reload' : [605, 590]
        }

        self.time_for_screenshot = datetime.now()
        self.iteration_counter = 0

    def get_current_window(self):
        # Get a screenshot of the full screen
        im = ImageGrab.grab()
        filename = os.getcwd() + '\\full_screen.png'
        im.save(filename, 'PNG')
        full_screen = cv2.imread(filename)

        # load the top left image and the bottom right image
        top_left_image = cv2.imread(os.getcwd() + '\\templates\\top-left.png')
        bottom_right_image = cv2.imread(os.getcwd() + '\\templates\\bottom-right.png')

        result = cv2.matchTemplate(full_screen, top_left_image, METHOD)
        top_left_location = cv2.minMaxLoc(result)[2]

        result = cv2.matchTemplate(full_screen, bottom_right_image, METHOD)
        bottom_right_image_location = cv2.minMaxLoc(result)[2]

        # See what we found
        self.BOX_LEFT = top_left_location[0] - LEFT_PADDING
        self.BOX_TOP = top_left_location[1] - TOP_PADDING
        self.BOX_RIGHT = bottom_right_image_location[0] + RIGHT_PADDING
        self.BOX_BOTTOM = bottom_right_image_location[1] + BOTTOM_PADDING

        box = (
            self.BOX_LEFT,
            self.BOX_TOP,
            self.BOX_RIGHT,
            self.BOX_BOTTOM
        )

        im = ImageGrab.grab(box)
        im.save(WINDOW_IMAGE_LOCATION, 'PNG')
        self.update_window()

    def update_window(self):
        box = (
            self.BOX_LEFT,
            self.BOX_TOP,
            self.BOX_RIGHT,
            self.BOX_BOTTOM
        )

        im = ImageGrab.grab(box)
        im.save(WINDOW_IMAGE_LOCATION, 'PNG')
        self.window_image = cv2.imread(WINDOW_IMAGE_LOCATION)

    def activate_abilities(self):
        self.click(self.abilities['clickstorm'][0], self.abilities['clickstorm'][1])
        self.click(self.abilities['powersurge'][0], self.abilities['powersurge'][1])
        self.click(self.abilities['lucky strikes'][0], self.abilities['lucky strikes'][1])
        self.click(self.abilities['metal detector'][0], self.abilities['metal detector'][1])
        self.click(self.abilities['energize'][0], self.abilities['energize'][1])
        self.click(self.abilities['golden clicks'][0], self.abilities['golden clicks'][1])
        self.click(self.abilities['super clicks'][0], self.abilities['super clicks'][1])

    def invoke_the_dark_ritual(self):
        self.click(self.abilities['the dark ritual'][0], self.abilities['the dark ritual'][1])
        self.click(self.abilities['reload'][0], self.abilities['reload'][1])

    def click_farm_mode(self):
        self.click(1112, 250)

    def click(self, x, y):
        x += self.BOX_LEFT
        y += self.BOX_TOP
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

    def click_on_candy_cane(self):
        candy_cane_image = cv2.imread(os.getcwd() + '\\templates\\candy-cane.png')
        result = cv2.matchTemplate(self.window_image, candy_cane_image, METHOD)

        candy_cane_location = cv2.minMaxLoc(result)[2]

        x_location = candy_cane_location[0] + 10
        y_location = candy_cane_location[1] + 15

        self.click(x_location, y_location)

        #print "Clicked on a candy cane!"

    def apply_level_ups(self):
        sections = [
            # Samurai Section 35%
            [548, 285],
            # Ice Apprentice Section 25%
            [548, 344],
            # King's Guard Section 15%
            [548, 386],
            # Ma Zhu Section 10%
            [548, 448],
            # Aphrodite Section 10%
            [548, 495],
            # Dread Knight Section 5%
            [548, 543]
        ]

        the_decision = random.random()
        if the_decision <= 0.35:
            section = sections[0]
        elif the_decision <= 0.6:
            section = sections[1]
        elif the_decision <= 0.75:
            section = sections[2]
        elif the_decision <= 0.85:
            section = sections[3]
        elif the_decision <= 0.85:
            section = sections[4]    
        elif the_decision <= 1.0:
            section = sections[5]

        # scroll to the top
        self.click(548, 204)
        time.sleep(0.3)

        # scroll to the section
        self.click(section[0], section[1])
        time.sleep(0.3)

        hero_positions = [
            [45, 550],
            [45, 450],
            [45, 350],
            [45, 250]
        ]

        # There is a 40% chance we will apply levels top down
        if random.random() > 0.6:
            hero_positions.reverse()

        win32api.keybd_event(0x5A, 0, 0, 0) # hold down Z
        for i in range(0, 3):
            for hero in hero_positions:
                self.click(hero[0], hero[1])
        win32api.keybd_event(0x5A, 0, win32con.KEYEVENTF_KEYUP, 0) # release Z

    def hire_new_recruit_and_level(self):
        # click the scroll bar to go all the way to the bottom
        self.click(548, 601)
        time.sleep(0.3)

        # buy availaible upgrades
        self.click(371, 555)

        # Click to hire the new guy
        self.click(97, 466)

        # level the highest guy five levels if we can
        for i in range(0, 5):
            self.click(104, 347)

        # buy availaible upgrades
        self.click(371, 555)

    def click_the_evil_monster(self):
        self.click(850, 320)

    def scroll_to_top(self):
        self.click(547, 206)
        time.sleep(0.5)

    def scroll_to_bottom(self):
        self.click(547, 610)
        time.sleep(0.5)

    def buy_available_upgrades(self):
        self.scroll_to_bottom()
        self.click(364, 543)
        time.sleep(0.1)

    def control_click(self, x, y):
        # Control click the first three
        win32api.keybd_event(0x11, 0, 0, 0) # hold down Z
        self.click(x, y)
        time.sleep(0.1)
        win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0) # release Z
        time.sleep(0.1)

    def start_the_ascension(self):
        self.click_farm_mode()

        # Click four times per second for 32 seconds
        for i in range(0, 32 * 4):
            self.click_the_evil_monster()
            time.sleep(0.25)

        # Hire the first four
        self.click(54, 227) # Cid
        time.sleep(0.1)
        self.click(54, 338) # Treebeast
        time.sleep(0.1)
        self.click(54, 446) # Ivan
        time.sleep(0.1)
        self.click(54, 556) # Brittany
        time.sleep(0.1)

        # for 10 minutes, Every 10 seconds
        # Scroll to the top, scroll to the selftom, and hire
        before_time = datetime.now()
        current_time = datetime.now() - timedelta(minutes=3, seconds=15)
        while(current_time < before_time):
            self.scroll_to_top()
            time.sleep(0.5)
            self.scroll_to_bottom()
            time.sleep(0.75)

            # Attempt to hire a hero
            self.click(45, 454)

            time.sleep(0.25)

            # Catch one in the backlog if need be
            self.click(45, 346)

            time.sleep(7)
            current_time = datetime.now() - timedelta(minutes=3, seconds=15)
        
        self.scroll_to_top()
        time.sleep(0.5)


        # Control click all the heroes twice
        self.control_click(42, 215) # Cid
        time.sleep(0.1)
        self.control_click(42, 215)
        time.sleep(0.1)

        self.control_click(42, 316) # Treebeast
        time.sleep(0.1)
        self.control_click(42, 316)
        time.sleep(0.1)

        self.control_click(42, 415) # Ivan
        time.sleep(0.1)
        self.control_click(42, 415)
        time.sleep(0.1)

        self.control_click(42, 531) # Brittany
        time.sleep(0.1)
        self.control_click(42, 531)
        time.sleep(0.1)

        # Click the down arrow 8 times
        for i in range(0, 8):
            self.click(544, 625)
            time.sleep(0.2)
        
        self.control_click(42, 215) # Wandering
        time.sleep(0.1)
        self.control_click(42, 215)
        time.sleep(0.1)

        self.control_click(42, 316) # Betty Clicker
        time.sleep(0.1)
        self.control_click(42, 316)
        time.sleep(0.1)

        self.control_click(42, 415) # Samurai
        time.sleep(0.1)
        self.control_click(42, 415)
        time.sleep(0.1)

        self.control_click(42, 531) # Leon
        time.sleep(0.1)
        self.control_click(42, 531)
        time.sleep(0.1)

        for i in range(0, 7):
            self.click(544, 625)
            time.sleep(0.2)

        self.control_click(42, 215) # Forrest Seer
        time.sleep(0.1)
        self.control_click(42, 215)
        time.sleep(0.1)

        self.control_click(42, 316) # Alexa
        time.sleep(0.1)
        self.control_click(42, 316)
        time.sleep(0.1)

        self.control_click(42, 415) # Natalia
        time.sleep(0.1)
        self.control_click(42, 415)
        time.sleep(0.1)

        self.control_click(42, 531) # Mercedes
        time.sleep(0.1)
        self.control_click(42, 531)
        time.sleep(0.1)

        for i in range(0, 8):
            self.click(544, 625)
            time.sleep(0.2)

        self.control_click(42, 215) # Bobby
        time.sleep(0.1)
        self.control_click(42, 215)
        time.sleep(0.1)

        self.control_click(42, 316) # Broyle
        time.sleep(0.1)
        self.control_click(42, 316)
        time.sleep(0.1)

        self.control_click(42, 415) # Sir George
        time.sleep(0.1)
        self.control_click(42, 415)
        time.sleep(0.1)

        self.control_click(42, 531) # King Midas
        time.sleep(0.1)
        self.control_click(42, 531)
        time.sleep(0.1)

        for i in range(0, 7):
            self.click(544, 625)
            time.sleep(0.2)

        self.control_click(42, 215) # Referi
        time.sleep(0.1)
        self.control_click(42, 215)
        time.sleep(0.1)

        self.control_click(42, 316) # Abaddon
        time.sleep(0.1)
        self.control_click(42, 316)
        time.sleep(0.1)

        self.control_click(42, 415) # Ma Zhu
        time.sleep(0.1)
        self.control_click(42, 415)
        time.sleep(0.1)

        self.control_click(42, 531) # Amenhotep
        time.sleep(0.1)
        self.control_click(42, 531)
        time.sleep(0.1)

        for i in range(0, 7):
            self.click(544, 625)
            time.sleep(0.2)

        self.control_click(42, 215) # Beastlord
        time.sleep(0.1)
        self.control_click(42, 215)
        time.sleep(0.1)

        self.control_click(42, 316) # Athena
        time.sleep(0.1)
        self.control_click(42, 316)
        time.sleep(0.1)

        self.control_click(42, 415) # Aphrodite
        time.sleep(0.1)
        self.control_click(42, 415)
        time.sleep(0.1)

        self.control_click(42, 531) # Shinatobe
        time.sleep(0.1)
        self.control_click(42, 531)
        time.sleep(0.1)

        self.buy_available_upgrades()

    def level_click_and_activate(self):
        print str(datetime.now()) + ': Clicking on things!'
        self.update_window()

        if datetime.now() > self.time_for_screenshot:
            print '  - Copying the screenshot over.'
            dst = os.path.join(
                os.getcwd(), 
                'saved_screenshots', 
                'benchmark_' + datetime.now().strftime('%Y-%m-%d_%H.%M.%S') + '.png'
            )

            shutil.copy(WINDOW_IMAGE_LOCATION, dst)
            self.time_for_screenshot = self.time_for_screenshot + timedelta(minutes = 30)

        # Close dialogs in case we screwed up
        self.click(898, 107)
        time.sleep(0.1)
        self.click(1085, 23)
        time.sleep(0.1)

        # Make sure we're on the hire tab
        self.click(40, 99)
        time.sleep(0.1)

        # Close relic ooze dialog
        self.click(900, 103)
        time.sleep(0.1)

        self.click_on_candy_cane()
        self.hire_new_recruit_and_level()
        self.apply_level_ups()
        self.activate_abilities()
        
        if self.iteration_counter == 0:
            print '  - Invoking the dark ritual'
            self.invoke_the_dark_ritual()

        if self.iteration_counter % 5 == 0:
            print '  - Clicking on farm/progression mode'
            self.click_farm_mode()

        print "  - Clicking a bunch"
        for i in range(0, 2000):
            self.click_the_evil_monster()
        print "  - Done clicking a bunch"

        print '--------- Done for Now ---------'

        self.iteration_counter += 1
        if self.iteration_counter >= 24:
            self.iteration_counter = 0

        # Check for a candy cane more often!
        time.sleep(74.5)

        self.update_window()
        # Close dialogs in case we screwed up
        self.click(898, 107)
        time.sleep(0.1)
        self.click(1085, 23)
        time.sleep(0.1)
        # Close relic ooze dialog
        self.click(900, 103)
        time.sleep(0.1)
        self.click_on_candy_cane()

    def ascend(self):
        # Salvage relics
        self.click(362, 102)
        time.sleep(0.1)
        self.click(274, 441)

        # confirmation button
        self.click(488, 404)
        time.sleep(0.1)

        # Hero Tab
        self.click(40, 104)

        # Ascend
        self.click(1112, 294) # Ascend ability
        self.click(493, 476) # Yes button


def screenGrab():
    box = (1936,46,2833,529)
    im = ImageGrab.grab()
    filename = os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png'
    im.save(filename, 'PNG')

    large_image = cv2.imread(filename)
    small_image = cv2.imread(os.getcwd() + '\\templates\\top-left.png')

    method = cv.CV_TM_SQDIFF_NORMED

    result = cv2.matchTemplate(large_image, small_image, method)

    print cv2.minMaxLoc(result)
 
def main():
    bot = CHBot()

    ascended = False

    # bot.start_the_ascension() # TEMP

    while True:
        if len(sys.argv) > 1:
            if sys.argv[1] == "from_the_beginning" or ascended:
                bot.start_the_ascension()
                bot.click_farm_mode()

        time_to_ascend = datetime.now() + timedelta(hours = 3, minutes = 30)
        while datetime.now() < time_to_ascend:
            bot.level_click_and_activate()
            time.sleep(74.5)

            print 'Clickfest starting in 5 ...'
            time.sleep(1)
            print '                      4 ...'
            time.sleep(1)
            print '                      3 ...'
            time.sleep(1)
            print '                      2 ...'
            time.sleep(1)
            print '                      1 ...'
            time.sleep(1)

        ascended = True
        #bot.ascend()
 
if __name__ == '__main__':
    main()

    #bot = CHBot()
    #bot.update_window()
    #bot.begin_a_new_world()

    #bot = CHBot()
    #bot.update_window()