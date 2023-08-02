from backend.custom_error import Error
from .help import *
from tabulate import tabulate

class Symbol:
    def __init__(self):
        self.table = []
        self.scopes = [GLOBAL]
        self.custom_error_listener = Error()
        self.ERRORS = self.custom_error_listener.ERRORS

    def getTable(self):
        return self.table
    
    def push_scope(self, scope):
        self.scopes.append(scope)

    def pop_scope(self):
        self.scopes.pop()

    def insert(self, name, typ, kind, scope, line, value=None):
        scope_variables = filter(lambda x: x['scope'] == scope, self.table)
        if (name, kind) in map(lambda x: (x['name'], x['kind']), scope_variables):
            if kind == 'parameter':
                for p in reversed(self.table):
                    if p['kind'] == 'method':
                        break
                    elif p['name'] == name and p['kind'] == kind and p['scope'] == scope and p['line'] == line :
                        self.custom_error_listener.error(KIND_TABLE_ERROR[kind] + ' ' + name + ' ya declarada ', line)
            else:
                self.custom_error_listener.error(KIND_TABLE_ERROR[kind] + ' ' + name + ' ya declarada ', line)

        self.table.append({'name': name, 'type': typ, 'kind': kind, 'scope': scope, 'line': line, 'value': value})

    def get(self, name, line,scope=None):
        if scope is None:
            scope = self.get_scope()

        scope_variables = filter(lambda x: x['scope'] == scope, self.table)
        for variable in scope_variables:
            if variable['name'] == name:
                return variable

        self.custom_error_listener.error('Variable ' + name + ' no declarada', line)

    def set(self, name, line, value):
        for scope in reversed(self.scopes):
            for row in self.table:
                if row['name'] == name and row['scope'] == scope:
                    row['value'] = value
                    return

        self.custom_error_listener.error('Variable ' + name + ' no declarada', line)

    def get_scope(self):
        return self.scopes[-1]

    def __str__(self):
        table = map(lambda x: x.values(), self.table)
        return tabulate(table, headers=['name', 'type', 'kind', 'scope', 'line', 'value'])
