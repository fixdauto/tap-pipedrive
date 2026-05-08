from tap_pipedrive.stream import PipedriveV1IncrementalStream

class UsersStream(PipedriveV1IncrementalStream):
    endpoint = 'users'
    schema = 'users'
    key_properties = ['id']
    replication_method = 'FULL_TABLE'
