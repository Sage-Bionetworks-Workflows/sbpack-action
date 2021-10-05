import configparser
import os
import subprocess

# Set env variable
app_name = os.getenv("INPUT_APP_NAME")
api_endpoint = os.getenv("INPUT_API_ENDPOINT")
# {user}/{project}/{app}
workflow_path = os.getenv("INPUT_WORKFLOW_PATH")
auth_token = os.getenv("INPUT_AUTH_TOKEN")


# Write SBG config
config = configparser.ConfigParser()
config['sbg'] = {'api_endpoint': api_endpoint,
                 'auth_token': auth_token}

sbg_folder = os.path.expanduser("~/.sevenbridges")
os.mkdir(sbg_folder)

with open(os.path.join(sbg_folder, "credentials"), 'w') as configfile:
    config.write(configfile)

cmd = ['sbpack', 'sbg', app_name, workflow_path]
subprocess.call(cmd)
