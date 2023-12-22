

# import tensorflow as tf
# import csv

# path_file = r"E:\AI_DS_ML\brain_tumor_detection\runs\classify\train\events.out.tfevents.1703146304.AIDreamer.44188.0"

# # Create a summary iterator for the file
# summary_iterator = tf.compat.v1.train.summary_iterator(path_file)

# # Open a CSV file to write the summary data
# csv_path = r'E:\AI_DS_ML\brain_tumor_detection\classify\data.csv'
# with open(csv_path, "w") as csvfile:
#     csv_writer = csv.writer(csvfile)

#     # Iterate over the summaries and write the data to the CSV file
#     for summary in summary_iterator:
#         for value in summary.summary.value:
#             csv_writer.writerow([value.tag, value.simple_value])

import tensorflow as tf
import csv

path_file = r"E:\AI_DS_ML\brain_tumor_detection\runs\classify\train\events.out.tfevents.1703146304.AIDreamer.44188.0"

# Open a CSV file to write the summary data
csv_path = r'E:\AI_DS_ML\brain_tumor_detection\classify\data.csv'
with open(csv_path, "w", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write the header to the CSV file
    csv_writer.writerow(["Tag", "Simple Value"])
    # Iterate over the summaries and write the data to the CSV file
    for summary in tf.compat.v1.train.summary_iterator(path_file):
        for value in summary.summary.value:
            csv_writer.writerow([value.tag, value.simple_value])
