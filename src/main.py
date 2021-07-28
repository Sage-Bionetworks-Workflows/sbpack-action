import os
import subprocess

# Set env variable
app_name = os.getenv("INPUT_APP_NAME")
# {user}/{project}/{app}
workflow_path = os.getenv("INPUT_WORKFLOW_PATH")


cmd = ['sbpack', 'sbg', app_name, workflow_path]
subprocess.check_call(cmd)
