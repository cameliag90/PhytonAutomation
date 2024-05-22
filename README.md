<<<<<<< HEAD
# PhytonAutomation
=======
1. Install PyCharm:

- Download and install PyCharm from the JetBrains website.
- Follow the installation instructions for your operating system.

2. Clone project from GitHub:
- Open PyCharm
- Go to Git tab and select Clone
- Fill in the URL with: https://github.com/cameliag90/PhytonAutomation.git
- Click clone

3. Set Up a Virtual Environment (Optional but Recommended):

- Open the terminal within PyCharm (View > Tool Windows > Terminal).
- Navigate to the project directory.
- Create a virtual environment by running: python -m venv venv
- Activate the virtual environment: venv\Scripts\activate

4. Install Packages from requirements.txt:
When setting up a new environment, you can install all required packages using the requirements.txt file:

- pip install -r requirements.txt

5. Install Selenium:

- in the virtual environment, install Selenium using pip: pip install selenium

6. Download WebDriver:

- Download the WebDriver executable for your preferred browser (e.g., Chrome, Firefox).
- Place the WebDriver executable in your project directory.


7. Run Test Script:

- Right-click on your Python file in PyCharm.
- Choose "Run 'filename'" to execute your test script.
or
- Open terminal and run: pytest path_to_test - for one test (ex: pytest backendTests/1_get_users_list.py )
>>>>>>> master
