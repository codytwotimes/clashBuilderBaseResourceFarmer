import pyautogui
import time

numRaids = 30

start_swipe_for_elixir_x = -804
start_swipe_for_elixir_y = 136
end_swipe_for_elixir_x = -804
end_swipe_for_elixir_y = 445

elixir_icon_x = -573
elixir_icon_y = 145

elixir_collect_x = -471
elixir_collect_y = 945

battle_start_x = -1793
battle_start_y = 924

troops_x = -1505
troops_y = 971

battle_machine_x = -1700
battle_machine_y = 965

emulator_clear_tabs_x = -576
emulator_clear_tabs_y = 93

clash_icon_x = -836
clash_icon_y = 355

for raidNumber, _ in enumerate(range(numRaids)):
    print("Starting Raid", raidNumber)
    #in builder base:
    if raidNumber % 5 == 0:
        #collect elixir
        #swipe down to get up to icon
        pyautogui.moveTo(start_swipe_for_elixir_x,
            start_swipe_for_elixir_y, 2)
        pyautogui.mouseDown()
        pyautogui.moveTo(end_swipe_for_elixir_x,
            end_swipe_for_elixir_y, 2)
        pyautogui.mouseUp()

        #tap elixir icon
        pyautogui.moveTo(elixir_icon_x, elixir_icon_y, 2)
        pyautogui.click()

        #collect elixir
        pyautogui.moveTo(elixir_collect_x, elixir_collect_y, 2)
        pyautogui.click()

        pyautogui.moveTo(-251, 67)
        pyautogui.click()

    # start battle:
    pyautogui.moveTo(battle_start_x, battle_start_y, 2)
    pyautogui.click()

    pyautogui.moveTo(-500, 708, 2)
    pyautogui.click()

    time.sleep(20)

    #in battle:
    #DEPLOY TROOPS
    pyautogui.moveTo(troops_x, troops_y, 2)
    pyautogui.click()

    pyautogui.keyDown('b')
    pyautogui.keyDown('c')
    time.sleep(4)
    pyautogui.keyUp('b')
    pyautogui.keyUp('c')

    #DEPLOY BATTLE MACHINE
    pyautogui.moveTo(battle_machine_x, battle_machine_y, 2)
    pyautogui.click()
    pyautogui.keyDown('b')
    pyautogui.keyDown('c')
    time.sleep(1)
    pyautogui.keyUp('b')
    pyautogui.keyUp('c')
    pyautogui.moveTo(battle_machine_x, battle_machine_y, 2)
    pyautogui.click()

    time.sleep(5)
    
    #open tabs menu
    pyautogui.hotkey('ctrl','shift','5')
    time.sleep(2)

    #clear tabs button
    pyautogui.moveTo(emulator_clear_tabs_x, emulator_clear_tabs_y, 2)
    pyautogui.click()
    time.sleep(2)

    pyautogui.moveTo(clash_icon_x, clash_icon_y, 2)
    pyautogui.click()

    time.sleep(10)

pyautogui.moveTo(clash_icon_x, clash_icon_y, 2)
pyautogui.click()
