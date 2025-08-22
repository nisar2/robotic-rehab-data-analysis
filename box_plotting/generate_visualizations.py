import os
from natsort import natsorted
import pandas as pd
from matplotlib import pyplot as plt
import math
import numpy as np
from pprint import pprint

data_path = './data'

subject_folders = natsorted(os.listdir(data_path))
subject_folders = [folder for folder in subject_folders if folder != '.DS_Store']

'''
{
    "Patient ID": {
        "assistance": {
            "shape": {
                "robot_data": {
                    "x": [],
                    "y": [],
                },
                "targets_data": {
                    "x": [],
                    "y": [],
                }
            },
            ...
            "shape": {
                "robot_data": {
                    "x": [],
                    "y": [],
                },
                "targets_data": {
                    "x": [],
                    "y": [],
                }
            }
        },
    }
}
'''

for_plotting = {}
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
        # multiply Y by 100
        targets_data['X'] = targets_data['X'] * -100
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

        # center the target data around (0,0)
        # scale=.25
        # target_data_x_interpolated = [(x)*scale for x in target_data_x_interpolated] 
        # target_data_y_interpolated = [(y)*scale for y in target_data_y_interpolated]
        # # center the robot data around (0,0)
        # robot_data['X'] = (robot_data['X'] )*scale
        # robot_data['Y'] = (robot_data['Y'] )*scale
     
        # if shape =='B':
        #     # shift the x and y coordinates of the robot data
        #     robot_data['X'] = robot_data['X'] + 2.5
        #     target_data_x_interpolated = [x + 2.5 for x in target_data_x_interpolated]

        if shape =='Infinity':
            x_shift = 0.0
            y_shift = 0.0
            # shift the x and y coordinates of the robot data
            robot_data['X'] = robot_data['X'] + x_shift
            robot_data['Y'] = robot_data['Y'] + y_shift
            target_data_x_interpolated = [x + x_shift for x in target_data_x_interpolated]
            target_data_y_interpolated = [y + y_shift for y in target_data_y_interpolated]

            # scale the x coordinate of robot_data and target_data by 0.5
            scale = 0.15
            robot_data['X'] = robot_data['X'] * scale
            robot_data['Y'] = robot_data['Y'] * scale
            target_data_x_interpolated = [x * scale for x in target_data_x_interpolated]
            target_data_y_interpolated = [y * scale for y in target_data_y_interpolated]

            

        if shape =='Circle':
            x_shift = .75
            y_shift = -0.5
            # shift the x and y coordinates of the robot data
            robot_data['X'] = robot_data['X'] + x_shift
            robot_data['Y'] = robot_data['Y'] + y_shift
            target_data_x_interpolated = [x + x_shift for x in target_data_x_interpolated]
            target_data_y_interpolated = [y + y_shift for y in target_data_y_interpolated]

            # scale the x coordinate of robot_data and target_data by 0.5
            scale = 0.25
            robot_data['X'] = robot_data['X'] * scale
            robot_data['Y'] = robot_data['Y'] * scale
            target_data_x_interpolated = [x * scale for x in target_data_x_interpolated]
            target_data_y_interpolated = [y * scale for y in target_data_y_interpolated]

        if shape =='Square':
            x_shift = 0
            y_shift = 0.0
            # shift the x and y coordinates of the robot data
            robot_data['X'] = robot_data['X'] + x_shift
            robot_data['Y'] = robot_data['Y'] + y_shift
            target_data_x_interpolated = [x + x_shift for x in target_data_x_interpolated]
            target_data_y_interpolated = [y + y_shift for y in target_data_y_interpolated]

            # scale the x coordinate of robot_data and target_data by 0.5
            scale = 0.2
            robot_data['X'] = robot_data['X'] * scale
            robot_data['Y'] = robot_data['Y'] * scale
            target_data_x_interpolated = [x * scale for x in target_data_x_interpolated]
            target_data_y_interpolated = [y * scale for y in target_data_y_interpolated]

        if shape =='B':
            x_shift = 2.5
            y_shift = 0.5
            # shift the x and y coordinates of the robot data
            robot_data['X'] = robot_data['X'] + x_shift
            robot_data['Y'] = robot_data['Y'] + y_shift
            target_data_x_interpolated = [x + x_shift for x in target_data_x_interpolated]
            target_data_y_interpolated = [y + y_shift for y in target_data_y_interpolated]

            # scale the x coordinate of robot_data and target_data by 0.5
            scale = 0.25
            robot_data['X'] = robot_data['X'] * scale
            robot_data['Y'] = robot_data['Y'] * scale
            target_data_x_interpolated = [x * scale for x in target_data_x_interpolated]
            target_data_y_interpolated = [y * scale for y in target_data_y_interpolated]

            

        if shape =='Triangle':
            x_shift = 0.0
            y_shift = 0.0
            # shift the x and y coordinates of the robot data
            robot_data['X'] = robot_data['X'] + x_shift
            robot_data['Y'] = robot_data['Y'] + y_shift
            target_data_x_interpolated = [x + x_shift for x in target_data_x_interpolated]
            target_data_y_interpolated = [y + y_shift for y in target_data_y_interpolated]
            # scale the x coordinate of robot_data and target_data by 0.5
            scale = 0.225
            robot_data['X'] = robot_data['X'] * scale
            robot_data['Y'] = robot_data['Y'] * scale
            target_data_x_interpolated = [x * scale for x in target_data_x_interpolated]
            target_data_y_interpolated = [y * scale for y in target_data_y_interpolated]

        if shape =='Hexagon':
            x_shift = 1.25
            y_shift = -0.5
            # shift the x and y coordinates of the robot data
            robot_data['X'] = robot_data['X'] + x_shift
            robot_data['Y'] = robot_data['Y'] + y_shift
            target_data_x_interpolated = [x + x_shift for x in target_data_x_interpolated]
            target_data_y_interpolated = [y + y_shift for y in target_data_y_interpolated]

            # scale the x coordinate of robot_data and target_data by 0.5
            scale = 0.2
            robot_data['X'] = robot_data['X'] * scale
            robot_data['Y'] = robot_data['Y'] * scale
            target_data_x_interpolated = [x * scale for x in target_data_x_interpolated]
            target_data_y_interpolated = [y * scale for y in target_data_y_interpolated]

        # if shape =='Hexagon':
        #     # scale the x coordinate of robot_data and target_data by 0.5
        #     scale = 0.8
        #     robot_data['X'] = robot_data['X'] * scale
        #     robot_data['Y'] = robot_data['Y'] * scale
        #     target_data_x_interpolated = [x * scale for x in target_data_x_interpolated]
        #     target_data_y_interpolated = [y * scale for y in target_data_y_interpolated]

        # if shape =='Triangle':
        #     # scale the x coordinate of robot_data and target_data by 0.5
        #     scale = 0.8
        #     robot_data['X'] = robot_data['X'] * scale
        #     robot_data['Y'] = robot_data['Y'] * scale
        #     target_data_x_interpolated = [x * scale for x in target_data_x_interpolated]
        #     target_data_y_interpolated = [y * scale for y in target_data_y_interpolated]

        # build the for_plotting dictionary
        if subject not in for_plotting.keys():
            for_plotting[subject] = {}
        if assistance not in for_plotting[subject].keys():  
            for_plotting[subject][assistance] = {}
        if shape not in for_plotting[subject][assistance].keys():   
            for_plotting[subject][assistance][shape] = {
            'robot_data': {'x': [], 'y': []},
            'targets_data': {'x': [], 'y': []}
            }
        # Append data to avoid overwriting
        for_plotting[subject][assistance][shape]['robot_data']['x'].extend(robot_data['X'].tolist())
        for_plotting[subject][assistance][shape]['robot_data']['y'].extend(robot_data['Y'].tolist())
        for_plotting[subject][assistance][shape]['targets_data']['x'].extend(target_data_x_interpolated)
        for_plotting[subject][assistance][shape]['targets_data']['y'].extend(target_data_y_interpolated)


