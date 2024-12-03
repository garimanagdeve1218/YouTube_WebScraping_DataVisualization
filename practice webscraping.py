# CODE TO EXTRACT DATA (NOT IN CSV) BUT IN LIST FORMAT
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
#
# url = 'https://www.youtube.com/@YudiJ/videos'
#
# # Using Selenium driver to access the page
# driver = webdriver.Chrome()
# driver.get(url)
#
# # Wait for the videos to load if necessary
# driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to appear
#
# # Find all video elements
# videos = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-grid-media')
#
# video_list = []
#
# # Loop through each video and extract the title, views, and when
# for video in videos:
#     try:
#         title = video.find_element(By.XPATH, './/*[@id="video-title"]').text  # Use .text to extract text
#         views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text  # Use .text to extract text
#         when = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text  # Use .text to extract text
#
#         # Create a dictionary for each video
#         vid_item = {
#             'title': title,
#             'views': views,
#             'posted': when
#         }
#
#         # Append the dictionary to the video list
#         video_list.append(vid_item)
#     except Exception as e:
#         print(f"Error extracting data from a video: {e}")
#
# # Optional: Convert video_list to a DataFrame for better display
# df = pd.DataFrame(video_list)
#
# # Close the browser
# driver.quit()
#
# # Display the video data
# print(df)

# --------------------------------------------------------
# CODE TO EXTRACT DATA IN LIST TO DATA IN CSV

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
#
# url = 'https://www.youtube.com/@YudiJ/videos'
#
# # Using Selenium driver to access the page
# driver = webdriver.Chrome()
# driver.get(url)
#
# # Wait for the videos to load if necessary
# driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to appear
#
# # Find all video elements
# videos = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-grid-media')
#
# video_list = []
#
# # Loop through each video and extract the title, views, and when
# for video in videos:
#     try:
#         title = video.find_element(By.XPATH, './/*[@id="video-title"]').text  # Use .text to extract text
#         views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text  # Use .text to extract text
#         when = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text  # Use .text to extract text
#
#         # Create a dictionary for each video
#         vid_item = {
#             'title': title,
#             'views': views,
#             'posted': when
#         }
#
#         # Append the dictionary to the video list
#         video_list.append(vid_item)
#     except Exception as e:
#         print(f"Error extracting data from a video: {e}")
#
# #reverse the list
# video_list.reverse()
#
# # Convert video_list to a DataFrame
# df = pd.DataFrame(video_list)
#
# # Save the DataFrame to a CSV file
# df.to_csv('youtube_video_data.csv', index=False)  # Save as 'youtube_video_data.csv'
#
# # Close the browser
# driver.quit()
#
# # Display the video data
# print("Data saved to 'youtube_video_data.csv'")

# -------------------------------------------------------------------
# CODE TO EXTRACT THE LAST ROW OF THE CSV INTO NEW CSV AND DELETE THE PREVIOUS CSV
#
# import os
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'https://www.youtube.com/@YudiJ/videos'
#
# # Using Selenium driver to access the page
# driver = webdriver.Chrome()
# driver.get(url)
#
# # Wait for the videos to load if necessary
# driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to appear
#
# # Find all video elements
# videos = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-grid-media')
#
# video_list = []
#
# # Loop through each video and extract the title, views, and when
# for video in videos:
#     try:
#         title = video.find_element(By.XPATH, './/*[@id="video-title"]').text  # Use .text to extract text
#         views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text  # Use .text to extract text
#         when = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text  # Use .text to extract text
#
#         # Create a dictionary for each video
#         vid_item = {
#             'title': title,
#             'views': views,
#             'posted': when
#         }
#
#         # Append the dictionary to the video list
#         video_list.append(vid_item)
#     except Exception as e:
#         print(f"Error extracting data from a video: {e}")
#
# # Reverse the list to get the newest first
# video_list.reverse()
#
# # Convert video_list to a DataFrame
# df = pd.DataFrame(video_list)
#
# # Save the reversed DataFrame to a CSV file
# csv_file = 'youtube_video_data_reversed.csv'
# df.to_csv(csv_file, index=False)
#
# # Close the browser
# driver.quit()
#
# # Extract the last row from the CSV
# last_row = df.tail(1)
#
# # Delete the previous CSV file
# if os.path.exists(csv_file):
#     os.remove(csv_file)
#
# # Save the last row to a new CSV file
# new_csv_file = 'last_video_data.csv'
# last_row.to_csv(new_csv_file, index=False)
#
# print(f"Last row saved to '{new_csv_file}'")

