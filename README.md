---

# EatEasy: Intelligent Dining Solution

## Overview

EatEasy is an intelligent dining solution designed to address the challenge of finding less crowded food counters and empty tables in the college mess during peak hours. The web application provides real-time data on crowd density at food counters and seating availability, empowering students to make informed decisions and save time. The minimalistic user interface enhances the user experience, ensuring easy and efficient interaction.

## Features

- **Real-time Data:** Utilizes CCTV cameras to collect data on crowd density, table occupancy, and counter density.
  
- **Object Detection:** Implements YOLO v4 as the main object detection model to calculate crowd density and provide suggestions to users.

- **User Ratings:** Allows users to rate the food in the mess, providing valuable feedback for catering staff.

- **Web Application:** Frontend built with HTML, CSS, and JavaScript, backed by Flask and Python. SQLite serves as the primary database for login and review data.

## Introduction

In a school or college cafeteria, finding a vacant food counter or seating area during busy times can be challenging and time-consuming. EatEasy aims to revolutionize the dining experience for college students by offering real-time information on open seats and counters, resulting in time savings and improved convenience.

### Problem Statement

- Locating less congested food counters or seating areas during peak times is inconvenient for students.
- Difficulty for catering staff in obtaining timely feedback on the quality of food in the mess.

## Proposed System

The web application's goal is to simplify the process of locating the least crowded seating and counter places in the campus mess during peak times. Built using HTML, CSS, JavaScript, and Flask, the frontend provides a seamless experience. CCTV cameras capture real-time data, and YOLO v4 calculates crowd density, offering suggestions to users. The application includes a rating feature for users to provide feedback on the food.

## System Analysis and Design

### Overall Description

The project combines HTML, CSS, JavaScript, and Flask to create a web application. CCTV data is processed in real-time, and YOLO v4 calculates crowd density. The frontend features a user-friendly interface with login, registration, and interactive functionalities.


## User Interface

### UI Description

The web application's frontend is built with standard markup languages (HTML, CSS) and enhanced with JavaScript for added functionality. Users are greeted with a login page, followed by a home page featuring a navigation bar and key buttons for finding least crowded areas and viewing the mess map.

#### Home Page

- Welcome message
- Navigation bar with project logo and utilities (logout, help, feedback)
- Buttons for finding and viewing map

#### Find Page

- Find Counter: Displays the least crowded food counter.
- Find Table: Displays the least crowded seating area, table, and density table for user decision-making.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/theNewtonCode/EatEasy-smart-mess.git
    cd EatEasy
    ```
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ``
3. Run the Flask application:

    ```bash
    flask run
    ```

4. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

## Contribution

Contribute to EatEasy by forking the repository, creating a new branch, and submitting pull requests. Your contributions are valuable in enhancing the dining experience for college students.

## License

EatEasy is licensed under the MIT License. Feel free to use, modify, and share this project.

---
