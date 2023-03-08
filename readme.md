# Description

Line manager project is a proof of concept for identifying the line manager using containers.

each container is linked with the parent container and the children containers. each container has the following attributes:

- parentContainer: reference to the parent container
- childContainers: list of children containers references
- employees: list of the container's employees
- manager: a manager of the container

The manager can be defined based on the job type of the employees, is it supervisory? Note that the additional tasks have priority when deciding who is the manager of a container. Even if there is no supervisory job in a certain container we can travel up to the parent container to find the manager or even to the siblings' containers if needed.

# Installation

1. Install python: https://www.python.org/downloads/
2. Create virtual environment: https://docs.python.org/3/library/venv.html
3. Activate virtual environment: https://docs.python.org/3/library/venv.html#how-venvs-work
4. Install dependencies: `pip install -r /path/to/requirements.txt`

# Usage

After activating the virtual environment and installing the dependencies run the following command on the terminal:

`python /path/to/main.py`

# Notes

The excel sheet should contain the following columns so the program can run properly:

- Emp Id: employee SQU ID
- Emp Name: employee name
- Branch Code
- Branch
- Department Code
- Department
- Section Code
- Section
- Parent Container: the code of the parent department or section
- Designation
- is job add task: is designation additional task
- is job supervisory: is designation supervisory
- has add task: dose the employee have active additional task

# Credits

Information and Data Section, Human Resources Department