# ---------------------------------------------------

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import tkinter as tk
# from tkinter import messagebox
# import re
#
#
# def start_scraping():
#     try:
#         # Scrape data using Selenium
#         url = 'https://www.youtube.com/@YudiJ/videos'
#
#         # Using Selenium driver to access the page
#         driver = webdriver.Chrome()
#         driver.get(url)
#
#         # Wait for the videos to load if necessary
#         driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to appear
#
#         # Find all video elements
#         videos = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-grid-media')
#
#         video_list = []
#
#         # Loop through each video and extract the title, views, and when
#         for video in videos:
#             try:
#                 title = video.find_element(By.XPATH, './/*[@id="video-title"]').text  # Use .text to extract text
#                 views = video.find_element(By.XPATH,
#                                            './/*[@id="metadata-line"]/span[1]').text  # Use .text to extract text
#                 when = video.find_element(By.XPATH,
#                                           './/*[@id="metadata-line"]/span[2]').text  # Use .text to extract text
#
#                 # Create a dictionary for each video
#                 vid_item = {
#                     'title': title,
#                     'views': views,
#                     'posted': when
#                 }
#
#                 # Append the dictionary to the video list
#                 video_list.append(vid_item)
#             except Exception as e:
#                 print(f"Error extracting data from a video: {e}")
#
#         # Reverse the list to get the newest first
#         video_list.reverse()
#
#         # Convert video_list to a DataFrame
#         df = pd.DataFrame(video_list)
#
#         # Save the reversed DataFrame to a CSV file
#         csv_file = 'youtube_video_data_reversed.csv'
#         df.to_csv(csv_file, index=False)
#
#         # Close the browser
#         driver.quit()
#
#         # Extract the last row from the CSV
#         last_row = df.tail(1)
#
#         # Delete the previous CSV file
#         if os.path.exists(csv_file):
#             os.remove(csv_file)
#
#         # Save the last row to a new CSV file
#         new_csv_file = 'last_video_data.csv'
#         last_row.to_csv(new_csv_file, index=False)
#
#         # Create the bar graph
#         create_bar_graph(df)
#
#         # Delete the last row CSV file after graph generation
#         if os.path.exists(new_csv_file):
#             os.remove(new_csv_file)
#
#         # Show success message
#         messagebox.showinfo("Success", "Process completed successfully. Last row extracted and graph generated.")
#
#     except Exception as e:
#         # Handle errors and show message
#         messagebox.showerror("Error", f"An error occurred: {e}")
#
#
# def convert_views_to_numeric(views):
#     """Converts views (e.g. '1.2M', '15k') into numeric values."""
#     try:
#         views = views.lower().replace('views', '').strip()  # Remove 'views' and extra spaces
#
#         if 'k' in views:
#             return float(views.replace('k', '').replace(',', '').strip()) * 1000
#         elif 'm' in views:
#             return float(views.replace('m', '').replace(',', '').strip()) * 1000000
#         elif 'b' in views:
#             return float(views.replace('b', '').replace(',', '').strip()) * 1000000000
#         else:
#             # If views are a plain number without 'k', 'm', or 'b', just clean and convert
#             return float(views.replace(',', '').strip())
#     except ValueError as e:
#         print(f"Error converting views: {views}. Error: {e}")
#         return 0  # Return 0 if there's an error
#
#
# def create_bar_graph(df):
#     # Prepare the views data for the bar chart
#     df['views_numeric'] = df['views'].apply(convert_views_to_numeric)
#
#     # Create a figure with a custom size to ensure the full titles are visible
#     plt.figure(figsize=(12, 8))  # Increase width and reduce height
#
#     # Create a vertical bar plot (switch x and y axes)
#     plt.barh(df['title'], df['views_numeric'], color='tab:blue')  # Use barh for horizontal bars
#
#     # Set labels and title
#     plt.xlabel('Views')
#     plt.ylabel('Video Title')
#     plt.title('YouTube Videos Views')
#
#     # Adjust layout to fit the labels and titles better
#     plt.tight_layout()
#
#     # Show the plot
#     plt.show()
#
#
# # Create the GUI window
# root = tk.Tk()
# root.title("Web Scraping and Data Visualization")
#
# # Set window size
# root.geometry("300x150")
#
# # Create a "Start" button to trigger the scraping and graph creation process
# start_button = tk.Button(root, text="Start", command=start_scraping, height=2, width=20)
# start_button.pack(pady=30)
#
# # Run the GUI loop
# root.mainloop()

