from dataclasses import dataclass
from quart import Blueprint
from quart_schema import validate_response

blueprint = Blueprint('health', __name__, url_prefix = '/health')

@dataclass
class Status:
    status: str

@blueprint.route('/', methods=['GET'])
@validate_response(Status, 200)
async def health():
    '''
    Static health endpoint that always returns a success message.
    '''
    return Status(status = 'OK'), 200
