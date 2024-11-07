# Wichteln, but as web app

This simple web app allows you to remotely and asynchronously determine who gifts whom:
- Distribute a password to each person and update `app.py` accordingly.
- Agree on a seed
- Run the web app and distribute the link
- Each individual enters their name, password + seed and learns who they should gift

## Running the web app
- Install the minimal `nginx` config (edit beforehand) + start `nginx`
- Activate venv: `python -m venv .venv && source .venv/bin/activate`
- Install python dependencies: `pip install -r requirements`
- Start the app: `chmod +x launch.sh && ./launch.sh`