# save the json
import json
with open('for_plotting.json', 'w') as f:
    json.dump(for_plotting, f, indent=4)

shape_order = ['Hexagon', 'Triangle', 'Circle', 'Infinity', 'B']
# Plot the data
for subject in for_plotting.keys():
    for assistance in for_plotting[subject].keys():
        shapes = for_plotting[subject][assistance].keys()
        fig, axes = plt.subplots(1, len(shapes), 
                     figsize=(5 * len(shapes), 5))
        
        if len(shapes) == 1:
            axes = [axes]  # Ensure axes is iterable when there's only one subplot

        shapes = [shape for shape in shape_order if shape in shapes]
        for idx, shape in enumerate(shapes):
            robot_data = for_plotting[subject][assistance][shape]['robot_data']
            targets_data = for_plotting[subject][assistance][shape]['targets_data']
            
            ax = axes[idx]
            ax.plot(robot_data['x'], robot_data['y'], label='Robot Data', alpha=0.75)
            ax.plot(targets_data['x'], targets_data['y'], label='Targets Data', linewidth=3)
            # make the axis equal
            # make the x axis limits -10 to 10

            ax.set_xlim(-1.5, 1.5)
            ax.set_ylim(-1.5, 1.5)
            ax.set_aspect('equal', adjustable='box')
            # ax.legend()
        
            ax.legend(loc='upper left')
        
        # add figure title
        # fig.suptitle(f'Subject: {subject}, Assistance: {assistance}', fontsize=16)
        # fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=2, fontsize=12)
        plt.tight_layout()
        plt.savefig(f'./visualizations/{subject}_{assistance}.png')
        plt.close(fig)
