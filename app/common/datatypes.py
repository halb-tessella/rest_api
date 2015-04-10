__author__ = 'andreap'
from flask import current_app


class DataType():

    def __init__(self, name, datasources = []):
        self.name = name
        self.datasources = datasources


class DataSource():

     def __init__(self, name, datatypes = []):
        self.name = name
        self.datatypes = datatypes



class DataTypes():
    ''' Singleton representing all the known datatypes with associated datasources
    '''

    def __init__(self):
        self.datatypes = {}
        self.datasources = {}
        for datatype_name,datasources in current_app.config.DATATYPES.items():
            self.datatypes[datatype_name] = DataType(datatype_name, datasources)
            for datasource_name in datasources:
                if datasource_name not in self.datasources:
                    self.datasources[datasource_name] = DataSource(datasource_name,[datatype_name])
                else:
                    self.datasources[datasource_name].datatypes.append()


    def get_datasources(self, datatype):
        return self.datatypes[datatype].datasources

    def get_datatypes(self, datasource):
        return self.datasources[datasource].datatypes


