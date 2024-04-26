from src.project_files.config.v1 import BaseSettingsWrapper

class MongoConfig(BaseSettingsWrapper):
    mongo_host = "localhost"
    
mongo_config = MongoConfig()