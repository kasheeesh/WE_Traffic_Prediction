# Import necessary modules
import streamlit as st
import random
# Import necessary functions from web_functions
#from images.web_functions import predict




def holiday_to_number(status):
    """Converts holiday status to number"""
    # Define a dictionary to map day names to numbers
    H_status = {"No": 0, "Yes": 1}
    # Check if the input day name is in the dictionary
    if status in H_status:
        return H_status[status]
    else:
        return None


def day_name_to_number(day_name):
    """Converts day name to number"""
    # Define a dictionary to map day names to numbers
    days = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }
    # Check if the input day name is in the dictionary
    if day_name in days:
        return days[day_name]
    else:
        return None
