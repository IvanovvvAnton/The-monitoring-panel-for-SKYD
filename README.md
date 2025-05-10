# The-monitoring-panel-for-SKYD

## 📍 Appointment

To monitor events related to the entrance or exit of users from the building, a web interface has been developed integrated with an access control and management system (ACS) using RFID identification and biometric authentication through facial recognition. This interface provides authorized employees with the ability to monitor user actions in real time, which is critical for ensuring security and access control in the organization's premises.

The system operation process is as follows:

### 🔍 The authentication process:

1 The user approaches the access point, where his RFID card is read using the RC522 RFID module connected to the Arduino.

2 If the RFID card is successfully read, the system starts additional biometric verification. The camera is used to recognize the employee's face using biometric authentication algorithms.

3 If both stages of verification are successful, the system records the user's full name, the date and time of entry or exit, as well as the type of event (entry or exit).

#### ☁️ Sending data to the server:

1 All data collected by the system (full name, event type, date and time) is sent to the server in real time using a method implemented in Python (for example, via Flask).

#### 💻 Processing and display on the dashboard:

1 The server receives this data and transmits it to the web-based monitoring interface, which is automatically updated to display up-to-date data about users in the building.

2 The dashboard shows a list of employees who have successfully authenticated and are in the building. The system also displays the type of event (input or output) and the time when the event occurred.

3 For each entry, the user's full name, event type, and timestamp are displayed. Employees who have left the building are displayed as "not in the building", and information about them disappears from the panel as soon as they pass the exit check.

#### 🚶‍♂️ Operational tracking of movements:

1 Authorized employees or security systems can monitor in real time who is in the building and who has left it, which allows them to quickly respond to changes.

2 The dashboard can also include filtering, sorting, and searching functions by full name, entry/exit time, and event type. This simplifies data analysis, especially in the case of security checks or event analysis.

#### 📍 Thus, this system not only automates the access control process, but also significantly increases the level of security, allowing you to quickly track the movements of employees in the building, which is especially important for organizations where strict security measures must be observed or a large number of visitors must be managed.

## 📊 Event displays

The dashboard displays events with data about the user's full name, time of the event, and type (entrance/exit), which allows you to effectively monitor the current situation in the building. All events are displayed in real time, updating automatically so that employees can immediately see information about who entered or left the building, as well as when it happened. Each event is accompanied by the following data:

- User's full name: The full name of the authenticated employee or visitor.

- Date and time of the event: The exact time when the entrance or exit occurred, which allows you to accurately record the time intervals when users were in the building.

- Event type: An indication of whether this event was the entrance to the building (entrance) or exit from it (exit), which helps to distinguish between these two types of actions and allows for accurate monitoring.

To increase the convenience of displaying information, it is structured and easily perceived. The following elements are provided in the interface:

- Sorting and Filtering: Employees can sort events by time, event type, or user's full name. This allows you to quickly find information about a specific employee or timestamp.

- Automatic update: The dashboard is updated in real time, which allows you to always be aware of the current situation. New events are added to the table or list, and old events can be hidden when they are no longer relevant.

- Event History: All events are saved and can be viewed in a historical context. This is especially useful for subsequent analysis, reporting, or in the case of incident investigations.

- Color coding: To enhance visibility, events can be highlighted in colors, for example, the entrance is green, the exit is red. This helps to quickly identify the type of event and allows you to quickly respond to changes.

[Sample Python code for updating data update_data.py file](update_data.py)

