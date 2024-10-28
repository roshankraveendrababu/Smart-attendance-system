
Smart Attendance System using Face Detection

The Smart Attendance System project utilizes the Haar Cascade
Frontal Face Algorithm for face detection, a highly efficient machine
learning-based approach used to detect human faces in real-time. This
system works by capturing images of individuals' faces and creating a
dataset that trains the model to recognize each person’s unique facial
features. Once the dataset is created, it is stored for future reference
and used for tracking attendance. When a live video feed is provided to
the system, it scans the faces of individuals and cross-checks them
against the dataset to identify the person. Upon successful
identification, the system logs the name, along with the exact time and
date, and records this data into an Excel file.


## Tech Stack
1) Numpy - could be a library for Python, adding support for multi-dimensional arrays and matrices, in conjunction with an enormous assortment of high-level mathematical functions to operate on these arrays.
2) Pandas - is a fast, powerful, flexible, and easy to use open-source data analysis and manipulation tool, built on top of the Python programming language.
3) Haar Cascade - is a machine learning object detection algorithm used to identify objects in an image or video and based on the concept of features proposed by Paul Viola and Michael Jones in their paper "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001.
4) Datetime - It’s a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, and info.
5) Face_Recognition - Recognize and manipulate faces from Python or the command line with the world’s simplest face recognition library.
6) OpenCV - a library of programming functions primarily geared toward real-time computer vision.


## Authors

- [@K.R.ROSHAN](https://github.com/roshankraveendrababu)


## Acknowledgements

 - [Smart Attendance System using Face Detection with Open CV](https://github.com/shumbul/Smart-Attendance-System)
 - [Efficient attendance management:a face recognition approach](https://ieeexplore.ieee.org/document/10428141)
 


## Appendix

This project on the Smart Attendance System is designed to automate and streamline attendance tracking using advanced technologies. The system utilizes facial recognition to secure and contactless attendance verification. Built using Python and integrated with a database (e.g.,SQL), it stores and manages attendance records in real-time. Deployment options include local servers or cloud platforms for scalability.


## Documentation

[Documentation](https://drive.google.com/file/d/1Eg068Wo2Ff-9TcO8PKDAYA5HfJokmYPw/view?usp=drive_link)


## FAQ

1) What was the Algorithm used for this project?

Haar Cascade Frontal Face Algorithm

2) What is the accuracy of the model?

96%


## 🚀 About Me
I'm a An soon-to-be data scientist upskilling myself day by day.
nice to have you here and hope you have an great time here.


# Hi, I'm Roshan! 👋


## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/roshankr09/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/roshankr0912)


## Installation

Clone the repository and navigate to the project folder

```bash
  git clone https://github.com/roshankraveendrababu/Smart-attendance-system.git
  cd smart-attendance-system

```

Install dependencies
```bash
  pip install -r requirements.txt

```

Run dataset creation
```bash
  python dataset-creation.py

```

Train the model
```bash
  python model-train.py

```

Start attendance logging
```bash
  python recognize_attendance.py

``` 











    
## Contributing

Any modification/additional feature in this project would be appreciated.
Send a PR along with output screenshot, to get the new changes merged.

