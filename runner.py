import sys
from streamlit.web import cli as stcli

sys.argv = ['streamlit', 'run', 'DASHBOARD.py']
sys.exit(stcli.main())