# importing the required modules
import glob
import random
import csv
import numpy as np
  
# specifying the path to csv files
path = "resources"
  
# csv files in the path
files = glob.glob(path + "/*.csv")

def random_cl_rx():  
  with open("resources/cl_lens.csv", "r") as presription_csv_file:
    csv_reader = csv.reader(presription_csv_file, delimiter=',')
    # This skips over the header row
    next(csv_reader)
    filtered_list = list(filter(None, csv_reader))
    cl_sphere = random.choice([row[0] for row in filtered_list if row[0] != ''])
    cl_diameter = random.choice([row[1] for row in filtered_list if row[1] != ''])
    cl_axis = random.choice([row[2] for row in filtered_list if row[2] != ''])
    cl_base_curve = random.choice([row[3] for row in filtered_list if row[3] != ''])
    cl_colour = random.choice([row[4] for row in filtered_list if row[4] != ''])
    return {"cl_sphere" : cl_sphere, "cl_diameter": cl_diameter, "cl_axis":cl_axis,"cl_base_curve":cl_base_curve,"cl_colour":cl_colour}

def random_presribed_rx():
  threshold_range1 = np.arange(-6.00,+6.00,0.25) 
  threshold_range2 = np.arange(-12.00,-6.00,0.50)
  threshold_range = (threshold_range1.tolist() + threshold_range2.tolist())
  r_sph=random.choice(np.round(threshold_range, 2))
  l_sph=random.choice(np.round(threshold_range, 2))
  r_cyl=random.choice(np.round(threshold_range1, 2).tolist())
  l_cyl=random.choice(np.round(threshold_range1, 2).tolist())
  sph_right_eye = (f"{r_sph:+.2f}")
  sph_left_eye = (f"{l_sph:+.2f}")
  cyl_right_eye = (f"{r_cyl:+.2f}")
  cyl_left_eye = (f"{l_cyl:+.2f}")
  if (sph_right_eye == '+0.00'): sph_right_eye = '0.00'
  else: sph_right_eye
  if (sph_left_eye == '+0.00'): sph_left_eye = '0.00'
  else: sph_left_eye
  if (cyl_right_eye == '+0.00'): cyl_right_eye = '-'
  else: cyl_right_eye
  if (cyl_left_eye == '+0.00'): cyl_left_eye = '-'
  else: cyl_left_eye
  return {"sph_right_eye" : sph_right_eye,
          "left_right_eye" : sph_left_eye,
          "cyl_right_eye" : cyl_right_eye, 
          "cyl_left_eye" : cyl_left_eye, 
          "right_axis": random.randint(1, 180),
          "left_axis": random.randint(1, 180),
          "PD": random.randint(54, 74)}