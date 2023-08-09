import logging
from fastapi import FastAPI, Response, status
from dotenv import load_dotenv
import os


load_dotenv()
app = FastAPI(name='Settings repo')

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(message)s", level=logging.DEBUG
)


@app.get('/setting/{name}')
def get_setting_by_name(name: str, response: Response):
    logging.debug(f'Received request for {name}')
    name = name.upper()
    setting = os.getenv(name)
    if not setting:
        logging.debug('Setting not found, returning 404.')
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Setting {name} not found.'}
    logging.debug('Sucessfully returning.')
    return {name: setting}
