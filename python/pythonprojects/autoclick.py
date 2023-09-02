
# import pyautogui
# import time
# def get_coordinates():
#     print("Move your mouse cursor over the desired point...")
#     try:
#         while True:
#             time.sleep(10)
#             x, y = pyautogui.position()
#             position_str = f"X: {x}, Y: {y}"
#             print(position_str, end="\n")
#     except KeyboardInterrupt:
#         print("\nCoordinates captured!")

# if __name__ == "__main__":
#     get_coordinates()

# =======================================================================

# import pyautogui
# import time

# def click_and_wait(x, y, delay=0.5):
#     pyautogui.click(x, y)
#     time.sleep(delay)

# def main():
#     try:
#         for slide_number in range(138, 207):
#             # Step 1: Go to the first coordinate and click
#             click_and_wait(1817, 897)
            
#             # Step 2: Go to the second coordinate and click
#             click_and_wait(388, 211)
            
#             # Step 3: Replace the slide number and press Enter
#             pyautogui.hotkey("ctrl", "a")
#             pyautogui.write(f"Slide{slide_number}")
#             pyautogui.press("enter")
            
#             # Step 4: Wait for 3 seconds
#             time.sleep(3)
            
#             # Step 5: Go to the third coordinate and click
#             click_and_wait(375, 385)
            
#             # Repeat for the next slide
#     except KeyboardInterrupt:
#         print("\nAutomation stopped.")

# if __name__ == "__main__":
#     time.sleep(5)
#     main()