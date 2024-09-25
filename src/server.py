import os
import asyncio
from config import Config, setConfig, create_app
from hypercorn.config import Config
from hypercorn.asyncio import serve

if __name__ == '__main__':
    is_prod = False
    config = Config()

    if os.environ.get('WORK_ENV') == 'PROD':
        config.debug = False 
        is_prod = True
    else:
        config.debug = True
        
    
    setConfig(config)
    app = create_app(config)
    asyncio.run(main=serve(app, Config()), debug=config.debug)
