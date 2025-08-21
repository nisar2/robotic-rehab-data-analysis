import os
from natsort import natsorted
import pandas as pd
from matplotlib import pyplot as plt
import math
import numpy as np

data_path = './data'

subject_folders = natsorted(os.listdir(data_path))
subject_folders = [folder for folder in subject_folders if folder != '.DS_Store']

results = []
for subject in subject_folders:
    shape_assistance_folders = natsorted(os.listdir(os.path.join(data_path, subject)))
    # remove .DS_Store from list
    shape_assistance_folders = [folder for folder in shape_assistance_folders if folder != '.DS_Store']
    shape_assistance_folders = [folder for folder in shape_assistance_folders if folder != 'Subject characteristics.docx']

    diagnosis = subject.split(' ')[0]
    subj_id = subject.split(' ')[1]

    for shape_assistance in shape_assistance_folders:
        shape = shape_assistance.split(' - ')[0]
        assistance = shape_assistance.split(' - ')[1]
        print(f'PROCESSING: Subject: {subject}, Shape: {shape}, Assistance: {assistance}')
        if assistance == 'WITH assistance':
            assistance = True
        else:
            assistance = False

        # Get the list of files in the shape assistance folder
        session_file = os.listdir(os.path.join(data_path, subject, shape_assistance))
        # Remove .DS_Store from list
        session_file = [file for file in session_file if file != '.DS_Store']
        if len(session_file) == 0:
            print(f'No session file found for {subject}, {shape_assistance}')
            continue
        session_file = session_file[0]
        
        # Get the list of files in the session folder
        session_folder = os.path.join(data_path, subject, shape_assistance, session_file)
        session_files = os.listdir(session_folder)
        # Remove .DS_Store from list
        session_files = [file for file in session_files if file != '.DS_Store']
        # only keep files that start with 'targets' or 'robot'
        session_files = [file for file in session_files if file.startswith('targets') or file.startswith('robot')]
        # sort the files in natural order
        session_files = natsorted(session_files)
        robot_file = session_files[0]
        targets_file = session_files[1]

        # open the robot file using pandas
        robot_file_path = os.path.join(session_folder, robot_file)
        targets_file_path = os.path.join(session_folder, targets_file)
        robot_data = pd.read_csv(robot_file_path)
        targets_data = pd.read_csv(targets_file_path)

        # from robot_data keep only the columns 'Timestamp', 'Unity Stylus Position X', 'Unity Stylus Position Y', 'Unity Stylus Position Z', 'Is Assisting'
        robot_data = robot_data[['Timestamp', 'Unity Stylus Position X', 'Unity Stylus Position Y', 'Unity Stylus Position Z', 'Is Assisting']]
        # remove the last row of the robot data
        robot_data = robot_data[:-1]

        # offset the timestamp by the first timestamp
        robot_data['Timestamp'] = robot_data['Timestamp'] - robot_data['Timestamp'][0]
        # divide by 10^7
        robot_data['Timestamp'] = robot_data['Timestamp'] / 10**7
        
        # multiply Unity Stylus Position X by 100
        robot_data['Unity Stylus Position X'] = robot_data['Unity Stylus Position X'] * -100 # to invert the x axis
        # multiply Unity Stylus Position Y by 100
        robot_data['Unity Stylus Position Y'] = robot_data['Unity Stylus Position Y'] * 100
        # multiply Unity Stylus Position Z by 100
        robot_data['Unity Stylus Position Z'] = robot_data['Unity Stylus Position Z'] * 100
        # rename 'Unity Stylus Position X' to 'X', 'Unity Stylus Position Y' to 'Y', 'Unity Stylus Position Z' to 'Z'
        robot_data = robot_data.rename(columns={'Unity Stylus Position X': 'X', 'Unity Stylus Position Y': 'Y', 'Unity Stylus Position Z': 'Z'})
        
        # from targets_data keep only the columns 'Name', 'x, 'Y'
        targets_data = targets_data[['Name', 'X', 'Y']]
        # multiply X by 100
        targets_data['X'] = targets_data['X'] * -100 # to invert the x axis
        # multiply Y by 100
        targets_data['Y'] = targets_data['Y'] * 100

        # interpolate the target data to with n samples between each target
        target_data_x = targets_data['X'].values
        target_data_y = targets_data['Y'].values
        # interpolate the target data to with n samples between each target
        target_data_x_interpolated = []
        target_data_y_interpolated = []  

        d = 0.05 # distance between points
        # loop over the pairs of target data
        for i in range(len(target_data_x)):
            if i == len(target_data_x) - 1:
                x_start = target_data_x[i]
                y_start = target_data_y[i]
                x_end = target_data_x[0]
                y_end = target_data_y[0]
            else:
                x_start = target_data_x[i]
                y_start = target_data_y[i]
                x_end = target_data_x[i + 1]
                y_end = target_data_y[i + 1]
            # compute the angle between the two points
            angle = math.atan2(y_end - y_start, x_end - x_start)
            # get distance in terms of x and y
            dx = d * math.cos(angle)
            dy = d * math.sin(angle)

            while(True):
                # add the point to the list
                target_data_x_interpolated.append(x_start)
                target_data_y_interpolated.append(y_start)
                # check if we are close enough to the end point
                if abs(x_start - x_end) < d and abs(y_start - y_end) < d:
                    break
                # move to the next point
                x_start += dx
                y_start += dy

        target_coords_interpolated = np.array([target_data_x_interpolated, target_data_y_interpolated])
        target_coords_interpolated = target_coords_interpolated.T
        min_distances = []
        # loop over the rows of the robot data using iterrows
        for index, row in robot_data.iterrows():  
            x = row['X']
            y = row['Y']
            robot_coord = np.array([x, y])

            distance = np.linalg.norm(target_coords_interpolated - robot_coord, axis=1)
            # get the index of the minimum distance
            min_index = np.argmin(distance)
            # get the minimum distance
            min_distance = distance[min_index]
            # save
            min_distances.append(min_distance)
        
        min_distances = np.array(min_distances)
        mean_min_distance = np.mean(min_distances)

        to_save = {
            'subject': subject,
            'diagnosis': diagnosis,
            'id': subj_id,
            'shape': shape,
            'assistance': assistance,
            'average_distance': mean_min_distance,
            'duration': robot_data['Timestamp'].iloc[-1] - robot_data['Timestamp'].iloc[0],
        }

        # if subject == 'Patient 4' and shape == 'Hexagon' and assistance == False:
        #     print(robot_data['Timestamp'])
        #     input()
        results.append(to_save)

results = pd.DataFrame(results)
# save the results to a csv file
results.to_csv('results.csv', index=False)