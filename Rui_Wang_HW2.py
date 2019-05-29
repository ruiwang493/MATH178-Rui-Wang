from pathlib import Path
from typing import List
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import math
import os

# data pre processing
base_data_folder_path = Path('public_dataset')
file_name_to_colume_names = {
    'Accelerometer.csv': ['Systime', 'EventTime', 'ActivityID', 'X', 'Y', 'Z', 'Phone_orientation'],
    'Activity.csv': ['ID', 'SubjectID', 'Start_time', 'End_time', 'Relative_Start_time', 'Relative_End_time',
                     'Gesture_scenario', 'TaskID', 'ContentID'],
    'Gyroscope.csv': ['Systime', 'EventTime', 'ActivityID', 'X', 'Y', 'Z', 'Phone_orientation'],
}


def get_user_ids() -> List[str]:
    x = []
    directory = os.fsencode("./")
    for file in os.listdir(directory)
        filename = os.fsdecode(file)
        x.append(filename)
    return x


def get_user_session_ids(user_id: str) -> List[str]:
    x = []
    directory = os.fsencode("./"+user_id)
    for file in os.listdir(directory)
        filename = os.fsdecode(file)
        x.append(open(filename,'r').read())
    return x

def read_file(user_id: str, user_session_id: str, file_name: str, colume_names: List[str]) -> DataFrame:
    f = open("/public_dataset/"+user_id+"_session_"+user_session_id+"/"+file_name, 'r')
    s = f.readlines()
    for line in s :
        a = s.split(',')
    newFrame = pd.DataFrame(np.array(a), columns = colume_names)
    newFrame
    return newFrame

def get_user_session_data(user_id: str, user_session_id: str) -> DataFrame:
    df1 = read_file(user_id, user_session_id, "Accelerometer.csv", ['Systime', 'EventTime', 'ActivityID', 'X', 'Y', 'Z', 'Phone_orientation'])
    df2 = read_file(user_id, user_session_id, "Gyroscope.csv", ['Systime', 'EventTime', 'ActivityID', 'X', 'Y', 'Z', 'Phone_orientation'])
    df3 = read_file(user_id, user_session_id, "Activity.csv", ['ID', 'SubjectID', 'Start_time', 'End_time', 'Relative_Start_time', 'Relative_End_time', 'Gesture_scenario', 'TaskID', 'ContentID'])
    newFrame = pd.concat([df3, df1, df2])
    return newFrame

user_id = 248252
# pick the user as well as activities and extract 3 out of 6 features 
pass
# visualize of the features you pick
pass

def multiV_curvature(nbddata: DataFrame) -> float:  
    x = nbddata.loc[:, "x(t)"]
    y = nbddata.loc[:, "y(t)"]
    z = nbddata.loc[:, "z(t)"]
    """
     * I do not understand how to code this I am sorry
    """
    """
    Calculate multi V curvature
    :param nbddata: neighborhood of time t_i containing (t, x(t), y(t), z(t)), 
    where x(t), y(t), z(t) are the 3 out of the 6 features. 
    :return: multi V curvature
    """
    pass
def multiV_torsion(nbddata: DataFrame) -> float:  
    x = nbddata.loc[:, "x(t)"]
    y = nbddata.loc[:, "y(t)"]
    z = nbddata.loc[:, "z(t)"]
    """
     * I do not understand how to code this I am sorry
    """
    """
    Calculate multi V torsion
    :param nbddata: neighborhood of time t_i containing (t, x(t), y(t), z(t)), 
    where x(t), y(t), z(t) are the 3 out of the 6 features. 
    :return: multi V torsion
    """
    pass

# Calucate and plot curvature and torsion of the features you pick
pass

