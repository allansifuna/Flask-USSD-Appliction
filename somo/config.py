import os


class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = 'kdhjgvfcmvyugdiqygiqebudb'
    # SERVER_NAME='http://localhost:3000/'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'somo.db')
    # SQLALCHEMY_DATABASE_URI='postgresql://uwzryxcyjxfpgx:420d665f19c781fd8ebea9afc8de4a64955974c8f1a4440fa11cbd2655b6cb1b@ec2-34-239-241-25.compute-1.amazonaws.com:5432/dfb6nb8fgia5vn'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = 'redis://h:p013e746cf1e2c72dc4c478b0e3cd86cd8f94829a6bf548340e1636c0ea6e6db1@ec2-34-192-197-232.compute-1.amazonaws.com:17429'
    APP_NAME = "SOMI"
    # SERVER_NAME='schoolpas.com'
