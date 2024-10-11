# Water Reminder Application

## Overview

The Water Reminder application is a desktop application built using Python's Tkinter library, designed to help users manage their water intake effectively. The application allows users to set a timer for reminders to drink water, ensuring they stay hydrated throughout the day. It also features user authentication for a personalized experience.

## Features

- **User Authentication**: Secure login and sign-up functionality for users to keep track of their hydration.
- **Customizable Timer**: Users can set the timer in hours, minutes, and seconds to receive reminders.
- **Real-time Countdown**: The application displays a countdown timer showing the time remaining until the next reminder.
- **Sound Alerts**: The application plays an alert sound when it’s time to drink water.
- **Multi-threading**: Handles countdowns without freezing the user interface, allowing smooth interaction with the app.

## Technologies Used

- **Programming Language**: Python
- **GUI Framework**: Tkinter
- **Database**: MySQL for user authentication
- **Audio**: Pygame for sound alerts

## Installation

### Prerequisites

Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

Before running the application, you need to install the following Python packages:

```bash
pip install mysql-connector-python
pip install pygame
```
### Setting Up MySQL Database

1.  Create a database named `mydb`.
    
2.  Create a table named `users` with the following structure:
```sql
CREATE TABLE users (
        email VARCHAR(255) NOT NULL PRIMARY KEY,
        password VARCHAR(255) NOT NULL
    );
```