# -------------------------------------
# IMPORTANT CODE: MAKING THE BAR GRAPH WITH HOVER EFFECT SHOWING VIEWS

import os
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors  # Import mplcursors for interactivity
from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import messagebox

def start_scraping():
    try:
        # Scrape data using Selenium
        url = 'https://www.youtube.com/@YudiJ/videos'

        # Using Selenium driver to access the page
        driver = webdriver.Chrome()
        driver.get(url)

        # Wait for the videos to load if necessary
        driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to appear

        # Find all video elements
        videos = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-grid-media')

        video_list = []

        # Loop through each video and extract the title, views, and when
        for video in videos:
            try:
                title = video.find_element(By.XPATH, './/*[@id="video-title"]').text  # Use .text to extract text
                views = video.find_element(By.XPATH,
                                           './/*[@id="metadata-line"]/span[1]').text  # Use .text to extract text
                when = video.find_element(By.XPATH,
                                          './/*[@id="metadata-line"]/span[2]').text  # Use .text to extract text

                # Create a dictionary for each video
                vid_item = {
                    'title': title,
                    'views': views,
                    'posted': when
                }

                # Append the dictionary to the video list
                video_list.append(vid_item)
            except Exception as e:
                print(f"Error extracting data from a video: {e}")

        # Reverse the list to get the newest first
        video_list.reverse()

        # Convert video_list to a DataFrame
        df = pd.DataFrame(video_list)

        # Save the reversed DataFrame to a CSV file
        csv_file = 'youtube_video_data_reversed.csv'
        df.to_csv(csv_file, index=False)

        # Close the browser
        driver.quit()

        # Extract the last row from the CSV
        last_row = df.tail(1)

        # Delete the previous CSV file
        if os.path.exists(csv_file):
            os.remove(csv_file)

        # Save the last row to a new CSV file
        new_csv_file = 'last_video_data.csv'
        last_row.to_csv(new_csv_file, index=False)

        # Create the bar graph
        create_bar_graph(df)

        # Delete the last row CSV file after graph generation
        if os.path.exists(new_csv_file):
            os.remove(new_csv_file)

        # Show success message
        messagebox.showinfo("Success", "Process completed successfully. Last row extracted and graph generated.")

    except Exception as e:
        # Handle errors and show message
        messagebox.showerror("Error", f"An error occurred: {e}")


def convert_views_to_numeric(views):
    """Converts views (e.g. '1.2M', '15k') into numeric values."""
    try:
        views = views.lower().replace('views', '').strip()  # Remove 'views' and extra spaces

        if 'k' in views:
            return float(views.replace('k', '').replace(',', '').strip()) * 1000
        elif 'm' in views:
            return float(views.replace('m', '').replace(',', '').strip()) * 1000000
        elif 'b' in views:
            return float(views.replace('b', '').replace(',', '').strip()) * 1000000000
        else:
            # If views are a plain number without 'k', 'm', or 'b', just clean and convert
            return float(views.replace(',', '').strip())
    except ValueError as e:
        print(f"Error converting views: {views}. Error: {e}")
        return 0  # Return 0 if there's an error


def create_bar_graph(df):
    # Prepare the views data for the bar chart
    df['views_numeric'] = df['views'].apply(convert_views_to_numeric)

    # Create a figure with a custom size to ensure the full titles are visible
    plt.figure(figsize=(12, 8))  # Increase width and reduce height

    # Create a vertical bar plot (switch x and y axes)
    bars = plt.barh(df['title'], df['views_numeric'], color='tab:blue')  # Use barh for horizontal bars

    # Set labels and title
    plt.xlabel('Views')
    plt.ylabel('Video Title')
    plt.title('YouTube Videos Views')

    # Adjust layout to fit the labels and titles better
    plt.tight_layout()

    # Use mplcursors to make the bar chart interactive and show the view count on hover
    mplcursors.cursor(bars, hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(f"{df['views'].iloc[sel.index]} views")
    )

    # Show the plot
    plt.show()


# Create the GUI window
root = tk.Tk()
root.title("Web Scraping and Data Visualization")

# Set window size
root.geometry("300x150")

# Create a "Start" button to trigger the scraping and graph creation process
start_button = tk.Button(root, text="Start", command=start_scraping, height=2, width=20)
start_button.pack(pady=30)

# Run the GUI loop
root.mainloop()
