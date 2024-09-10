# This is an interface to supplement CRR Market Operators

### To run this application, open 'Command Prompt', navigate to a directory you want the repository to be saved into, then enter:
```git clone https://businessbitbucket.ercot.com/scm/~dsherry/operatorinterface.git```

You will be asked to log in to Bitbucket inside of the Command Prompt, using your Windows username/password

When cloning is complete enter:

```cd operatorinterface```

```python -m venv operatorenv```

```operatorenv\Scripts\activate.bat```

```pip install -r requirements.txt```

You will only need to do the commands above once. Afterwards you can open the project in your IDE of choice or from Command Prompt, and run the following code to launch the app/website:

```streamlit run homepage.py```

The application should open up in a new tab of a browser



Contents include:
- Popular links used by operators
- SQL queries that generate directly in the app (download option available)
- Automations that streamline operator operations
- A way to compare two Excel sheets easily



