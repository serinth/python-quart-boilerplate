from dataclasses import dataclass
from quart import Blueprint
from quart_schema import validate_response

blueprint = Blueprint('health', __name__, url_prefix = '/health')

@dataclass
class Status:
    status: str

@blueprint.route('/', methods=['GET'])
@validate_response(model_class=Status, status_code=200)
async def health() -> tuple[Status, int]:
    '''
    Static health endpoint that always returns a success message.
    '''
    return Status(status = 'OK'), 200
