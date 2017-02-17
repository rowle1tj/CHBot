from thebot import CHBot
import time
from datetime import datetime, timedelta

def main():
    bot = CHBot()
    
    bot.click_farm_mode()

    # Click four times per second for one minute
    for i in range(0, 240):
        bot.click_the_evil_monster()
        time.sleep(0.25)

    # Hire the first four
    bot.click(54, 227) # Cid
    time.sleep(0.1)
    bot.click(54, 338) # Treebeast
    time.sleep(0.1)
    bot.click(54, 446) # Ivan
    time.sleep(0.1)
    bot.click(54, 556) # Brittany
    time.sleep(0.1)

    # for 10 minutes, Every 10 seconds
    # Scroll to the top, scroll to the bottom, and hire
    before_time = datetime.now()
    current_time = datetime.now() - timedelta(minutes=7, seconds=45)
    while(current_time < before_time):
        bot.scroll_to_top()
        time.sleep(0.75)
        bot.scroll_to_bottom()
        time.sleep(0.75)

        # Attempt to hire a hero
        bot.click(45, 454)

        time.sleep(0.5)

        # Catch one in the backlog if need be
        bot.click(45, 346)

        time.sleep(8)
        current_time = datetime.now() - timedelta(minutes=7, seconds=45)
    
    bot.scroll_to_top()
    time.sleep(0.5)


    # Control click all the heroes twice
    bot.control_click(42, 215) # Cid
    time.sleep(0.1)
    bot.control_click(42, 215)
    time.sleep(0.1)

    bot.control_click(42, 316) # Treebeast
    time.sleep(0.1)
    bot.control_click(42, 316)
    time.sleep(0.1)

    bot.control_click(42, 415) # Ivan
    time.sleep(0.1)
    bot.control_click(42, 415)
    time.sleep(0.1)

    bot.control_click(42, 531) # Brittany
    time.sleep(0.1)
    bot.control_click(42, 531)
    time.sleep(0.1)

    # Click the down arrow 8 times
    for i in range(0, 8):
        bot.click(544, 625)
        time.sleep(0.2)
    
    bot.control_click(42, 215) # Wandering
    time.sleep(0.1)
    bot.control_click(42, 215)
    time.sleep(0.1)

    bot.control_click(42, 316) # Betty Clicker
    time.sleep(0.1)
    bot.control_click(42, 316)
    time.sleep(0.1)

    bot.control_click(42, 415) # Samurai
    time.sleep(0.1)
    bot.control_click(42, 415)
    time.sleep(0.1)

    bot.control_click(42, 531) # Leon
    time.sleep(0.1)
    bot.control_click(42, 531)
    time.sleep(0.1)

    for i in range(0, 7):
        bot.click(544, 625)
        time.sleep(0.2)

    bot.control_click(42, 215) # Forrest Seer
    time.sleep(0.1)
    bot.control_click(42, 215)
    time.sleep(0.1)

    bot.control_click(42, 316) # Alexa
    time.sleep(0.1)
    bot.control_click(42, 316)
    time.sleep(0.1)

    bot.control_click(42, 415) # Natalia
    time.sleep(0.1)
    bot.control_click(42, 415)
    time.sleep(0.1)

    bot.control_click(42, 531) # Mercedes
    time.sleep(0.1)
    bot.control_click(42, 531)
    time.sleep(0.1)

    for i in range(0, 8):
        bot.click(544, 625)
        time.sleep(0.2)

    bot.control_click(42, 215) # Bobby
    time.sleep(0.1)
    bot.control_click(42, 215)
    time.sleep(0.1)

    bot.control_click(42, 316) # Broyle
    time.sleep(0.1)
    bot.control_click(42, 316)
    time.sleep(0.1)

    bot.control_click(42, 415) # Sir George
    time.sleep(0.1)
    bot.control_click(42, 415)
    time.sleep(0.1)

    bot.control_click(42, 531) # King Midas
    time.sleep(0.1)
    bot.control_click(42, 531)
    time.sleep(0.1)

    for i in range(0, 7):
        bot.click(544, 625)
        time.sleep(0.2)

    bot.control_click(42, 215) # Referi
    time.sleep(0.1)
    bot.control_click(42, 215)
    time.sleep(0.1)

    bot.control_click(42, 316) # Abaddon
    time.sleep(0.1)
    bot.control_click(42, 316)
    time.sleep(0.1)

    bot.control_click(42, 415) # Ma Zhu
    time.sleep(0.1)
    bot.control_click(42, 415)
    time.sleep(0.1)

    bot.control_click(42, 531) # Amenhotep
    time.sleep(0.1)
    bot.control_click(42, 531)
    time.sleep(0.1)

    for i in range(0, 7):
        bot.click(544, 625)
        time.sleep(0.2)

    bot.control_click(42, 215) # Beastlord
    time.sleep(0.1)
    bot.control_click(42, 215)
    time.sleep(0.1)

    bot.control_click(42, 316) # Athena
    time.sleep(0.1)
    bot.control_click(42, 316)
    time.sleep(0.1)

    bot.control_click(42, 415) # Aphrodite
    time.sleep(0.1)
    bot.control_click(42, 415)
    time.sleep(0.1)

    bot.control_click(42, 531) # Shinatobe
    time.sleep(0.1)
    bot.control_click(42, 531)
    time.sleep(0.1)

    bot.buy_available_upgrades()



if __name__ == "__main__":
    main()