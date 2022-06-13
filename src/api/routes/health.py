import asyncio
from quart_openapi import PintBlueprint, Resource

blueprint = PintBlueprint('health', __name__)

@blueprint.route('/health')
#@blueprint.doc 
class Health(Resource):
    async def get(self):
        return {'status': 'OK'}
