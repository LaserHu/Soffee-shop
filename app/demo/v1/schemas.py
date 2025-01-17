# -*- coding: utf-8 -*-

import six
from jsonschema import RefResolver
# TODO: datetime support

class RefNode(object):

    def __init__(self, data, ref):
        self.ref = ref
        self._data = data

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __setitem__(self, key, value):
        return self._data.__setitem__(key, value)

    def __getattr__(self, key):
        return self._data.__getattribute__(key)

    def __iter__(self):
        return self._data.__iter__()

    def __repr__(self):
        return repr({'$ref': self.ref})

    def __eq__(self, other):
        if isinstance(other, RefNode):
            return self._data == other._data and self.ref == other.ref
        elif six.PY2:
            return object.__eq__(other)
        elif six.PY3:
            return object.__eq__(self, other)
        else:
            return False

    def __deepcopy__(self, memo):
        return RefNode(copy.deepcopy(self._data), self.ref)

    def copy(self):
        return RefNode(self._data, self.ref)

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1'

definitions = {'definitions': {'postAnOrder': {'type': 'object', 'properties': {'orderID': {'type': 'integer', 'format': 'int64', 'example': 12345}, 'type': {'type': 'string', 'enum': ['Latte Price: $6.0', 'Espresso Price: $4.0', 'Cappuccino Price: $8.0', 'Irish Coffee Price: $12.0'], 'example': 'Latte Price: $6.0'}, 'size': {'type': 'string', 'enum': ['Small', 'Regular', 'Large', 'Extra large'], 'example': 'Regular'}, 'quantity': {'type': 'integer', 'format': 'int32', 'example': 1}, 'cost': {'type': 'number', 'format': 'float', 'example': '6.0'}, 'status': {'type': 'string', 'enum': ['Unpaid', 'Paid', 'Canceled', 'Finished'], 'example': 'Unpaid'}, 'time': {'type': 'string', 'format': 'date-time'}, 'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:POST; href:https://coffee.api.au/v1/orders'}, 'list all orders': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders'}, 'get this order': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders/12345'}, 'amend this order': {'type': 'string', 'example': 'method:PUT href:https://coffee.api.au/v1/orders/12345'}, 'cancel this order': {'type': 'string', 'example': 'method:DELETE href:https://coffee.api.au/v1/orders/12345'}}}}}, 'getOrders': {'type': 'object', 'properties': {'orderID': {'type': 'integer', 'format': 'int64', 'example': 12345}, 'type': {'type': 'string', 'enum': ['Latte', 'Espresso', 'Cappuccino', 'Irish Coffee'], 'example': 'Latte'}, 'size': {'type': 'string', 'enum': ['Small', 'Regular', 'Large', 'Extra large'], 'example': 'Regular'}, 'quantity': {'type': 'integer', 'format': 'int32', 'example': 1}, 'cost': {'type': 'number', 'format': 'float', 'example': '6.0'}, 'status': {'type': 'string', 'enum': ['Unpaid', 'Paid', 'Canceled', 'Finished'], 'example': 'Unpaid'}, 'time': {'type': 'string', 'format': 'date-time'}, 'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:GET; href:https://coffee.api.au/v1/orders'}, 'list all orders': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders'}, 'get an order': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders/12345'}, 'amend an order': {'type': 'string', 'example': 'method:PUT href:https://coffee.api.au/v1/orders/12345'}, 'cancel an order': {'type': 'string', 'example': 'method:DELETE href:https://coffee.api.au/v1/orders/12345'}}}}}, 'putAnOrder': {'type': 'object', 'properties': {'orderID': {'type': 'integer', 'format': 'int64', 'example': 12345}, 'type': {'type': 'string', 'enum': ['Latte Price: $6.0', 'Espresso Price: $4.0', 'Cappuccino Price: $8.0', 'Irish Coffee Price: $12.0'], 'example': 'Latte Price: $6.0'}, 'size': {'type': 'string', 'enum': ['Small', 'Regular', 'Large', 'Extra large'], 'example': 'Regular'}, 'quantity': {'type': 'integer', 'format': 'int32', 'example': 1}, 'cost': {'type': 'number', 'format': 'float', 'example': '6.0'}, 'status': {'type': 'string', 'enum': ['Unpaid', 'Paid', 'Canceled', 'Finished'], 'example': 'Unpaid'}, 'time': {'type': 'string', 'format': 'date-time'}, 'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:PUT; href:https://coffee.api.au/v1/orders/12345'}, 'list all orders': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders'}, 'get this order': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders/12345'}, 'amend this order': {'type': 'string', 'example': 'method:PUT href:https://coffee.api.au/v1/orders/12345'}, 'cancel this order': {'type': 'string', 'example': 'method:DELETE href:https://coffee.api.au/v1/orders/12345'}}}}}, 'failToAmend': {'type': 'object', 'properties': {'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:PUT; href:https://coffee.api.au/v1/orders/12345'}, 'list all orders': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders'}, 'amend another order': {'type': 'string', 'example': 'method:PUT href:https://coffee.api.au/v1/orders/12345'}}}}}, 'getAnOrder': {'type': 'object', 'properties': {'orderID': {'type': 'integer', 'format': 'int64', 'example': 12345}, 'type': {'type': 'string', 'enum': ['Latte', 'Espresso', 'Cappuccino', 'Irish Coffee'], 'example': 'Latte'}, 'size': {'type': 'string', 'enum': ['Small', 'Regular', 'Large', 'Extra large'], 'example': 'Regular'}, 'quantity': {'type': 'integer', 'format': 'int32', 'example': 1}, 'cost': {'type': 'number', 'format': 'float', 'example': '6.0'}, 'status': {'type': 'string', 'enum': ['Unpaid', 'Paid', 'Canceled', 'Finished'], 'example': 'Unpaid'}, 'time': {'type': 'string', 'format': 'date-time'}, 'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:GET; href:https://coffee.api.au/v1/orders/12345'}, 'list all orders': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders'}, 'amend this order': {'type': 'string', 'example': 'method:PUT href:https://coffee.api.au/v1/orders/12345'}, 'cancel this order': {'type': 'string', 'example': 'method:DELETE href:https://coffee.api.au/v1/orders/12345'}}}}}, 'failToGet': {'type': 'object', 'properties': {'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:GET; href:https://coffee.api.au/v1/orders/12345'}, 'list all orders': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders'}, 'get another order': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders/12345'}}}}}, 'deleteAnOrder': {'type': 'object', 'properties': {'orderID': {'type': 'integer', 'format': 'int64', 'example': 12345}, 'type': {'type': 'string', 'enum': ['Latte', 'Espresso', 'Cappuccino', 'Irish Coffee'], 'example': 'Latte'}, 'size': {'type': 'string', 'enum': ['Small', 'Regular', 'Large', 'Extra large'], 'example': 'Regular'}, 'quantity': {'type': 'integer', 'format': 'int32', 'example': 1}, 'cost': {'type': 'number', 'format': 'float', 'example': '6.0'}, 'status': {'type': 'string', 'enum': ['Unpaid', 'Paid', 'Canceled', 'Finished'], 'example': 'Unpaid'}, 'time': {'type': 'string', 'format': 'date-time'}, 'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:DELETE; href:https://coffee.api.au/v1/orders/12345'}, 'list all the other orders': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders'}, 'cancel another order': {'type': 'string', 'example': 'method:DELETE href:https://coffee.api.au/v1/orders/12345'}}}}}, 'failToDelete': {'type': 'object', 'properties': {'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:DELETE; href:https://coffee.api.au/v1/orders/12345'}, 'list all the other orders': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders'}, 'cancel another order': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders/12345'}}}}}, 'payAnOrder': {'type': 'object', 'properties': {'orderID': {'type': 'integer', 'format': 'int64', 'example': 12345}, 'type': {'type': 'string', 'enum': ['Latte', 'Espresso', 'Cappuccino', 'Irish Coffee'], 'example': 'Latte'}, 'size': {'type': 'string', 'enum': ['Small', 'Regular', 'Large', 'Extra large'], 'example': 'Regular'}, 'quantity': {'type': 'integer', 'format': 'int32', 'example': 1}, 'cost': {'type': 'number', 'format': 'float', 'example': '6.0'}, 'status': {'type': 'string', 'enum': ['Unpaid', 'Paid', 'Canceled', 'Finished'], 'example': 'paid'}, 'time': {'type': 'string', 'format': 'date-time'}, 'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:PUT; href:https://coffee.api.au/v1/payment/12345'}, 'list all orders': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders'}, 'pay another order': {'type': 'string', 'example': 'method:PUT href:https://coffee.api.au/v1/payment/12345'}}}}}, 'failToPay': {'type': 'object', 'properties': {'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:PUT; href:https://coffee.api.au/v1/payment/12345'}, 'list all orders': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders'}, 'pay another order': {'type': 'string', 'example': 'method:PUT href:https://coffee.api.au/v1/payment/12345'}}}}}, 'getPayment': {'type': 'object', 'properties': {'orderID': {'type': 'integer', 'format': 'int64', 'example': 12345}, 'type': {'type': 'string', 'enum': ['Latte', 'Espresso', 'Cappuccino', 'Irish Coffee'], 'example': 'Latte'}, 'size': {'type': 'string', 'enum': ['Small', 'Regular', 'Large', 'Extra large'], 'example': 'Regular'}, 'quantity': {'type': 'integer', 'format': 'int32', 'example': 1}, 'cost': {'type': 'number', 'format': 'float', 'example': '6.0'}, 'status': {'type': 'string', 'enum': ['Unpaid', 'Paid', 'Canceled', 'Finished'], 'example': 'unpaid'}, 'time': {'type': 'string', 'format': 'date-time'}, 'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:GET; href:https://coffee.api.au/v1/payment/12345'}, 'list all orders': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders'}, 'pay another order': {'type': 'string', 'example': 'method:PUT href:https://coffee.api.au/v1/payment/12345'}}}}}, 'failToGetPayment': {'type': 'object', 'properties': {'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:GET; href:https://coffee.api.au/v1/payment/12345'}, 'list all orders': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/orders'}, 'get detail of another order': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/payment/12345'}}}}}, 'addCoffee': {'type': 'object', 'properties': {'type': {'type': 'string', 'example': 'Americano'}, 'time': {'type': 'string', 'format': 'date-time'}, 'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:POST; href:https://coffee.api.au/v1/coffees'}, 'list all coffee types': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/coffees'}}}}}, 'failToAddCoffee': {'type': 'object', 'properties': {'time': {'type': 'string', 'format': 'date-time'}, 'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:POST; href:https://coffee.api.au/v1/coffees'}, 'list all coffee types': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/coffees'}}}}}, 'getCoffee': {'type': 'object', 'properties': {'type0': {'type': 'string', 'example': 'Latte'}, 'type1': {'type': 'string', 'example': 'Espresso'}, 'type2': {'type': 'string', 'example': 'Cappuccino'}, 'type3': {'type': 'string', 'example': 'Irish Coffee'}, 'type4': {'type': 'string', 'example': 'Americano'}, 'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:GET; href:https://coffee.api.au/v1/coffees'}, 'add a new coffee': {'type': 'string', 'example': 'method:POST href:https://coffee.api.au/v1/coffees'}}}}}, 'deleteCoffee': {'type': 'object', 'properties': {'type0': {'type': 'string', 'example': 'Latte'}, 'type1': {'type': 'string', 'example': 'Espresso'}, 'type2': {'type': 'string', 'example': 'Cappuccino'}, 'type3': {'type': 'string', 'example': 'Irish Coffee'}, 'links': {'type': 'object', 'properties': {'link': {'type': 'string', 'example': 'rel:self; method:DELETE; href:https://coffee.api.au/v1/coffees/Americano'}, 'list all coffee types': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/coffees'}, 'delete another coffee': {'type': 'string', 'example': 'method:GET href:https://coffee.api.au/v1/coffees/Latte'}}}}}}, 'parameters': {}}

validators = {
    ('orders', 'POST'): {'args': {'required': ['type', 'size', 'quantity'], 'properties': {'type': {'description': 'What type of coffee do you want', 'type': 'string', 'enum': ['Latte Price: $6.0', 'Espresso Price: $4.0', 'Cappuccino Price: $8.0', 'Irish Coffee Price: $12.0']}, 'size': {'description': 'Which size do you want', 'type': 'string', 'enum': ['Small -$1.0', 'Regular +$0.0', 'Large +$1.0', 'Extra large +2.0'], 'default': 'Regular +$0.0'}, 'quantity': {'description': 'How many cups of coffee do you want', 'type': 'integer', 'format': 'int64', 'minimum': 1, 'maximum': 10, 'default': 1}}}},
    ('coffees', 'POST'): {'args': {'required': ['type'], 'properties': {'type': {'description': 'Add a new coffee to the menu', 'type': 'string'}}}},
}

filters = {
    ('orders', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/postAnOrder'}}, 400: {'headers': None, 'schema': {'type': 'object', 'properties': {'time': {'type': 'string', 'format': 'date-time'}}}}},
    ('orders', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/getOrders'}}, 404: {'headers': None, 'schema': {'type': 'object', 'properties': {'time': {'type': 'string', 'format': 'date-time'}}}}},
    ('orders_orderID', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/putAnOrder'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/failToAmend'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/failToAmend'}}},
    ('orders_orderID', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/getAnOrder'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/failToGet'}}},
    ('orders_orderID', 'DELETE'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/deleteAnOrder'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/failToDelete'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/failToDelete'}}},
    ('payment_orderID', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/payAnOrder'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/failToPay'}}, 409: {'headers': None, 'schema': {'$ref': '#/definitions/payAnOrder'}}},
    ('payment_orderID', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/getPayment'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/failToGetPayment'}}},
    ('coffees', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/addCoffee'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/failToAddCoffee'}}},
    ('coffees', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/getCoffee'}}, 404: {'headers': None, 'schema': {'type': 'object', 'properties': {'time': {'type': 'string', 'format': 'date-time'}}}}},
    ('coffees_type', 'DELETE'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/deleteCoffee'}}, 404: {'headers': None, 'schema': {'type': 'object', 'properties': {'time': {'type': 'string', 'format': 'date-time'}}}}},
}

scopes = {
}

resolver = RefResolver.from_schema(definitions)

class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True, resolver=None):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults, resolver=resolver)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None, resolver=None):
    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key or '$ref' in _schema:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema is not False:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, (dict, RefNode)):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize_ref(schema, data):
        if resolver == None:
            raise TypeError("resolver must be provided")
        ref = schema.get(u"$ref")
        scope, resolved = resolver.resolve(ref)
        if resolved.get('nullable', False) and not data:
            return {}
        return _normalize(resolved, data)

    def _normalize(schema, data):
        if schema is True or schema == {}:
            return data
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
            'ref': _normalize_ref
        }
        type_ = schema.get('type', 'object')
        if type_ not in funcs:
            type_ = 'default'
        if schema.get(u'$ref', None):
            type_ = 'ref'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors
